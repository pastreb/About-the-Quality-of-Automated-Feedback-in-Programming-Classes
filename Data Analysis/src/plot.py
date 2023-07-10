import os
import re
from termcolor import colored # for printing funny colored text

import pandas as pd
pd.options.mode.chained_assignment = None  # default='warn'
import matplotlib
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

colors = {
         ti.CSV_TP_PS: GREEN, 
         ti.CSV_FP_PS: RED,
         ti.CSV_TN_PS: BLUE,
         ti.CSV_FN_PS: ORANGE,
         ti.CSV_A_PS: PURPLE,
         ti.CSV_R_PS: NEON,
         ti.CSV_P_PS: BROWN,
         ti.CSV_TP_ER: GREEN, 
         ti.CSV_FP_ER: RED,
         ti.CSV_TN_ER: BLUE,
         ti.CSV_FN_ER: ORANGE,
         ti.CSV_A_ER: PURPLE,
         ti.CSV_R_ER: NEON,
         ti.CSV_P_ER: BROWN,
         ti.CSV_ERRORS : BLACK
         }

def clear_plots() -> None:

    """
    Removes all the .png and .svg files present in the directory specified by bookkeeping.TARGET_DIRECTORY.

    If bookkeeping.TARGET_DIRECTORY does not exist, then this function does nothing.

    Raises:
        Exception: If any file can not be deleted, an exception will be raised and the program will exit.

    Returns:
        None
    """

    if not os.path.exists(bookkeeping.TARGET_DIRECTORY):
        return
    # Iterate through all the directories in bookkeeping.TARGET_DIRECTORY
    for file in os.listdir(bookkeeping.TARGET_DIRECTORY):
        file_path = os.path.join(bookkeeping.TARGET_DIRECTORY, file)
        # Delete the file if it is a .png or .svg file
        if os.path.isfile(file_path) and (file.endswith(".png") or file.endswith(".svg")):
            try:
                # Delete the file
                os.remove(file_path)
            except Exception as e:
                exit(colored(f"Failed to delete file\n{type(e)}\n{e.args}\n{e}", "red"))

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



def __get_project_data(project_names : list, test_names : list, csv_file_name : str, relative_ratios : bool = True) -> pd.DataFrame:

    """
    Extracts project data from a CSV file and performs some data cleaning and processing.
    
    Args:
        project_names (list): A list of project names to include in the extracted data.
        test_names (list): A list of test names to include in the extracted data.
        csv_file_name (str): The name of the CSV file to read from.
        relative_ratios (bool, optional): Whether to convert absolute counts to relative ratios (default True).
    
    Returns:
        pd.DataFrame: A pandas DataFrame containing the extracted and processed project data.
    """

    # Load the CSV file into a pandas DataFrame
    data_frame = __read_csv(csv_file_name)
    # Filter the DataFrame to only include the specified project names and test names
    data_frame = data_frame.loc[data_frame["Project"].isin(project_names)].loc[data_frame["Test Cases"].isin(test_names)]
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


def plot_project(project_name : str, test_names : str, csv_file_name : str, score_metric : ti.Score_Metric, relative_ratios : bool = True) -> None:

    """
    Plots the test results of a single project.

    Parameters:
        project_name (str): The name of the project to plot.
        test_names (list): The names of the test cases to plot.
        csv_file_name (str): The name of the CSV file containing the test results.
        score_metric (ti.Score_Metric): The score metric to be used for plotting. Can be one of ti.Score_Metric.PRESENTATION or ti.Score_Metric.EXAM.
        relative_ratios (bool, optional): Whether to use relative ratios or absolute counts (default True).

    Returns:
        None: The function only creates and saves a plot.
    """

    # Get data
    data = __get_project_data([project_name], test_names, csv_file_name, relative_ratios)
    # Have different versions of tests next to each other
    data = data.sort_values("Test")
    # Include n in labels
    labels = []
    for element in data.values:
        labels.append(f"{element[list(data.columns.values).index('Test')]}\n(n={element[list(data.columns.values).index('Submissions')]})")
    data["Test"] = labels
    data = data.set_index("Test")
    # Get data into shape for plot
    if score_metric == ti.Score_Metric.PRESENTATION:
        count_data = data[ti.CSV_PS_COUNTS]
        score_data = data[ti.CSV_PS_SCORES]
    elif score_metric == ti.Score_Metric.EXAM:
        count_data = data[ti.CSV_ER_COUNTS]
        score_data = data[ti.CSV_ER_SCORES]
    # Prepare plot name
    score_metric_string = "_Presentation" if score_metric == ti.Score_Metric.PRESENTATION else "_Exam" if score_metric == ti.Score_Metric.EXAM else ""
    ratio_type_string = "_Relative" if relative_ratios else "_Absolute"
    plot_name = f"{__clean_project_name(project_name)}_Plot{score_metric_string}{ratio_type_string}"
    # Plot
    __plot_bar(count_data, score_data, project_name, plot_name)



def plot_projects_against_each_other(project_1_name : str, project_2_name : str, test_names : list, csv_file_name : str, score_metric : ti.Score_Metric, relative_ratios : bool = True) -> None:

    """
    Plots the comparison of two projects (optimally the same project from different years) against each other based on the provided score metric, with counts and scores.

    Args:
        project_1_name (str): The name of the first project to be plotted.
        project_2_name (str): The name of the second project to be plotted.
        test_names (list): The names of the tests to be plotted.
        csv_file_name (str): The name of the CSV file containing the data to be plotted.
        score_metric (ti.Score_Metric): The score metric to be used for plotting. Can be one of ti.Score_Metric.PRESENTATION or ti.Score_Metric.EXAM.
        relative_ratios (bool, optional): Whether to plot relative or absolute ratios (default True).

    Returns:
        None: The function only creates and saves a plot.
    """

    # Get data
    data = __get_project_data([project_1_name, project_2_name], test_names, csv_file_name, relative_ratios)
    data = data.sort_values("Test")
    data["Project"] = data["Project"].apply(__clean_project_name)
    data = data.set_index(["Project", "Test"])
    # Get data into shape for plot
    if score_metric == ti.Score_Metric.PRESENTATION:
        count_data = data[ti.CSV_PS_COUNTS]
        score_data = data[ti.CSV_PS_SCORES]
    elif score_metric == ti.Score_Metric.EXAM:
        count_data = data[ti.CSV_ER_COUNTS]
        score_data = data[ti.CSV_ER_SCORES]
    # Prepare plot name
    score_metric_string = "_Presentation" if score_metric == ti.Score_Metric.PRESENTATION else "_Exam" if score_metric == ti.Score_Metric.EXAM else ""
    ratio_type_string = "_Relative" if relative_ratios else "_Absolute"
    plot_name = f"{__clean_project_name(project_1_name)}_vs_{__clean_project_name(project_2_name)}_Plot{score_metric_string}{ratio_type_string}"
    # Plot
    __plot_bar(count_data, score_data, f"{project_1_name} vs {project_2_name}", plot_name)



def plot_module(module : list, module_name : str, test_names : list, csv_file_name : str, score_metric : ti.Score_Metric, relative_ratios : bool = True) -> None:

    """
    Plots the average scores for the projects in a given module.

    Args:
        module (list): A list of project names within the module to be plotted.
        module_name (str): A string containing the name of the module to be plotted.
        test_names (list): The names of the test cases to be plotted.
        csv_file_name (str): A string containing the name of the CSV file containing the data.
        score_metric (ti.Score_Metric): The score metric to be used for plotting. Can be one of ti.Score_Metric.PRESENTATION or ti.Score_Metric.EXAM.
        relative_ratios (bool): A boolean indicating whether to plot relative ratios or absolute values (default True).

    Returns:
        None: The function only creates and saves a plot.
    """

    # Get data
    data = __get_project_data(module, test_names, csv_file_name, relative_ratios)
    # Get data into shape for plot
    data["Project"] = data["Project"].apply(__clean_project_name)
    data = data.groupby("Project").mean(numeric_only=True)
    if score_metric == ti.Score_Metric.PRESENTATION:
        data = data[ti.CSV_PS_COUNTS+ti.CSV_PS_SCORES]
    elif score_metric == ti.Score_Metric.EXAM:
        data = data[ti.CSV_ER_COUNTS+ti.CSV_ER_SCORES]
    # Prepare plot name
    score_metric_string = "_Presentation" if score_metric == ti.Score_Metric.PRESENTATION else "_Exam" if score_metric == ti.Score_Metric.EXAM else ""
    ratio_type_string = "_Relative" if relative_ratios else "_Absolute"
    plot_name = f"{module_name}_Plot{score_metric_string}{ratio_type_string}"
    # Plot
    __plot_lines(data, module_name, plot_name)



# TODO: Update Documentation
def __plot_bar(count_data : list[pd.DataFrame], score_data : list[pd.DataFrame], title : str, name : str) -> None:

    """
    Plots a bar chart comparing the performance of different test cases across all students in the given data.
    
    Args:
        data (pd.DataFrame): A Pandas DataFrame containing the data to be plotted.
        title (str): A string representing the title of the plot.
        name(str): A string representing the name of the plot file.
    
    Returns:
        None: The function only creates and saves a plot.
    """

    width = len(count_data)
    ax = count_data.plot.bar(alpha=0.75, color=colors, edgecolor="black", figsize=(int(width*1.5+3), 8), linewidth=1, position=1, rot=45, stacked=True, width=0.3, ylabel="% of students")
    score_data.plot.bar(alpha=0.75, ax=ax, color=colors, edgecolor="black", linewidth=1, position=0, rot=0, sharex=True, width=0.3, stacked=False)
    # Show grid
    plt.gca().yaxis.grid(True)
    plt.title(title, loc="left")
    # Move legend out of the plot
    plt.legend(loc='center left',bbox_to_anchor=(1.0, 0.5))
    # Center the entire plot
    plt.xlim([-0.5, width-0.5])
    # Get some space above and below the bars
    plt.ylim([-0.05, 1.05])
    # Add horizontal lines
    plt.yticks([0.1 * x for x in range(11)])
    # Make clean
    plt.tight_layout()
    plt.savefig(os.path.join(bookkeeping.TARGET_DIRECTORY, f"{name}.svg"), format="svg")
    print(colored(f"Successfully created Plot {name}", "green"))
    plt.close()

# TODO: Documentation
def __plot_lines(data : list[pd.DataFrame], title : str, name : str) -> None:
    width = len(data)
    data.plot.line(color=colors, figsize=(int(width*0.5+3), 8), linewidth=3, rot=45, ylabel="% of students")
    plt.title(title, loc="left")
    # Move legend out of the plot
    plt.legend(loc='center left',bbox_to_anchor=(1.0, 0.5))
    # Center the entire plot
    plt.xlim([-0.5, width-0.5])
    # Get some space above and below the bars
    plt.ylim([-0.05, 1.05])
    # Add horizontal lines
    plt.yticks([0.1 * x for x in range(11)])
    # Make clean
    plt.tight_layout()
    plt.savefig(os.path.join(bookkeeping.TARGET_DIRECTORY, f"{name}.svg"), format="svg")
    print(colored(f"Successfully created Plot {name}", "green"))
    plt.close()