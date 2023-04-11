import csv
import matplotlib.pyplot as plt
import os
import pandas as pd
import random
import re # regex
import shutil # moving files through directories
import string
from termcolor import colored # for printing funny colored text

student_code_to_gibberish = {} # maintains a unique random string for each student code

# Given a student code (aka ETH-Kuerzel) anonimizes it. 
# When the code is encountered for the first time, a new random gibberish string of size len is generated for it 
# and persisted in student_code_to_gibberish. 
# On each subsequent encounter of the same student code, the corresponding gibberish is simply returned.
def get_gibberish_string_for_student(student_code, len=6):
    if student_code not in student_code_to_gibberish.keys():
        gibberish = ''.join(random.choice(string.ascii_lowercase) for _ in range(len))
        while(gibberish in student_code_to_gibberish.values()):
            gibberish = ''.join(random.choice(string.ascii_letters) for _ in range(len))
        student_code_to_gibberish[student_code] = gibberish
    return student_code_to_gibberish[student_code]

# Given a [code]expert project source directory extracts and anonimizes the relevant files (testcases.csv from cx_audit and main.py) to the target directory.
def extract_project(source_directory, target_directory):
    n_students = 0
    n_existing_audit_files = 0
    for root, _, _ in os.walk(source_directory): # recursively traverse the source directory
        if os.path.basename(root) == "project": # the folders we are interested in are called "project"
            n_students += 1
            root = root.replace("\\", "/") # prepare root for regex action
            student_code = re.findall("[^/]+", re.findall("(?:/[^/]+/submission|/[^/]+/regrade)", root)[0])[0] # extract student code (aka ETH-Kuerzel) from path
            # If you want to have an 'or' match without having the split into match groups just add a '?:' to the beginning of the 'or' match.
            # https://stackoverflow.com/questions/24593824/why-does-re-findall-return-a-list-of-tuples-when-my-pattern-only-contains-one-gr
            if len(student_code) == 0: # no match
                print(colored("Could not find student code in " + root, "red"))
            # Find and move main file:
            src = os.path.join(source_directory, root, "main.py")
            dest = os.path.join(target_directory, get_gibberish_string_for_student(student_code) + "_main.py") # anonymize
            # print("Moving", src, "to", dest) # uncomment for verbose output
            shutil.copy(src, dest) # copy and rename main.py
            # Find and move audit file:
            src = os.path.join(source_directory, root, "cx_audit", "testcases.csv")
            if os.path.isfile(src): # audit file exists
                n_existing_audit_files += 1
                dest = os.path.join(target_directory, get_gibberish_string_for_student(student_code) + "_testcases.csv") # anonymize
                # print("Moving", src, "to", dest) # uncomment for verbose output
                shutil.copy(src, dest) # copy and rename testcases.csv
    print("Successfully moved and renamed files from", n_students, "students", end=' ')
    if n_students == n_existing_audit_files: # print info on number of found audit files
        print(colored(str(n_existing_audit_files) + "/" + str(n_students) + " audit file(s)", "green"))
    elif n_existing_audit_files >= n_students/2:
        print(colored(str(n_existing_audit_files) + "/" + str(n_students) + " audit file(s)", "yellow"))
    else:
        print(colored(str(n_existing_audit_files) + "/" + str(n_students) + " audit file(s)", "red"))

# Given a [code]expert project and a path to a scoreboard file containing the grades of students extracts (and returns) 
# the grades of the students for the module presentation belonging to the project.
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
                    student_grades_for_modul[get_gibberish_string_for_student(row[name_index])] = float(grade[0]) # anonymize
                else:
                    student_grades_for_modul[get_gibberish_string_for_student(row[name_index])] = -1 # encode everything non-graded as -1.0
    return student_grades_for_modul

def get_n_test_cases(test_results_csv):
    with open(test_results_csv, mode='r') as test_results: # read content from csv
        row_count = 0
        for _ in csv.reader(test_results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL):
            row_count += 1
    return row_count

# Given a cleaned-up [code]expert project and the grades of students for the module presentation belonging to the project 
# extracts the info from audit-files and writes them to a csv.
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
                    print(colored("Could not find grade of student " + student_name + ", so I will skip this student", "yellow"))
                    continue
                src = os.path.join(project_directory, file)
                with open(src, mode='r') as test_results: # read content from csv
                    n_rows = 0
                    for row in csv.reader(test_results, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL):
                        n_rows += 1
                        if(row[1].__contains__("success")):
                            results[row[0].replace(" ", "_") + "_SUCCESS"] += 1
                            if(student_grades[student_name] == 1.0):
                                results[row[0].replace(" ", "_") + "_TRUE_POSITIVE"] += 1
                            elif(student_grades[student_name] in [0.5, 0.0]):
                                results[row[0].replace(" ", "_") + "_FALSE_POSITIVE"] += 1
                            # The grade may also be -1.0, which means that the student missed the appointment
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
                    if(n_rows == 0):
                        print(colored("No entries in " + src, "yellow"))
                        n_test_cases = len(results) // 8
                        if(n_test_cases == 0):
                            print(colored("Couldn't capture the results as SKIP either, as I don't know (yet) how many test cases this project has", "red"))
                        else:
                            for i in range(n_test_cases):
                                results["Test_" + str(i+1) + "_SKIP"] += 1
    # Write test results to csv:
    with open(os.path.join(project_directory, "results.csv"), mode='a') as output_file:
        writer = csv.writer(output_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator = '\n')
        for key in results:
            writer.writerow([os.path.basename(project_directory), key, results[key]])
    # Generate Plot:
    project_test_cases_data = []
    for i in range(len(results) // 8):
        test_case_data = ["Test " + str(i+1),
                            results["Test_" + str(i+1) + "_TRUE_POSITIVE"], 
                            results["Test_" + str(i+1) + "_FALSE_POSITIVE"],
                            results["Test_" + str(i+1) + "_TRUE_NEGATIVE"],
                            results["Test_" + str(i+1) + "_FALSE_NEGATIVE"],
                            results["Test_" + str(i+1) + "_ERROR"]]
        test_case_data.append(sum(test_case_data[1:]))
        print(test_case_data)
        project_test_cases_data.append(test_case_data)
    make_bar_plot_for_single_project(os.path.basename(project_directory), project_test_cases_data)
    return results

# Given a project title and the extracted test cases data creates a simple bar plot.
def make_bar_plot_for_single_project(project_title, project_test_cases_data):
    # project_test_cases_data should be structured as follows:
    # [[test_name, n_true_positives, n_false_positives, n_true_negatives, n_false_negatives, n_errors, total], [...], ...]
    plotdata = pd.DataFrame({
        "True Positives": [test[1]/test[6] for test in project_test_cases_data],
        "False Positives": [test[2]/test[6] for test in project_test_cases_data],
        "True Negatives": [test[3]/test[6] for test in project_test_cases_data],
        "False Negatives": [test[4]/test[6] for test in project_test_cases_data],
        "Errors": [test[5]/test[6] for test in project_test_cases_data]
    }, index=[test[0] for test in project_test_cases_data])
    green = (0.173, 0.627, 0.173)
    red = (0.839, 0.153, 0.157)
    blue = (0.122, 0.467, 0.706)
    orange = (1.000, 0.498, 0.055)
    black = (0.750, 0.750, 0.750)
    my_colors = [green, red, orange, blue, black]
    print(plotdata)
    plotdata.plot(kind="bar", figsize=(15, 8), color=my_colors)
    plt.title(project_title)
    plt.xlabel("Test-Cases")
    plt.ylabel("% of students")
    plt.ylim([0, 1])
    plt.yticks([0.1 * x for x in range(11)])
    plt.show()