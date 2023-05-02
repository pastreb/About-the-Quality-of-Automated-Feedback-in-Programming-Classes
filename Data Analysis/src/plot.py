import csv
import os

import pandas as pd
import matplotlib.pyplot as plt

from termcolor import colored # for printing funny colored text

import bookkeeping
import test_info

GREEN = (0.173, 0.627, 0.173)
RED = (0.839, 0.153, 0.157)
BLUE = (0.122, 0.467, 0.706)
ORANGE = (1.000, 0.498, 0.055)
BLACK = (0.750, 0.750, 0.750)

PURPLE = (0.667, 0.263, 0.443)
NEON = (0.800, 1.000, 0.000)
BROWN = (0.918, 0.714, 0.306)


def __read_csv(file_name : str) -> list:
    # Get the path of the CSV file
    csv_path = os.path.join(bookkeeping.TARGET_DIRECTORY, file_name)
    if not os.path.isfile(csv_path):
        exit(colored(f"Could not find {csv_path} for plotting", "red"))
    with open(csv_path, mode='r') as scoreboard: # read content from csv
        # Create a CSV reader
        reader = csv.reader(scoreboard, delimiter=',', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
        # Check header
        header = next(reader)
        if len(header) == 1:
            # Try to use ';' for the delimiter instead of ';'
            reader = csv.reader(scoreboard, delimiter=';', quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator='\n')
            header = header[0].split(';')
        if len(header) != len(test_info.CSV_HEADER) or False in [(header[i] == test_info.CSV_HEADER[i]) for i in range(len(header))]:
            exit(colored(f"CSV header seems to be corrupted {header} vs. {test_info.CSV_HEADER}", "red"))
        # Loop over each row in the CSV file and store them
        rows = []
        for row in reader:
            rows.append(row)
        return rows

def __plot_tests_vs_students(data, title, colors, name):
    data.plot(kind="bar", figsize=(15, 8), color=colors)
    plt.title(title)
    plt.xlabel("Test-Cases")
    plt.ylabel("% of students")
    plt.ylim([0, 1])
    plt.yticks([0.1 * x for x in range(11)])
    plt.savefig(os.path.join(bookkeeping.TARGET_DIRECTORY, f"{name}.eps"), format="eps")
    plt.savefig(os.path.join(bookkeeping.TARGET_DIRECTORY, f"{name}.png"), format="png")
    print(colored(f"Successfully created score plot {name}", "green"))
    plt.cla()


def __plot_project(project_name : str, csv_file_name : str, score_metric : test_info.Score_Metric, relative_ratios : bool = True, include_fixed_main_exec : bool = False) -> None:
    rows = __read_csv(csv_file_name)
    project_index = test_info.CSV_HEADER.index("Project")
    test_index = test_info.CSV_HEADER.index("Test")
    total_index = test_info.CSV_HEADER.index("Submissions")
    score_metric_text = "Presentation Score" if score_metric == test_info.Score_Metric.PRESENTATION else "Exam Results" if score_metric == test_info.Score_Metric.EXAM else ""
    tp_index = test_info.CSV_HEADER.index(f"True Positives ({score_metric_text})")
    fp_index = test_info.CSV_HEADER.index(f"False Positives ({score_metric_text})")
    tn_index = test_info.CSV_HEADER.index(f"True Negatives ({score_metric_text})")
    fn_index = test_info.CSV_HEADER.index(f"False Negatives ({score_metric_text})")
    err_index = test_info.CSV_HEADER.index("Errors")
    plot_data = pd.DataFrame({ 
        "True Positives":  [int(row[tp_index])/(1 if not relative_ratios else int(row[total_index])) 
                            for row in rows 
                            if project_name in row[project_index] and ("fixed_main_exec" not in row[test_index] or include_fixed_main_exec)],
        "False Positives": [int(row[fp_index])/(1 if not relative_ratios else int(row[total_index]))  
                            for row in rows 
                            if project_name in row[project_index] and ("fixed_main_exec" not in row[test_index] or include_fixed_main_exec)],
        "True Negatives":  [int(row[tn_index])/(1 if not relative_ratios else int(row[total_index]))  
                            for row in rows 
                            if project_name in row[project_index] and ("fixed_main_exec" not in row[test_index] or include_fixed_main_exec)],
        "False Negatives": [int(row[fn_index])/(1 if not relative_ratios else int(row[total_index])) 
                            for row in rows 
                            if project_name in row[project_index] and ("fixed_main_exec" not in row[test_index] or include_fixed_main_exec)],
        "Errors":          [int(row[err_index])/(1 if not relative_ratios else int(row[total_index]))  
                            for row in rows 
                            if project_name in row[project_index] and ("fixed_main_exec" not in row[test_index] or include_fixed_main_exec)]
    }, index=[row[test_index] for row in rows 
              if project_name in row[project_index] and ("fixed_main_exec" not in row[test_index] or include_fixed_main_exec)])
    score_metric_string = "_presentation" if score_metric == test_info.Score_Metric.PRESENTATION else "_exam" if score_metric == test_info.Score_Metric.EXAM else ""
    ratio_type_string = "_relative" if relative_ratios else "_absolute"
    fm_string = "_with_fixed_main_exec" if include_fixed_main_exec else ""
    plot_name = f"{project_name}_plot_counts{score_metric_string}{ratio_type_string}{fm_string}"
    __plot_tests_vs_students(plot_data, project_name, [GREEN, RED, ORANGE, BLUE, BLACK], plot_name)
    accuracy_index = test_info.CSV_HEADER.index(f"Accuracy ({score_metric_text})")
    recall_index = test_info.CSV_HEADER.index(f"Recall ({score_metric_text})")
    precision_index = test_info.CSV_HEADER.index(f"Precision ({score_metric_text})")
    plot_data = pd.DataFrame({
        "Accuracy":        [float(row[accuracy_index]) 
                            for row in rows 
                            if project_name in row[project_index] and ("fixed_main_exec" not in row[test_index] or include_fixed_main_exec)],
        "Recall":          [float(row[recall_index]) 
                            for row in rows 
                            if project_name in row[project_index] and ("fixed_main_exec" not in row[test_index] or include_fixed_main_exec)],
        "Precision":       [float(row[precision_index]) 
                            for row in rows 
                            if project_name in row[project_index] and ("fixed_main_exec" not in row[test_index] or include_fixed_main_exec)]
    }, index=[row[test_index] for row in rows 
              if project_name in row[project_index] and ("fixed_main_exec" not in row[test_index] or include_fixed_main_exec)])
    plot_name = f"{project_name}_plot_scores{score_metric_string}{ratio_type_string}{fm_string}"
    __plot_tests_vs_students(plot_data, project_name, [PURPLE, NEON, BROWN], plot_name)