import os
import re
from termcolor import colored # for printing funny colored text

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib.pyplot as plt

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

# Define a global dictionary to cache already loaded CSV files
read_csvs = {}

def __read_csv(file_name : str) -> pd.DataFrame:
    
    """
    Loads a CSV file as a pandas DataFrame and validates its contents.
    
    Args:
        file_name (str): The name of the CSV file to load.
    
    Returns:
        pd.DataFrame: A pandas DataFrame containing the contents of the CSV file.
    """
    
    # Check if the CSV file has already been loaded
    if(file_name in read_csvs):
        return read_csvs[file_name]
    # Construct the path to the CSV file
    csv_path = os.path.join(bookkeeping.TARGET_DIRECTORY, file_name)
    # Check if the CSV file exists
    if not os.path.isfile(csv_path):
        exit(colored(f"Could not find {csv_path} for plotting", "red"))
    # Load the CSV file into a pandas DataFrame
    data_frame = pd.read_csv(csv_path)
    # Validate the header
    header = data_frame.columns.values
    if len(header) != len(ti.CSV_HEADER) or False in [(header[i] == ti.CSV_HEADER[i]) for i in range(len(header))]:
        exit(colored(f"CSV header seems to be corrupted:\n {header}\n vs.\n {ti.CSV_HEADER}", "red"))
    # Cache the loaded CSV file
    read_csvs[file_name] = data_frame
    return data_frame



def __get_project_data(project_names : list, csv_file_name : str, relative_ratios : bool = True, include_fixed_main_exec : bool = False) -> pd.DataFrame:

    """
    Extracts project data from a CSV file and performs some data cleaning and processing.
    
    Args:
        project_names (list): A list of project names to include in the extracted data.
        csv_file_name (str): The name of the CSV file to read from.
        relative_ratios (bool, optional): Whether to convert absolute counts to relative ratios (default True).
        include_fixed_main_exec (bool, optional): Whether to include or exclude the 'fixed_main_exec' versions of a test (default False).
    
    Returns:
        pd.DataFrame: A pandas DataFrame containing the extracted and processed project data.
    """

    # Load the CSV file into a pandas DataFrame
    data_frame = __read_csv(csv_file_name)
    # Filter out the 'fixed_main_exec' versions of a test if include_fixed_main_exec is False
    if not include_fixed_main_exec:
        data_frame = data_frame[~data_frame["Test"].str.contains("fixed_main_exec")]
    else:
        # Otherwise rename 'fixed_main_exec' versions
        data_frame["Test"] = data_frame["Test"].str.replace("fixed_main_exec", "fme")
    # Filter the DataFrame to only include the specified project names
    data_frame = data_frame.loc[data_frame["Project"].isin(project_names)]
    # Check if the resulting DataFrame is empty
    if data_frame.empty:
        exit(colored(f"DataFrame for project(s) {project_names} is empty\n {data_frame}", "red"))
    # Convert absolute counts to relative ratios (if specified)
    if relative_ratios:
        for col in (list(set(ti.CSV_PS_COUNTS) | set(ti.CSV_ER_COUNTS))):
            data_frame[col] = data_frame[col]/data_frame["Submissions"]
    return data_frame



def __clean_project_name(project_name : str) -> str:

    """
    Cleans the given project name by removing unnecessary information.
    
    Args:
        project_name (str): A string representing the project name.
    
    Returns:
        str: A string representing the cleaned project name.
    """

    course_prefixes = "|".join(bookkeeping.COURSE_PREFIXES)
    years = "|".join(bookkeeping.YEARS)
    regex = f"(?:{course_prefixes})_(?:{years})_M_\d*_(?:A|SA)_\d*"
    cleaned_project_name = re.findall(regex, project_name)
    return cleaned_project_name[0] if len(cleaned_project_name) == 1 else project_name


def plot_project(project_name : str, csv_file_name : str, score_metric : ti.Score_Metric, relative_ratios : bool = True, include_fixed_main_exec : bool = False) -> None:

    """
    Plots the test results of a single project.

    Parameters:
        project_name (str): The name of the project to plot.
        csv_file_name (str): The name of the CSV file containing the test results.
        score_metric (ti.Score_Metric): The score metric to be used for plotting. Can be one of ti.Score_Metric.PRESENTATION or ti.Score_Metric.EXAM.
        relative_ratios (bool, optional): Whether to use relative ratios or absolute counts (default True).
        include_fixed_main_exec (bool, optional): Whether to include fixed_main_exec tests (default False).

    Returns:
        None: The function only creates and saves a plot.
    """

    # Get data
    data = __get_project_data([project_name], csv_file_name, relative_ratios, include_fixed_main_exec)
    data = data.set_index("Test")
    # Get data into shape for first plot (with counts, e.g. "True Positives")
    if score_metric == ti.Score_Metric.PRESENTATION:
        count_data = data[ti.CSV_PS_COUNTS]
    elif score_metric == ti.Score_Metric.EXAM:
        count_data = data[ti.CSV_ER_COUNTS]
    else:
        count_data = data
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
    if score_metric == ti.Score_Metric.PRESENTATION:
        score_data = data[ti.CSV_PS_SCORES]
    elif score_metric == ti.Score_Metric.EXAM:
        score_data = data[ti.CSV_ER_SCORES]
    else:
        score_data = data
    for col in score_data.columns.values:
        score_data = score_data.rename(columns={col : col.replace(" (Presentation Score)", "").replace(" (Exam Result)", "")})
    # Second plot
    plot_name = f"{__clean_project_name(project_name)}_Plot_Scores{score_metric_string}{ratio_type_string}{fm_string}"
    __plot_tests_vs_students(score_data, project_name, [PURPLE, NEON, BROWN], plot_name)



def plot_projects_against_each_other(project_1_name : str, project_2_name : str, csv_file_name : str, score_metric : ti.Score_Metric, relative_ratios : bool = True) -> None:

    """
    Plots the comparison of two projects (optimally the same project from different years) against each other based on the provided score metric, with counts and scores.

    Args:
        project_1_name (str): The name of the first project to be plotted.
        project_2_name (str): The name of the second project to be plotted.
        csv_file_name (str): The name of the CSV file containing the data to be plotted.
        score_metric (ti.Score_Metric): The score metric to be used for plotting. Can be one of ti.Score_Metric.PRESENTATION or ti.Score_Metric.EXAM.
        relative_ratios (bool, optional): Whether to plot relative or absolute ratios (default True).

    Returns:
        None: The function only creates and saves a plot.
    """

    # Get data
    data = __get_project_data([project_1_name, project_2_name], csv_file_name, relative_ratios)
    data = data.sort_values("Test")
    data["Project"] = data["Project"].apply(__clean_project_name)
    data = data.set_index(["Project", "Test"])
    # Get data into shape for first plot (with counts, e.g. "True Positives")
    if score_metric == ti.Score_Metric.PRESENTATION:
        count_data = data[ti.CSV_PS_COUNTS]
    elif score_metric == ti.Score_Metric.EXAM:
        count_data = data[ti.CSV_ER_COUNTS]
    else:
        count_data = data
    for col in count_data.columns.values:
        count_data = count_data.rename(columns={col : col.replace(" (Presentation Score)", "").replace(" (Exam Result)", "")})
    # Prepare plot name
    score_metric_string = "_Presentation" if score_metric == ti.Score_Metric.PRESENTATION else "_Exam" if score_metric == ti.Score_Metric.EXAM else ""
    ratio_type_string = "_Relative" if relative_ratios else "_Absolute"
    plot_name = f"{__clean_project_name(project_1_name)}_vs_{__clean_project_name(project_2_name)}_Plot_Counts{score_metric_string}{ratio_type_string}"
    # First plot
    __plot_tests_vs_students(count_data, f"{project_1_name} vs {project_2_name}", [GREEN, RED, ORANGE, BLUE, BLACK], plot_name)
    # Get data into shape for first plot (with scores, e.g. "Accuracy")
    if score_metric == ti.Score_Metric.PRESENTATION:
        score_data = data[ti.CSV_PS_SCORES]
    elif score_metric == ti.Score_Metric.EXAM:
        score_data = data[ti.CSV_ER_SCORES]
    else:
        score_data = data
    for col in score_data.columns.values:
        score_data = score_data.rename(columns={col : col.replace(" (Presentation Score)", "").replace(" (Exam Result)", "")})
    # Second plot
    plot_name = f"{__clean_project_name(project_1_name)}_vs_{__clean_project_name(project_2_name)}_Plot_Sounts{score_metric_string}{ratio_type_string}"
    __plot_tests_vs_students(count_data, f"{project_1_name} vs {project_2_name}", [GREEN, RED, ORANGE, BLUE, BLACK], plot_name)



def plot_module(module : list, module_name : str, csv_file_name : str, score_metric : ti.Score_Metric, relative_ratios : bool = True) -> None:

    """
    Plots the average scores for the projects in a given module.

    Args:
        module (list): A list of project names within the module to be plotted.
        module_name (str): A string containing the name of the module to be plotted.
        csv_file_name (str): A string containing the name of the CSV file containing the data.
        score_metric (ti.Score_Metric): The score metric to be used for plotting. Can be one of ti.Score_Metric.PRESENTATION or ti.Score_Metric.EXAM.
        relative_ratios (bool): A boolean indicating whether to plot relative ratios or absolute values (default True).

    Returns:
        None: The function only creates and saves a plot.
    """

    # Get data
    data = __get_project_data(module, csv_file_name, relative_ratios)
    # Get data into shape for plot
    if score_metric == ti.Score_Metric.PRESENTATION:
        data = data[list(set(ti.CSV_PS_COUNTS) | set(ti.CSV_PS_SCORES))]
    elif score_metric == ti.Score_Metric.EXAM:
        data = data[list(set(ti.CSV_ER_COUNTS) | set(ti.CSV_ER_SCORES))]
    else:
        data = data
    for col in data.columns.values:
        data = data.rename(columns={col : col.replace(" (Presentation Score)", "").replace(" (Exam Result)", "")})
    data = data.mean()
    # Prepare plot name
    score_metric_string = "_Presentation" if score_metric == ti.Score_Metric.PRESENTATION else "_Exam" if score_metric == ti.Score_Metric.EXAM else ""
    ratio_type_string = "_Relative" if relative_ratios else "_Absolute"
    plot_name = f"{module_name}_Plot{score_metric_string}{ratio_type_string}"
    # Plot
    __plot_tests_vs_students(data, module_name, [GREEN, RED, ORANGE, BLUE, BLACK, PURPLE, NEON, BROWN], plot_name)



def __plot_tests_vs_students(data : pd.DataFrame, title : str, colors : list, name : str) -> None:

    """
    Plots a bar chart comparing the performance of different test cases across all students in the given data.
    
    Args:
        data (pd.DataFrame): A Pandas DataFrame containing the data to be plotted.
        title (str): A string representing the title of the plot.
        colors (list): A list of colors to be used for the plot.
        name(str): A string representing the name of the plot file.
    
    Returns:
        None: The function only creates and saves a plot.
    """

    data.plot(kind="bar", figsize=(16, 16), rot=45, color=colors)
    plt.title(title)
    plt.xlabel("Test-Cases")
    plt.ylabel("% of students")
    plt.ylim([0, 1])
    plt.yticks([0.1 * x for x in range(11)])
    plt.savefig(os.path.join(bookkeeping.TARGET_DIRECTORY, f"{name}.svg"), format="svg")
    plt.savefig(os.path.join(bookkeeping.TARGET_DIRECTORY, f"{name}.png"), format="png")
    print(colored(f"Successfully created Plot {name}", "green"))
    plt.cla()