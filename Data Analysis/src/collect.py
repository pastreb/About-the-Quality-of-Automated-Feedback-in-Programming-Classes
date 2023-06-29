import csv
import os

from termcolor import colored # for printing funny colored text

import bookkeeping
import test_info


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
        if not os.path.isdir(project_path):
            continue
        project_test_info = test_info.ProjectTestInfo(project)
        # Loop through all files in the projects
        for file in os.listdir(project_path):
            # Check if the file is a CSV file
            if not file.endswith(".csv"):
                continue
            # Define the path to the CSV file
            file_path = os.path.join(project_path, file)
            rows = []
            # Open the CSV file and read the rows
            with open(file_path, "r") as csv_file:
                csv_reader = csv.reader(csv_file)
                for row in csv_reader:
                    rows.append(row)
            # Add the rows to the project test info
            project_test_info.add_submission(rows)
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