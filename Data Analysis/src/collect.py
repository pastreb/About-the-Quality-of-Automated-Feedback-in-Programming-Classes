import csv
import os
import shutil

from termcolor import colored # for printing funny colored text

import bookkeeping
import test_info


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
    check_directory_exists(bookkeeping.TARGET_DIRECTORY)


def one_csv_to_rule_them_all() -> str:

    """
    Combines data from multiple CSV files in bookkeeping.TARGET_DIRECTORY into a single output file.

    Returns:
        A string representing the path to the output file.
    """

    # Create an empty list to store the rows from all CSV files
    all_rows = [test_info.CSV_HEADER]
    # Loop through all exported projects
    print("I will now collect the project data from the CSV files")
    for project in os.listdir(bookkeeping.TARGET_DIRECTORY):
        project_path = os.path.join(bookkeeping.TARGET_DIRECTORY, project)
        # Check if actually is a project
        if not project.endswith(".zip"):
            continue
        project = project.replace(".zip", "")
        new_project_path = os.path.join(bookkeeping.TARGET_DIRECTORY, project)
        if os.path.exists(new_project_path):
            print(colored("Path already exists, which should not have happened: {new_project_path}", "red"))
            continue
        shutil.unpack_archive(project_path, new_project_path,"zip")
        if not os.path.isdir(new_project_path):
            shutil.rmtree(new_project_path)
            continue
        project_test_info = test_info.ProjectTestInfo(project)
        # Loop through all files in the projects
        for file in os.listdir(new_project_path):
            # Check if the file is a CSV file
            if not file.endswith(".csv"):
                continue
            # Define the path to the CSV file
            file_path = os.path.join(new_project_path, file)
            rows = []
            # Open the CSV file and read the rows
            with open(file_path, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    rows.append(row)
            # Add the rows to the project test info
            project_test_info.add_submission(rows)
        shutil.rmtree(new_project_path)
        # Finalize the project test info and add the rows to the all_rows list
        for row in project_test_info.finalize():
            all_rows.append(row)
        print(colored(f"Done: {project}", "green"))
    # Define the output file path
    output_file = os.path.join(bookkeeping.TARGET_DIRECTORY, f"out.csv")
    if os.path.exists(output_file):
        try:
            # Delete the file
            os.remove(output_file)
        except Exception as e:
            exit(colored(f"Failed to delete file\n{type(e)}\n{e.args}\n{e}", "red"))
    # Write the combined rows to the output file
    with open(output_file, "w", newline="") as csv_file:
        writer = csv.writer(csv_file, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        writer.writerows(all_rows)
    # Print success message and return the output file path
    print(colored(f"Successfully combined information on {len(all_rows)-1} test cases from CSV files in {bookkeeping.TARGET_DIRECTORY} into {output_file}", "green"))
    return output_file