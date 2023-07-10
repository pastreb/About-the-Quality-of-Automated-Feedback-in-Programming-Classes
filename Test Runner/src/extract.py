import csv
import json
import os
import random
import re  # regex
import shutil  # moving files through directories
import string
from termcolor import colored  # for printing funny colored text
from typing import Dict
from unittest import TestLoader, TestSuite
import threading
from importlib.machinery import SourceFileLoader
import bookkeeping
import main_exec
from test_runner.tap_test_runner import TapTestRunner
from pathlib import Path


def check_directory_exists(directory: str) -> None:
    """
    Check if the given directory exists. If not, raise an exception.

    Args:
        directory (str): The directory to check.
    Raises:
        FileNotFoundError: If the directory does not exist.
    """
    if not os.path.exists(directory):
        raise FileNotFoundError(f"Directory '{directory}' does not exist.")


def clear_directory(directory: str) -> None:
    """
    Clear the given directory by removing all its contents.

    Args:
        directory (str): The directory to clear.
    Raises:
        PermissionError: If there is an issue deleting the directory.
    """
    try:
        shutil.rmtree(directory)
    except (FileNotFoundError, PermissionError) as e:
        raise PermissionError(f"Failed to delete directory '{directory}': {e}")


def setup_and_prepare_directories(clear_target_directory: bool = True) -> None:
    """
    Set up the target directory and prepare the files for processing.

    Expects that `bookkeeping.SOURCE_DIRECTORY` is set to an existing path (the location is supposed to contain
    CodeExpert project exports).

    Creates `bookkeeping.TARGET_DIRECTORY`. If `clear_target_directory` is set to True (default) and
    `bookkeeping.TARGET_DIRECTORY` already exists, then `bookkeeping.TARGET_DIRECTORY` is wiped.

    Renames all projects in `bookkeeping.SOURCE_DIRECTORY` that are named after some eduID- or LTI-account to the actual
    student code (if possible). Propagates this renaming to Scoreboard files in `bookkeeping.SOURCE_DIRECTORY` (if necessary).

    Args:
        clear_target_directory (bool, optional): Whether to clear the target directory if it already exists. Defaults to True.

    Raises:
        FileNotFoundError: If the source directory does not exist.
        PermissionError: If there is an issue deleting the target directory.
    """

    # Activate colored print on Windows systems
    if os.name == "nt":
        os.system("color")

    check_directory_exists(bookkeeping.SOURCE_DIRECTORY)

    if os.path.exists(bookkeeping.TARGET_DIRECTORY) and clear_target_directory:
        clear_directory(bookkeeping.TARGET_DIRECTORY)

    os.makedirs(bookkeeping.TARGET_DIRECTORY, exist_ok=True)

    # Try to rename projects that are named after some eduID- or LTI-account
    id_to_student_code = rename_projects()

    # Propagate changes to Scoreboard files and clean them up
    update_scoreboard_files(id_to_student_code)


def rename_projects() -> Dict[str, str]:
    """
    Renames all projects in `bookkeeping.SOURCE_DIRECTORY` that are named after some eduID- or LTI-account to the actual
    student code (if possible).

    Returns:
        dict: A dictionary that maps usernames of eduID- or LTI-accounts to the corresponding student codes.

    """

    id_to_student_code: Dict[str, str] = {}
    # Iterate through all the directories in bookkeeping.SOURCE_DIRECTORY
    for project in os.listdir(bookkeeping.SOURCE_DIRECTORY):
        project_path = os.path.join(bookkeeping.SOURCE_DIRECTORY, project)
        if os.path.isdir(project_path):
            # Iterate through all the submissions in the project directory
            for submission in os.listdir(project_path):
                submission_path = os.path.join(project_path, submission)
                # Check if the submission directory contains "eduID" or "LTI"
                if os.path.isdir(submission_path) and (
                    "eduID" in submission or "LTI" in submission
                ):
                    # Iterate through all the files in the submission directory
                    for root, _, files in os.walk(submission_path):
                        for file in files:
                            # Look for the "details.json" file in the submission directory
                            if "details.json" in file:
                                # Read the data from the "details.json" file
                                with open(
                                    os.path.join(submission_path, root, file)
                                ) as student_details:
                                    data = json.load(student_details)
                                    # Extract the student code from the email
                                    student_code = re.findall(".*\@", data["email"])[0][
                                        :-1
                                    ]
                                    # Check if the username was already encountered
                                    if data["username"] not in id_to_student_code:
                                        # Add the username and the corresponding student code to the dictionary
                                        id_to_student_code[
                                            data["username"]
                                        ] = student_code
                                    else:
                                        # Check if the new student code matches the previously encountered student code
                                        if (
                                            id_to_student_code[data["username"]]
                                            != student_code
                                        ):
                                            print(
                                                colored(
                                                    f"Same ID {data['username']} for different students {id_to_student_code[data['username']]} and {student_code}",
                                                    "yellow",
                                                )
                                            )
                                    # Generate the new path for the submission directory
                                    new_submission_path = os.path.join(
                                        bookkeeping.SOURCE_DIRECTORY,
                                        project,
                                        submission.replace(
                                            data["username"], student_code
                                        ),
                                    )
                    try:
                        # Rename the submission directory to the new path
                        shutil.copytree(submission_path, new_submission_path)
                        shutil.rmtree(submission_path)
                        print(
                            colored(
                                f"Successfully renamed {submission_path} to {new_submission_path}",
                                "green",
                            )
                        )
                    except Exception as e:
                        print(
                            colored(
                                f"Couldn't rename {submission_path} to {new_submission_path}\n{type(e)}\n{e.args}\n{e}",
                                "yellow",
                            )
                        )
    return id_to_student_code


def update_scoreboard_files(id_to_student_code: Dict[str, str]) -> None:
    """
    Propagates this renaming to Scoreboard files in `bookkeeping.SOURCE_DIRECTORY` (if necessary).

    Args:
        id_to_student_code (Dict[str, str]): A dictionary that maps usernames of eduID- or LTI-accounts to the corresponding student codes.
    """

    # Loop over all files in the directory
    for scoreboard_file in os.listdir(bookkeeping.SOURCE_DIRECTORY):
        # Check if the file name contains "Scoreboard" and ends with ".csv"
        if "Scoreboard" in scoreboard_file and scoreboard_file.endswith(".csv"):
            # Get the path of the scoreboard file and the path of the new scoreboard file
            scoreboard_path = os.path.join(
                bookkeeping.SOURCE_DIRECTORY, scoreboard_file
            )
            new_scoreboard_path = os.path.join(
                bookkeeping.SOURCE_DIRECTORY,
                scoreboard_file.replace(".csv", "_new.csv"),
            )
            # Create a dictionary to store the data
            scoreboard_data: Dict[str, str] = {}
            # Open the original CSV file for reading and the new CSV file for writing
            with open(scoreboard_path, mode="r") as scoreboard:  # read content from CSV
                with open(
                    new_scoreboard_path, mode="w"
                ) as new_scoreboard:  # write content to CSV
                    # Create a CSV writer for the new file
                    writer = csv.writer(
                        new_scoreboard,
                        delimiter=",",
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL,
                        lineterminator="\n",
                    )
                    # Create a CSV reader for the old file
                    reader = csv.reader(
                        scoreboard,
                        delimiter=",",
                        quotechar='"',
                        quoting=csv.QUOTE_MINIMAL,
                        lineterminator="\n",
                    )
                    # Find index for the username column
                    header = next(reader)
                    try:
                        name_index = header.index("Username")
                    except:
                        # Try to use ';' for the delimiter instead of ';'
                        reader = csv.reader(
                            scoreboard,
                            delimiter=";",
                            quotechar='"',
                            quoting=csv.QUOTE_MINIMAL,
                            lineterminator="\n",
                        )
                        header = header[0].split(";")
                        name_index = header.index("Username")
                    # Write header row
                    writer.writerow(header)
                    # Loop over each row in the original CSV file
                    for row in reader:
                        # Change name from eduID/LTI to actual student code if possible
                        if (
                            "eduID" in row[name_index] or "LTI" in row[name_index]
                        ) and row[name_index] in id_to_student_code:
                            row[name_index] = id_to_student_code[row[name_index]]
                        # Add the row to the scoreboard data dictionary if the username is not already in the dictionary
                        if row[name_index] not in scoreboard_data:
                            scoreboard_data[row[name_index]] = row
                        else:
                            # If the username is already in the dictionary, merge the rows
                            old_row = scoreboard_data[row[name_index]]
                            for i in range(len(old_row)):
                                if i != name_index and len(row[i]) != 0:
                                    if len(old_row[i]) == 0:
                                        old_row[i] = row[i]
                                    elif old_row[i] != row[i]:
                                        print(
                                            colored(
                                                f"Duplicated data for {header[i]} in {scoreboard_file}: {old_row[i]} vs. {row[i]}",
                                                "yellow",
                                            )
                                        )
                            # Update the scoreboard data dictionary with the merged row
                            scoreboard_data[row[name_index]] = old_row
                    # Write the merged rows to the new CSV file
                    for person in scoreboard_data:
                        writer.writerow(scoreboard_data[person])
            # Replace the original file with the new file if the modification is successful
            try:
                os.remove(scoreboard_path)
                shutil.move(new_scoreboard_path, scoreboard_path)
                pass
            except Exception as e:
                print(
                    colored(
                        f"Couldn't replace {scoreboard_path} with {new_scoreboard_path}\n{type(e)}\n{e.args}\n{e}",
                        "yellow",
                    )
                )


# Define a global variable to store mappings from student codes to gibberish strings
student_code_to_gibberish: Dict[str, str] = {}


def __get_gibberish_string_for_student(student_code: str, len: int = 6) -> str:
    """
    Given a student code (i.e. ETH-Kuerzel), anonymizes it by generating a new random
    gibberish string of length `len` (default 6) the first time the code is encountered.
    On subsequent encounters, returns the previously generated gibberish string.

    Args:
        student_code (str): The student code to anonymize.
        len (int, optional): The length of the gibberish string to generate (default 6).

    Returns:
        str: The anonymized student code as a gibberish string.
    """

    if student_code not in student_code_to_gibberish.keys():
        # Generate a new gibberish string
        gibberish = "".join(random.choice(string.ascii_lowercase) for _ in range(len))
        while gibberish in student_code_to_gibberish.values():
            gibberish = "".join(random.choice(string.ascii_letters) for _ in range(len))
        student_code_to_gibberish[student_code] = gibberish
    return student_code_to_gibberish[student_code]


def __get_scores_for_export(project_name: str) -> Dict[str, list]:
    """
    Finds the Scoreboard-file in bookkeeping.SOURCE_DIRECTORY corresponding to the given `project_name`.
    Returns a dictionary with entries of the form (anonymized student, [presentation score, exam result])
    (e.g. ("abcdef", [1.0, 0.42])).

    Args:
        project_name (str): The name of the project to retrieve scores for.

    Returns:
        Dict[str, list]: A dictionary mapping anonymized student codes to their corresponding scores.
    """

    # Extract course prefix, year, and module number from the project name
    course_prefix = re.findall(
        str(bookkeeping.COURSE_PREFIXES).replace(", ", "|").replace("'", "")[1:-1],
        project_name,
    )
    year = re.findall(
        str(bookkeeping.YEARS).replace(", ", "|").replace("'", "")[1:-1], project_name
    )
    module_number = re.findall("M_\d", project_name)
    # Check that all required components are present
    if not (course_prefix and year and module_number):
        exit(
            colored(f"Could not find Scoreboard file for project {project_name}", "red")
        )
    # Unpack regex results
    course_prefix = course_prefix[0]
    year = year[0]
    module_number = module_number[0][2]
    # Construct path to scoreboard file
    scoreboard_file = os.path.join(
        bookkeeping.SOURCE_DIRECTORY,
        course_prefix + "_" + year + "_" + "Scoreboard.csv",
    )
    # Read scores from CSV file
    scores = {}
    with open(scoreboard_file, mode="r") as scoreboard:
        # Create a CSV reader for the scoreboard file
        reader = csv.reader(
            scoreboard,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
            lineterminator="\n",
        )
        # Find indices for the username and score columns
        header = next(reader)
        if (
            "Username" not in header
            or f"Modul {module_number}" not in header
            or "Exam" not in header
        ):
            print(colored(f"Corrupted Scoreboard CSV header\n{header}"), "red")
            return {}
        name_index = header.index("Username")
        presentation_index = header.index(f"Modul {module_number}")
        exam_index = header.index("Exam")
        for row in reader:
            # Extract score
            presentation_score = re.findall("1|0\.5|0", row[presentation_index])
            exam_score = re.findall("\d*\.\d*", row[exam_index])
            # Unpack regex results
            presentation_score = (
                float(presentation_score[0]) if presentation_score else 0.0
            )
            exam_score = float(exam_score[0]) if exam_score else 0.0
            anonymized_student_code = __get_gibberish_string_for_student(
                row[name_index]
            )
            scores[anonymized_student_code] = [presentation_score, exam_score]
    return scores


def __find_student_code(path_to_student_project: str) -> str:
    """
    Extracts student code (i.e. ETH-Kuerzel) either from the given `path_to_student_project`
    or from `details.json` located somewhere within that directory.

    Args:
        path_to_student_project (str): The path to the project folder in a submission of a student.

    Returns:
        str: The student code, if found. An empty string otherwise.
    """

    # Extract the parts of the path that contain the student code
    # The regex matches "/submission" or "/regrade" in the path and captures the preceding directory as the student code.
    student_code_with_surroundings = re.findall(
        "(?:/[^/]+/submission|/[^/]+/regrade)",
        path_to_student_project.replace("\\", "/"),
    )
    # If you want to have an 'or' match without having the split into match groups just add a '?:' to the beginning of the 'or' match.
    # https://stackoverflow.com/questions/24593824/why-does-re-findall-return-a-list-of-tuples-when-my-pattern-only-contains-one-gr
    # Also note that path.replace("\\", "/") simplifies our regexes as we have to escape less stuff.
    if not student_code_with_surroundings:
        # No match found
        return ""
    if "LTI" in student_code_with_surroundings:
        # In some cases, the folder is named after the LTI account that the student used (e.g. exam environment).
        # In such cases, we need a different way to find the student code.
        parent_dir = os.path.join(path_to_student_project, "..")
        for file_name in os.listdir(parent_dir):
            if file_name.startswith("details") and file_name.endswith(".json"):
                # If a file named details.json is found in the parent directory, extract the student code from it
                with open(os.path.join(parent_dir, file_name)) as student_details:
                    data = json.load(student_details)
                    # Extract the student code from the email
                    student_code = re.findall(".*\@", data["email"])[0][:-1]
                    return student_code
        # No details.json file found
        return ""
    else:
        student_code = re.findall("[^/]+", student_code_with_surroundings[0])
        if not student_code:
            # No match found
            return ""
    return student_code[0]


def copy_main_file(src, dest):
    try:
        # Copy and rename main.py
        shutil.copy(src, dest)
    except Exception as e:
        print(
            colored(
                f"Couldn't copy {src} to {dest}\n{type(e)}\n{e.args}\n{e}", "yellow"
            )
        )


def read_existing_audit_file(audit_file):
    rows = []
    if os.path.isfile(audit_file):
        with open(audit_file, mode="r") as source_csv:
            # Create a CSV reader for the source audit file
            reader = csv.reader(
                source_csv,
                delimiter=",",
                quotechar='"',
                quoting=csv.QUOTE_MINIMAL,
                lineterminator="\n",
            )
            for row in reader:
                if (len(row)) != 0:
                    rows.append(["Original"] + row)
    return rows


def handle_audit_file(
    path_to_main: str,
    all_test_cases: list,
    dest: str,
    student_scores: list,
    project_student_info: str,
    run_tests: bool,
):
    # (Possibly) create audit folder
    audit_folder = os.path.join(path_to_main, "cx_audit")
    if not os.path.isdir(audit_folder):
        os.mkdir(audit_folder)

    # (Possibly) read from existing audit file
    audit_file = os.path.join(audit_folder, "testcases.csv")
    rows = read_existing_audit_file(audit_file)
    audit_file_exists = len(rows) > 0
    if not audit_file_exists:
        print(
            colored(
                f"Did not find existing audit file for {project_student_info}", "yellow"
            )
        )

    if run_tests:
        lock = threading.Lock()
        for test_cases in all_test_cases:
            thread = TestCaseRunner(
                lock, test_cases[0], test_cases[1], path_to_main, project_student_info
            )
            print(
                colored(
                    f"About to run {test_cases[1]} on {project_student_info}", "blue"
                )
            )
            thread.start()
            thread.join()
            print(
                colored(
                    f"Successfully executed {test_cases[1]} on {project_student_info}\n {thread.rows}",
                    "green",
                )
            )
            rows += thread.rows

    # Write to new audit file
    with open(dest, mode="a") as target_csv:
        # Create a CSV writer for the new audit file
        writer = csv.writer(
            target_csv,
            delimiter=",",
            quotechar='"',
            quoting=csv.QUOTE_MINIMAL,
            lineterminator="\n",
        )
        writer.writerow(["Presentation Score", str(student_scores[0])])
        writer.writerow(["Exam Result", str(student_scores[1])])
        for row in rows:
            test_number = int(re.findall("\d+", row[1])[0])
            test_number = f"0{test_number}" if test_number < 10 else f"{test_number}"
            writer.writerow(
                [
                    row[0],
                    f"Test {test_number}",
                    "Success"
                    if "success" in row[2]
                    else "Fail"
                    if "fail" in row[2]
                    else "Error",
                ]
            )
    return audit_file_exists


def extract_project(project_name: str, run_tests: bool) -> None:
    """
    Extracts relevant files (testcases.csv from cx_audit and main.py) and anonymizes them from the
    given [code]expert project export (of one task) if found in `bookkeeping.SOURCE_DIRECTORY`,
    and copies them to `bookkeeping.TARGET_DIRECTORY`.
    This function also includes information about the score of the student.

    Args:
        project_name (str): Name of the project to extract

    Returns:
        None: The function only extracts the project.
    """

    # Setup paths
    source_path = os.path.join(bookkeeping.SOURCE_DIRECTORY, project_name)
    target_path = os.path.join(bookkeeping.TARGET_DIRECTORY, project_name)
    # Check if project exists in source directory
    if not os.path.exists(source_path):
        print(colored(f"Could not find project export at {source_path}", "red"))
        return
    # Check if project is already exported
    if os.path.exists(target_path):
        print(colored("Project already exported, consider deleting it", "yellow"))
        return
    # Create target directory if it doesn't exist
    os.mkdir(target_path)

    # Get scores
    scores = __get_scores_for_export(project_name)

    # Get test cases
    all_test_cases = []
    for file in os.listdir(bookkeeping.TEST_CASES_DIRECTORY):
        if project_name in file:
            all_test_cases.append(
                [
                    SourceFileLoader(
                        file.replace(".py", ""),
                        os.path.join(bookkeeping.TEST_CASES_DIRECTORY, file),
                    ).load_module(),
                    file.replace(".py", ""),
                ]
            )
    # Prepare bookkeeping
    n_students = 0
    n_existing_audit_files = 0
    # Traverse the source recursively
    for root, _, _ in os.walk(source_path):
        # Check if folder is named "project"
        if os.path.basename(root) != "project":
            continue
        n_students += 1
        # Find student code
        student_code = __find_student_code(root)
        if student_code == "":  # no match
            print(colored(f"Could not find student code in {root}", "red"))
            continue
        # Check if score is found in scores
        anonymized_student_code = __get_gibberish_string_for_student(student_code)
        if anonymized_student_code not in scores:
            print(
                colored(
                    f"Could not find score of student {student_code}, so I will skip this student",
                    "yellow",
                )
            )
            continue

        path_to_main = os.path.join(source_path, root)
        src = os.path.join(path_to_main, "main.py")
        dest = os.path.join(target_path, f"{anonymized_student_code}_main.py")
        copy_main_file(src, dest)

        dest = os.path.join(target_path, f"{anonymized_student_code}_testresults.csv")
        main_exec.path_to_main = (
            path_to_main  # make sure that test cases run on correct main file
        )
        n_existing_audit_files += handle_audit_file(
            path_to_main,
            all_test_cases,
            dest,
            scores[anonymized_student_code],
            f"{project_name} of {student_code}",
            run_tests,
        )

    # Print results
    print(
        colored(
            f"Successfully moved and renamed files from {n_students} students", "green"
        )
    )
    # Print info on number of found audit (test result) files
    if n_students * 0.95 <= n_existing_audit_files:
        print(
            colored(
                f"{str(n_existing_audit_files)}/{str(n_students)} existing audit file(s)",
                "green",
            )
        )  # at least 95% of audit files were already present
    elif n_existing_audit_files >= n_students / 2:
        print(
            colored(
                f"{str(n_existing_audit_files)}/{str(n_students)} existing audit file(s)",
                "yellow",
            )
        )
    else:
        print(
            colored(
                f"{str(n_existing_audit_files)}/{str(n_students)} existing audit file(s)",
                "red",
            )
        )


def extract_projects(
    include: list = [], exclude: list = [], run_tests: bool = True
) -> None:
    """
    Extracts projects from the bookkeeping.SOURCE_DIRECTORY.

    Args:
        include (list): A list of project names. If provided, only these projects will be extracted.
        exclude (list): A list of project names. Projects in this list will be excluded from the extraction.

    Returns:
        None: The function only extracts the projects.
    """

    # If include is not provided, extract all projects that are not in exclude
    if include == []:
        for project_name in os.listdir(bookkeeping.SOURCE_DIRECTORY):
            if project_name not in exclude and os.path.isdir(
                os.path.join(bookkeeping.SOURCE_DIRECTORY, project_name)
            ):
                print(f"Processing {project_name}")
                extract_project(project_name, run_tests)
                print()
    # If include is provided, extract only the projects in include
    else:
        for project_name in include:
            if os.path.isdir(os.path.join(bookkeeping.SOURCE_DIRECTORY, project_name)):
                print(f"Processing {project_name}")
                extract_project(project_name, run_tests)
                print()


class TestCaseRunner(threading.Thread):
    def __init__(
        self, lock, test_cases, test_cases_name, path_to_main, project_student_info
    ):
        threading.Thread.__init__(self)
        self.lock = lock
        self.test_cases = test_cases
        self.test_cases_name = test_cases_name
        self.path_to_main = path_to_main
        self.project_student_info = project_student_info
        self.rows = []
        self.result = 0.0

    def run(self):
        self.lock.acquire()
        try:
            self.rows, self.result = self.run_tests(
                self.test_cases, self.test_cases_name
            )
        except Exception as e:
            print(
                colored(
                    f"Encountered an Exception when running test cases {self.test_cases_name} for {self.project_student_info}:\n{type(e)}\n{e.args}\n{e}",
                    "red",
                )
            )
        self.lock.release()

    def run_tests(self, test_cases: list, test_cases_name: str) -> list:
        loaded_tests = TestLoader().loadTestsFromTestCase(test_cases.Tests)
        suite = TestSuite([loaded_tests])
        runner = TapTestRunner(
            output="./tmp", report_name="result", add_timestamp=False, verbosity=2
        )
        result = runner.run(suite)
        # 0 for success, 1 for failure, 2 for error and 3 for skip
        # example: to get outcome of test 0, type test_outcomes[0].outcome
        test_outcomes = list(result._get_info_by_testcase().values())[0]
        outcome_values = {0: "success", 1: "failure", 2: "error", 3: "skip"}
        rows = []
        for n in range(len(test_outcomes)):
            rows.append(
                [
                    test_cases_name,
                    "Test {}".format(n + 1),
                    "Result: {}".format(outcome_values[test_outcomes[n].outcome]),
                ]
            )
        # Uncomment the following if you want to see the test results in console:
        if "V4" in rows[0][0] and "error" in rows[0][2]:
            with open("./tmp/result.log") as file_handler:
                print(file_handler.read())
        # Cleanup
        shutil.rmtree("./tmp")
        return rows, (len(result.successes) / result.testsRun)
