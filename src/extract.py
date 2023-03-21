import csv 
import os
import random
import re # regex
import shutil # moving files through directories
import string
from termcolor import colored # for printing funny colored text

student_code_to_gibberish = {} # maintains a unique random string for each student code

# Given a student code anonimizes it. 
# When the code is encountered for the first time, a new random gibberish string of size len is generated for it and persisted in student_code_to_gibberish. 
# On each subsequent encounter of the same student code, the corresponding gibberish is simply returned.
def get_gibberish_string_for_student(student_code, len=6):
    if student_code not in student_code_to_gibberish.keys():
        gibberish = ''.join(random.choice(string.ascii_letters) for _ in range(len))
        while(gibberish in student_code_to_gibberish.values()):
            gibberish = ''.join(random.choice(string.ascii_letters) for _ in range(len))
        student_code_to_gibberish[student_code] = gibberish
    return student_code_to_gibberish[student_code]

# Given a [code]Expert project source directory extracts/renames the relevant files (testcases.csv from cx_audit and main.py) to the target directory
def extract_project(source_directory, target_directory):
    n_students = 0
    n_audits = 0
    for root, dirs, files in os.walk(source_directory): # recursively traverse the source directory
        if os.path.basename(root) == "project": # the folders we are interested in are called "project"
            student_code = re.findall("[^/]+", re.findall("/[^/]+/submission", root.replace("\\", "/"))[0])[0] # extract student code (aka ETH-Kuerzel) from path
            n_students += 1 # count students so we know how many files to expect
            for file in files:
                if file == "main.py":
                    src = os.path.join(source_directory, root, file)
                    dest = os.path.join(target_directory, student_code + "_main.py")
                    # print("Moving", src, "to", dest) # uncomment for verbose output
                    shutil.copy(src, dest) # copy and rename main.py
            for dir in dirs:
                if dir == "cx_audit":
                    src = os.path.join(source_directory, root, dir, "testcases.csv")
                    dest = os.path.join(target_directory, student_code + "_testcases.csv")
                    # print("Moving", src, "to", dest) # uncomment for verbose output
                    shutil.copy(src, dest) # copy and rename testcases.csv
                    n_audits += 1 # count number of present audit files (we can later generate the missing ones)
    print("Successfully moved and renamed files from", n_students, "students", end=' ')
    if n_students == n_audits: # print info on number of found audit files
        print(colored(str(n_audits) + "/" + str(n_students) + " audit files", "green"))
    elif n_audits >= n_students/2:
        print(colored(str(n_audits) + "/" + str(n_students) + " audit files", "yellow"))
    else:
        print(colored(str(n_audits) + "/" + str(n_students) + " audit files", "red"))

# Given a [code]Expert project and a path to a scoreboard file containing the grades of students extracts (and returns) 
# the grades of the students for the module presentation belonging to the project
def extract_presentation_grades_from_scoreboard(project_directory, path_to_scoreboard_file):
    modul_nummer = re.findall("M_\d", project_directory)[0][2] # find out what module the project belongs to
    student_grades_for_modul = {}
    with open(path_to_scoreboard_file, mode='r') as scoreboard: # read content from csv
        for i, row in enumerate(csv.reader(scoreboard, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL)):
            if(i == 0): # get indeces for the columns with the username and the grade of the relevant module presentation
                name_index = row.index("Username")
                row_index = row.index("Modul " + modul_nummer)
            elif("LTI" in row[name_index]): # skip LTI Accounts
                continue
            else:
                grade = re.findall("1|0\.5|0", row[row_index]) # find grade
                if(len(grade) > 0):
                    student_grades_for_modul[row[name_index]] = float(grade[0])
                else:
                    student_grades_for_modul[row[name_index]] = -1 # encode everything non-graded as -1.0
    return student_grades_for_modul

def get_n_test_cases(test_results_csv):
    with open(test_results_csv, mode='r') as test_results: # read content from csv
        row_count = 0
        for _ in csv.reader(test_results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL):
            row_count += 1
    return row_count

# Given a cleaned-up [code]Expert project and the grades of students for the module presentation belonging to the project 
# extracts the info from audit-files
def collect_student_data_from_project(project_directory, student_grades):
    results = {} # collect test results
    for _, _, files in os.walk(project_directory): # traverse files in project directory
        for file in files:
            if("testcases" in file):
                if len(results) == 0: # init results
                    n_test_cases = get_n_test_cases(os.path.join(project_directory, file))
                    # use file to count number of test cases for this project
                    for i in range(n_test_cases):
                        results["Test_" + str(i+1) + "_SUCCESS"] = 0
                        results["Test_" + str(i+1) + "_FAIL"] = 0
                        results["Test_" + str(i+1) + "_ERROR"] = 0
                        results["Test_" + str(i+1) + "_SKIP"] = 0
                        results["Test_" + str(i+1) + "_TRUE_POSITIVE"] = 0
                        results["Test_" + str(i+1) + "_FALSE_POSITIVE"] = 0
                        results["Test_" + str(i+1) + "_TRUE_NEGATIVE"] = 0
                        results["Test_" + str(i+1) + "_FALSE_NEGATIVE"] = 0
                student_name = re.findall(".+\_", file)[0][0:-1] # extract student code from file name
                if(student_name not in student_grades):
                    print(colored("Could not find grade of student " + student_name, "yellow"))
                    continue
                src = os.path.join(project_directory, file)
                with open(src, mode='r') as test_results: # read content from csv
                    for row in csv.reader(test_results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL):
                        if(row[1].__contains__("success")):
                            results[row[0].replace(" ", "_") + "_SUCCESS"] += 1
                            if(student_grades[student_name] == 1.0):
                                results[row[0].replace(" ", "_") + "_TRUE_POSITIVE"] += 1
                            elif(student_grades[student_name] in [0.5, 0.0]):
                                results[row[0].replace(" ", "_") + "_FALSE_POSITIVE"] += 1
                        elif(row[1].__contains__("failure")):
                            results[row[0].replace(" ", "_") + "_FAIL"] += 1
                            if(student_grades[student_name] in [0.5, 0.0]):
                                results[row[0].replace(" ", "_") + "_TRUE_NEGATIVE"] += 1
                            elif(student_grades[student_name] == 1.0):
                                results[row[0].replace(" ", "_") + "_FALSE_NEGATIVE"] += 1
                        elif(row[1].__contains__("error")):
                            results[row[0].replace(" ", "_") + "_ERROR"] += 1
                        elif(row[1].__contains__("skip")):
                            results[row[0].replace(" ", "_") + "_SKIP"] += 1
                        else:
                            print(colored("Unknown test result " + str(row), "yellow"))
    return results

def write_to_csv(results):
    with open(os.path.join(folder, "results.csv"), mode='a') as output_file: # write test results to csv
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
        for key in results:
            writer.writerow([os.path.basename(subfolder), key, results[key]])