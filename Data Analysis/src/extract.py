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
def setup_and_prepare_directories(clear_target_directory=True):
    if os.name == 'nt': 
        os.system("color") # if on Windows we need to activate colored print
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
def __get_gibberish_string_for_student(student_code, len=6):
    if student_code not in student_code_to_gibberish.keys():
        gibberish = ''.join(random.choice(string.ascii_lowercase) for _ in range(len))
        while(gibberish in student_code_to_gibberish.values()):
            gibberish = ''.join(random.choice(string.ascii_letters) for _ in range(len))
        student_code_to_gibberish[student_code] = gibberish
    return student_code_to_gibberish[student_code]

# Finds the Scoreboard-file in bookkeeping.SOURCE_DIRECTORY corresponding to project_name.
# Returns a dictionary with entries of the form (anonymized student, score) (e.g. ("abcdef", 1.0)).
# You most probably do not want to call this yourself.
def __get_scores_for_export(project_name):
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

# Checks whether there possibly is a [code]expert project export (of one task) at bookkeeping.SOURCE_DIRECTORY/project_name.
# If that is the case, extracts and anonimizes the relevant files (testcases.csv from cx_audit and main.py) to bookkeeping.TARGET_DIRECTORY/project_name.
# Also includes information about the score of the student.
def extract_project(project_name):
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
    scores = __get_scores_for_export(project_name)
    n_students = 0
    n_existing_audit_files = 0
    for root, _, _ in os.walk(source_path): # recursively traverse the source
        if os.path.basename(root) == "project": # the folders we are interested in are called "project"
            n_students += 1
            root = root.replace("\\", "/") # prepare root for regex action
            student_code = re.findall("[^/]+", re.findall("(?:/[^/]+/submission|/[^/]+/regrade)", root)[0])[0] # extract student code (aka ETH-Kuerzel) from path
            # If you want to have an 'or' match without having the split into match groups just add a '?:' to the beginning of the 'or' match.
            # https://stackoverflow.com/questions/24593824/why-does-re-findall-return-a-list-of-tuples-when-my-pattern-only-contains-one-gr
            if len(student_code) == 0: # no match
                print(colored("Could not find student code in " + root, "red"))
                continue
            if __get_gibberish_string_for_student(student_code) not in scores:
                print(colored("Could not find score of student " + student_code + ", so I will skip this student", "yellow"))
                continue
            # Find and move main file:
            src = os.path.join(source_path, root, "main.py")
            if not os.path.isfile(src):
                print(colored("Could not main.py of student " + student_code + ", so I will skip this student", "yellow"))
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
                with open(dest, mode='a') as test_results: # append content to csv
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
    
# Given a list of project names, tries to extract a multitude of projects from bookkeeping.SOURCE_DIRECTORY (more info in extract_project).
# If include is something other than [] (e.g. ["GDI_2022_M_1_...", ...]), then only the given projects are extracted (assuming they exist).
# If include is [], then all existing projects that are not in exclude are extracted.
def extract_projects(include=[], exclude=[]):
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