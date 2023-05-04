import csv
import os

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt

from termcolor import colored # for printing funny colored text

import bookkeeping
import test_info as ti

GREEN = (0.173, 0.627, 0.173)
RED = (0.839, 0.153, 0.157)
BLUE = (0.122, 0.467, 0.706)
ORANGE = (1.000, 0.498, 0.055)
BLACK = (0.750, 0.750, 0.750)

PURPLE = (0.667, 0.263, 0.443)
NEON = (0.800, 1.000, 0.000)
BROWN = (0.918, 0.714, 0.306)

read_csvs = {}

def __read_csv(file_name : str) -> pd.DataFrame:
    if(file_name in read_csvs):
        return read_csvs[file_name]
    # Get the path of the CSV file
    csv_path = os.path.join(bookkeeping.TARGET_DIRECTORY, file_name)
    if not os.path.isfile(csv_path):
        exit(colored(f"Could not find {csv_path} for plotting", "red"))
    # Read content from CSV directly into a DataFrame
    data_frame = pd.read_csv(csv_path)
    # Check header
    header = data_frame.columns.values
    if len(header) != len(ti.CSV_HEADER) or False in [(header[i] == ti.CSV_HEADER[i]) for i in range(len(header))]:
        exit(colored(f"CSV header seems to be corrupted:\n {header}\n vs.\n {ti.CSV_HEADER}", "red"))
    # Rename fixed_main_exec
    data_frame["Test"] = data_frame["Test"].str.replace("fixed_main_exec", "*")
    # Make/check MultiIndex
    data_frame.set_index(["Project", "Test"], inplace=True)
    if "Project" not in data_frame.index.names or "Test" not in data_frame.index.names:
        exit(colored(f"Unexpected MultiIndex found in CSV:\n {data_frame.index.names}", "red"))
    read_csvs[file_name] = data_frame
    return data_frame

def __get_project_data(project_name : str, csv_file_name : str, relative_ratios : bool = True):
    data = __read_csv(csv_file_name).loc[project_name]
    for col in data.columns.values:
        if relative_ratios and (col in ti.CSV_PS_COUNTS or col in ti.CSV_ER_COUNTS):
            data[col] = data[col]/data["Submissions"]
    return data

def __plot_project(project_name : str, csv_file_name : str, score_metric : ti.Score_Metric, relative_ratios : bool = True, include_fixed_main_exec : bool = False) -> None:
    data = __get_project_data(project_name, csv_file_name, relative_ratios)
    data.drop([test for test in data.index.values if ("fixed_main_exec" in test) or include_fixed_main_exec])
    # Prepare plot_name
    score_metric_string = "_presentation" if score_metric == ti.Score_Metric.PRESENTATION else "_exam" if score_metric == ti.Score_Metric.EXAM else ""
    ratio_type_string = "_relative" if relative_ratios else "_absolute"
    fm_string = "_with_fixed_main_exec" if include_fixed_main_exec else ""
    # First plot
    count_data = data[ti.CSV_PS_COUNTS] if score_metric == ti.Score_Metric.PRESENTATION else data[ti.CSV_ER_COUNTS] if score_metric == ti.Score_Metric.EXAM else data
    for col in count_data.columns.values:
        count_data = count_data.rename(columns={col : col.replace(" (Presentation Score)", "").replace(" (Exam Result)", "")})
    count_data = count_data.sort_index()
    plot_name = f"{project_name}_plot_counts{score_metric_string}{ratio_type_string}{fm_string}"
    __plot_tests_vs_students(count_data, project_name, [GREEN, RED, ORANGE, BLUE, BLACK], plot_name)
    # Second plot
    score_data = data[ti.CSV_PS_SCORES] if score_metric == ti.Score_Metric.PRESENTATION else data[ti.CSV_ER_SCORES] if score_metric == ti.Score_Metric.EXAM else data
    score_data = score_data.sort_index()
    plot_name = f"{project_name}_plot_scores{score_metric_string}{ratio_type_string}{fm_string}"
    __plot_tests_vs_students(score_data, project_name, [PURPLE, NEON, BROWN], plot_name)

def plot_projects_against_each_other(project_1_name : str, project_2_name : str, csv_file_name : str, score_metric : ti.Score_Metric, relative_ratios : bool = True, include_fixed_main_exec : bool = False) -> None:
    pass

def __plot_module(module_name : str, csv_file_name : str, score_metric : ti.Score_Metric, relative_ratios : bool = True, include_fixed_main_exec : bool = False) -> None:
    pass

def __plot_tests_vs_students(data, title, colors, name):
    data.plot(kind="bar", figsize=(15, 10), color=colors)
    plt.title(title)
    plt.xlabel("Test-Cases")
    plt.ylabel("% of students")
    plt.ylim([0, 1])
    plt.yticks([0.1 * x for x in range(11)])
    plt.savefig(os.path.join(bookkeeping.TARGET_DIRECTORY, f"{name}.eps"), format="eps")
    plt.savefig(os.path.join(bookkeeping.TARGET_DIRECTORY, f"{name}.png"), format="png")
    print(colored(f"Successfully created score plot {name}", "green"))
    plt.cla()