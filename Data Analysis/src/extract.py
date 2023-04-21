import csv
import os
import random
import re # regex
import shutil # moving files through directories
import string
from termcolor import colored # for printing funny colored text

import bookkeeping

# Call this before any other method here.
# Expects that bookkeeping.SOURCE_DIRECTORY is set to an existing path (the location is supposed to contain [code]expert project exports).
# Creates bookkeeping.TARGET_DIRECTORY.
# If clear_target_directory is set to true (default) and bookkeeping.TARGET_DIRECTORY already exists, then bookkeeping.TARGET_DIRECTORY is wiped.
def setup_and_prepare_directories(clear_target_directory : bool = True) -> None:
    if os.name == 'nt':
        # If on Windows we need to activate colored print:
        os.system("color")
    if not os.path.exists(bookkeeping.SOURCE_DIRECTORY):
        exit(colored("Source directory", bookkeeping.SOURCE_DIRECTORY, "does not exist", "red"))
    if os.path.exists(bookkeeping.TARGET_DIRECTORY) and clear_target_directory:
        try:
            shutil.rmtree(bookkeeping.TARGET_DIRECTORY)
        except OSError as error:
            exit(colored("Failed to delete directory\n", error, "red"))
    if not os.path.exists(bookkeeping.TARGET_DIRECTORY):
        os.mkdir(bookkeeping.TARGET_DIRECTORY)

# Maintains a unique random string for each student code:
student_code_to_gibberish = {}

# Given a student code (aka ETH-Kuerzel) anonimizes it. 
# When the code is encountered for the first time, a new random gibberish string of size len (default 6) is generated for it and persisted in student_code_to_gibberish. 
# On each subsequent encounter of the same student code, the corresponding gibberish is simply returned.
# You most probably do not want to call this yourself.
def __get_gibberish_string_for_student(student_code : str, len : int = 6) -> str:
    if student_code not in student_code_to_gibberish.keys():
        gibberish = ''.join(random.choice(string.ascii_lowercase) for _ in range(len))
        while(gibberish in student_code_to_gibberish.values()):
            gibberish = ''.join(random.choice(string.ascii_letters) for _ in range(len))
        student_code_to_gibberish[student_code] = gibberish
    return student_code_to_gibberish[student_code]

# Finds the Scoreboard-file in bookkeeping.SOURCE_DIRECTORY corresponding to project_name.
# Returns a dictionary with entries of the form (anonymized student, score) (e.g. ("abcdef", 1.0)).
# You most probably do not want to call this yourself.
def __get_scores_for_export(project_name : str) -> dict:
    course_prefix = re.findall(str(bookkeeping.COURSE_PERFIXES).replace(", ", "|").replace("'", "")[1:-1], project_name)
    year = re.findall(str(bookkeeping.YEARS).replace(", ", "|").replace("'", "")[1:-1], project_name)
    module_number = re.findall("M_\d", project_name)
    if len(course_prefix) == 0 or len(year) == 0 or len(module_number) == 0:
        exit(colored("Could not find Scoreboard file for project " + project_name, "red"))
    course_prefix = course_prefix[0] # unpack regex result
    year = year[0] # unpack regex result
    module_number = module_number[0][2] # unpack regex result
    scoreboard_file = os.path.join(bookkeeping.SOURCE_DIRECTORY, course_prefix + "_" + year + "_" + "Scoreboard.csv")
    scores = {}
    with open(scoreboard_file, mode='r') as scoreboard: # read content from csv
        for i, row in enumerate(csv.reader(scoreboard, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)):
            if i == 0: # get indeces for the columns with the username and the score of the relevant module presentation
                name_index = row.index("Username")
                row_index = row.index("Modul " + module_number)
            elif "LTI" in row[name_index]: # skip LTI Accounts
                continue
            else:
                score = re.findall("1|0\.5|0", row[row_index]) # find score
                if len(score) > 0:
                    scores[__get_gibberish_string_for_student(row[name_index])] = float(score[0]) # anonymize
                else:
                    scores[__get_gibberish_string_for_student(row[name_index])] = -1.0 # encode everything non-graded as -1.0
    return scores

# Extracts student code (aka ETH-Kuerzel) from path.
def __find_student_code_in_path(path : str) -> str:
    student_code_with_surroundings = re.findall("(?:/[^/]+/submission|/[^/]+/regrade)", path.replace("\\", "/"))
    # If you want to have an 'or' match without having the split into match groups just add a '?:' to the beginning of the 'or' match.
    # https://stackoverflow.com/questions/24593824/why-does-re-findall-return-a-list-of-tuples-when-my-pattern-only-contains-one-gr
    # Also note that path.replace("\\", "/") simplifys our regexes as we have to escape less stuff.
    if len(student_code_with_surroundings) == 0: # no match
        return ""
    student_code = re.findall("[^/]+", student_code_with_surroundings[0])
    if len(student_code) == 0: # no match
        return ""
    return student_code[0]

# Checks whether there possibly is a [code]expert project export (of one task) at bookkeeping.SOURCE_DIRECTORY/project_name.
# If that is the case, extracts and anonimizes the relevant files (testcases.csv from cx_audit and main.py) to bookkeeping.TARGET_DIRECTORY/project_name.
# Also includes information about the score of the student.
# If there is a version of the project with "fixed_main_exec" then it is included as well.
def extract_project(project_name : str) -> str:
    # Setup path stuff:
    source_path = os.path.join(bookkeeping.SOURCE_DIRECTORY, project_name)
    if not os.path.exists(source_path):
        print(colored("Could not find project export at " + source_path, "red"))
        return
    target_path = os.path.join(bookkeeping.TARGET_DIRECTORY, project_name)
    if not os.path.exists(target_path):
        os.mkdir(target_path)
    else:
        print(colored("Project already exported, consider deleting it", "red"))
        return
    # Get scores:
    scores = __get_scores_for_export(project_name)
    # Prepare bookkeeping:
    n_students = 0
    n_existing_audit_files = 0
    # Recursively traverse the source:
    for root, _, _ in os.walk(source_path):
        if os.path.basename(root) == "project": # the folders we are interested in are called "project"
            n_students += 1
            student_code = __find_student_code_in_path(root)
            if student_code == "": # no match
                print(colored("Could not find student code in " + root, "red"))
                continue
            if __get_gibberish_string_for_student(student_code) not in scores:
                print(colored("Could not find score of student " + student_code + ", so I will skip this student", "yellow"))
                continue
            # Find and move main file:
            src = os.path.join(source_path, root, "main.py")
            if not os.path.isfile(src):
                print(colored("Could not find main.py of student " + student_code + ", so I will skip this student", "yellow"))
                continue
            dest = os.path.join(target_path, __get_gibberish_string_for_student(student_code) + "_main.py") # anonymize
            # print("Moving", src, "to", dest) # uncomment for verbose output
            shutil.copy(src, dest) # copy and rename main.py
            # Find and move audit file:
            src = os.path.join(source_path, root, "cx_audit", "testcases.csv")
            if os.path.isfile(src): # audit file exists
                n_existing_audit_files += 1
                dest = os.path.join(target_path, __get_gibberish_string_for_student(student_code) + "_testresults.csv") # anonymize
                # print("Moving", src, "to", dest) # uncomment for verbose output
                shutil.copy(src, dest) # copy and rename testcases.csv
                with open(dest, mode='a') as test_results: # append score to csv
                    writer = csv.writer(test_results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
                    writer.writerow(["Presentation Score", "Score: " + str(scores[__get_gibberish_string_for_student(student_code)])])
                    # TODO: include other scores
    print("Successfully moved and renamed files from", n_students, "students", end=' ')
    if n_students == n_existing_audit_files: # print info on number of found audit (test result) files
        print(colored(str(n_existing_audit_files) + "/" + str(n_students) + " audit file(s)", "green"))
    elif n_existing_audit_files >= n_students/2:
        print(colored(str(n_existing_audit_files) + "/" + str(n_students) + " audit file(s)", "yellow"))
    else:
        print(colored(str(n_existing_audit_files) + "/" + str(n_students) + " audit file(s)", "red"))
    # Possibly also extract the audit info of a version of the project with "fixed_main_exec":
    fixed_main_exec_source_path = os.path.join(bookkeeping.SOURCE_DIRECTORY, project_name + "_fixed_main_exec")
    # Prepare bookkeeping:
    n_existing_fixed_main_exec_audit_files = 0
    if os.path.exists(fixed_main_exec_source_path):
        print("Found a fixed_main_exec version of the project, processing", (project_name + "_fixed_main_exec"))
        # Again recursively traverse the source:
        for root, _, _ in os.walk(fixed_main_exec_source_path):
            if os.path.basename(root) == "project": # the folders we are interested in are called "project"
                student_code = __find_student_code_in_path(root)
                if student_code == "": # no match
                    print(colored("Could not find student code in " + root, "red"))
                    continue
                if __get_gibberish_string_for_student(student_code) not in scores:
                    print(colored("Could not find score of student " + student_code + ", so I will skip this student", "yellow"))
                    continue
                # We are actually not interested in the main files; those are the same as in the orignial project
                # Find and audit file and store information in the already existing (extracted) audit file of the original project:
                src = os.path.join(fixed_main_exec_source_path, root, "cx_audit", "testcases.csv")
                if os.path.isfile(src): # audit file exists
                    n_existing_fixed_main_exec_audit_files += 1
                    dest = os.path.join(target_path, __get_gibberish_string_for_student(student_code) + "_testresults.csv") # get dest path from original project
                    with open(src, mode='r') as fixed_main_exec_test_results: # read from "fixed_main_exec" audit file
                        with open(dest, mode='a') as test_results: # append score to exported audit file from original project
                            writer = csv.writer(test_results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
                            for row in csv.reader(fixed_main_exec_test_results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL):
                                row[0] += " fixed main_exec"
                                writer.writerow(row)
        if n_existing_fixed_main_exec_audit_files == n_existing_audit_files:
            print(colored("Found the same number of audit files", "green"))
        else:
            print(colored("Found a different number of audit files: " + str(n_existing_fixed_main_exec_audit_files) + " vs " + str(n_existing_audit_files), "yellow"))
    else:
        print(colored("Did not find a fixed_main_exec version of the project", "yellow"))
    
# Given a list of project names, tries to extract a multitude of projects from bookkeeping.SOURCE_DIRECTORY (more info in extract_project).
# If include is something other than [] (e.g. ["GDI_2022_M_1_...", ...]), then only the given projects are extracted (assuming they exist).
# If include is [], then all existing projects that are not in exclude are extracted.
def extract_projects(include : list = [], exclude : list = []) -> None:
    if include == []:
        for project_name in os.listdir(bookkeeping.SOURCE_DIRECTORY):
            if project_name not in exclude and os.path.isdir(os.path.join(bookkeeping.SOURCE_DIRECTORY, project_name)):
                print("Processing", project_name)
                extract_project(project_name)
                print()
    else:
        for project_name in include:
            if os.path.isdir(os.path.join(bookkeeping.SOURCE_DIRECTORY, project_name)):
                print("Processing", project_name)
                extract_project(project_name)
                print()