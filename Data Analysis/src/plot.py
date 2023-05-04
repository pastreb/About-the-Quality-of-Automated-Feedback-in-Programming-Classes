import csv
import os
import re

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt

from termcolor import colored # for printing funny colored text

import bookkeeping
import test_info as ti

# TODO: Document this

GREEN = (0.173, 0.627, 0.173)
RED = (0.839, 0.153, 0.157)
BLUE = (0.122, 0.467, 0.706)
ORANGE = (1.000, 0.498, 0.055)
BLACK = (0.750, 0.750, 0.750)

PURPLE = (0.667, 0.263, 0.443)
NEON = (0.800, 1.000, 0.000)
BROWN = (0.918, 0.714, 0.306)

# Cache
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
    # Cache
    read_csvs[file_name] = data_frame
    return data_frame



def __get_project_data(project_names : list, csv_file_name : str, relative_ratios : bool = True, include_fixed_main_exec : bool = False):
    # Read CSV file into DataFrame
    data_frame = __read_csv(csv_file_name)
    if not include_fixed_main_exec:
        # Remove fixed_main_exec
        data_frame = data_frame[~data_frame["Test"].str.contains("fixed_main_exec")]
    else:
        # Rename fixed_main_exec
        data_frame["Test"] = data_frame["Test"].str.replace("fixed_main_exec", "fme")
    data_frame = data_frame.loc[data_frame["Project"].isin(project_names)]
    # Change absolute counts to relative ratios (if specified so)
    if relative_ratios:
        for col in (ti.CSV_PS_COUNTS + ti.CSV_ER_COUNTS):
            data_frame[col] = data_frame[col]/data_frame["Submissions"]
    return data_frame



def __clean_project_name(project_name):
    regex = (str(bookkeeping.COURSE_PERFIXES) + "_" + str(bookkeeping.YEARS)).replace("[", "(?:").replace("]", ")").replace(", ", "|").replace("'", "") + "_M_\d*_[A|SA]_\d*"
    cleaned_project_name = re.findall(regex, project_name)
    return cleaned_project_name[0] if len(cleaned_project_name) == 1 else project_name


def plot_project(project_name : str, csv_file_name : str, score_metric : ti.Score_Metric, relative_ratios : bool = True, include_fixed_main_exec : bool = False) -> None:
    # Get data
    data = __get_project_data([project_name], csv_file_name, relative_ratios, include_fixed_main_exec)
    data = data.sort_values("Test")
    data = data.set_index("Test")
    # Get data into shape for first plot (with counts, e.g. "True Positives")
    count_data = data[ti.CSV_PS_COUNTS] if score_metric == ti.Score_Metric.PRESENTATION else data[ti.CSV_ER_COUNTS] if score_metric == ti.Score_Metric.EXAM else data
    for col in count_data.columns.values:
        count_data = count_data.rename(columns={col : col.replace(" (Presentation Score)", "").replace(" (Exam Result)", "")})
    # Prepare first plot name
    score_metric_string = "_Presentation" if score_metric == ti.Score_Metric.PRESENTATION else "_Exam" if score_metric == ti.Score_Metric.EXAM else ""
    ratio_type_string = "_Relative" if relative_ratios else "_Absolute"
    fm_string = "_with_fixed_main_exec" if include_fixed_main_exec else ""
    plot_name = f"{__clean_project_name(project_name)}_Plot_Counts{score_metric_string}{ratio_type_string}{fm_string}"
    # First plot    
    __plot_tests_vs_students(count_data, project_name, [GREEN, RED, ORANGE, BLUE, BLACK], plot_name)
    # Get data into shape for first plot (with scores, e.g. "Accuracy")
    score_data = data[ti.CSV_PS_SCORES] if score_metric == ti.Score_Metric.PRESENTATION else data[ti.CSV_ER_SCORES] if score_metric == ti.Score_Metric.EXAM else data
    for col in score_data.columns.values:
        score_data = score_data.rename(columns={col : col.replace(" (Presentation Score)", "").replace(" (Exam Result)", "")})
    # Second plot
    plot_name = f"{__clean_project_name(project_name)}_Plot_Scores{score_metric_string}{ratio_type_string}{fm_string}"
    __plot_tests_vs_students(score_data, project_name, [PURPLE, NEON, BROWN], plot_name)



def plot_projects_against_each_other(project_1_name : str, project_2_name : str, csv_file_name : str, score_metric : ti.Score_Metric, relative_ratios : bool = True) -> None:
    # Get data
    data = __get_project_data([project_1_name, project_2_name], csv_file_name, relative_ratios)
    data = data.sort_values("Test")
    data["Project"] = data["Project"].apply(__clean_project_name)
    data = data.set_index(["Project", "Test"])
    # Get data into shape for first plot (with counts, e.g. "True Positives")
    count_data = data[ti.CSV_PS_COUNTS] if score_metric == ti.Score_Metric.PRESENTATION else data[ti.CSV_ER_COUNTS] if score_metric == ti.Score_Metric.EXAM else data
    for col in count_data.columns.values:
        count_data = count_data.rename(columns={col : col.replace(" (Presentation Score)", "").replace(" (Exam Result)", "")})
    # Prepare plot_name
    score_metric_string = "_Presentation" if score_metric == ti.Score_Metric.PRESENTATION else "_Exam" if score_metric == ti.Score_Metric.EXAM else ""
    ratio_type_string = "_Relative" if relative_ratios else "_Absolute"
    plot_name = f"{__clean_project_name(project_1_name)}_vs_{__clean_project_name(project_2_name)}_Plot_Counts{score_metric_string}{ratio_type_string}"
    # First plot
    __plot_tests_vs_students(count_data, f"{project_1_name} vs {project_2_name}", [GREEN, RED, ORANGE, BLUE, BLACK], plot_name)
    # Get data into shape for first plot (with scores, e.g. "Accuracy")
    score_data = data[ti.CSV_PS_SCORES] if score_metric == ti.Score_Metric.PRESENTATION else data[ti.CSV_ER_SCORES] if score_metric == ti.Score_Metric.EXAM else data
    for col in score_data.columns.values:
        score_data = score_data.rename(columns={col : col.replace(" (Presentation Score)", "").replace(" (Exam Result)", "")})
    # Second plot
    plot_name = f"{__clean_project_name(project_1_name)}_vs_{__clean_project_name(project_2_name)}_Plot_Sounts{score_metric_string}{ratio_type_string}"
    __plot_tests_vs_students(count_data, f"{project_1_name} vs {project_2_name}", [GREEN, RED, ORANGE, BLUE, BLACK], plot_name)



def plot_module(module : list, module_name : str, csv_file_name : str, score_metric : ti.Score_Metric, relative_ratios : bool = True) -> None:
    # Get data
    data = __get_project_data(module, csv_file_name, relative_ratios)
    # Get data into shape for plot
    data = data[ti.CSV_PS_COUNTS + ti.CSV_PS_SCORES] if score_metric == ti.Score_Metric.PRESENTATION else data[ti.CSV_ER_COUNTS + ti.CSV_ER_SCORES] if score_metric == ti.Score_Metric.EXAM else data
    for col in data.columns.values:
        data = data.rename(columns={col : col.replace(" (Presentation Score)", "").replace(" (Exam Result)", "")})
    data = data.mean()
    # Prepare plot_name
    score_metric_string = "_Presentation" if score_metric == ti.Score_Metric.PRESENTATION else "_Exam" if score_metric == ti.Score_Metric.EXAM else ""
    ratio_type_string = "_Relative" if relative_ratios else "_Absolute"
    plot_name = f"{module_name}_Plot{score_metric_string}{ratio_type_string}"
    # Plot
    __plot_tests_vs_students(data, module_name, [GREEN, RED, ORANGE, BLUE, BLACK, PURPLE, NEON, BROWN], plot_name)



def __plot_tests_vs_students(data, title, colors, name):
    data.plot(kind="bar", figsize=(16, 16), rot=45, color=colors)
    plt.title(title)
    plt.xlabel("Test-Cases")
    plt.ylabel("% of students")
    plt.ylim([0, 1])
    plt.yticks([0.1 * x for x in range(11)])
    plt.savefig(os.path.join(bookkeeping.TARGET_DIRECTORY, f"{name}.svg"), format="svg")
    plt.savefig(os.path.join(bookkeeping.TARGET_DIRECTORY, f"{name}.png"), format="png")
    print(colored(f"Successfully created score plot {name}", "green"))
    plt.cla()