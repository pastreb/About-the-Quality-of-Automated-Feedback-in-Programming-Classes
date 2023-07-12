import bookkeeping
import collect
import plot
import test_info as ti
import os

def run_for_gdi():
    collect.setup_and_prepare_directories()
    output_file = collect.one_csv_to_rule_them_all()
    plot.clear_plots()

    for project in bookkeeping.GDI_2022:
        plot.plot_project(project, ["Original"], output_file, ti.Score_Metric.PRESENTATION)
        plot.plot_project(project, ["Original"], output_file, ti.Score_Metric.EXAM)
    
    for project in bookkeeping.GDI_2021:
        plot.plot_project(project, ["Original"], output_file, ti.Score_Metric.PRESENTATION)
    
    for project_2022 in bookkeeping.GDI_2022:
        for project_2021 in bookkeeping.GDI_2021:
            if bookkeeping.extract_name_from_project(project_2022) in project_2021:
                plot.plot_projects_against_each_other(project_2021, project_2022, ["Original"], output_file, ti.Score_Metric.PRESENTATION)
    
    plot.plot_module(bookkeeping.GDI_2022_M_1, ["Original"], "GDI_2022_M_1", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2022_M_2, ["Original"], "GDI_2022_M_2", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2022_M_3, ["Original"], "GDI_2022_M_3", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2022_M_4, ["Original"], "GDI_2022_M_4", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2022_M_5, ["Original"], "GDI_2022_M_5", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2022_M_6, ["Original"], "GDI_2022_M_6", output_file, ti.Score_Metric.PRESENTATION)
    
    plot.plot_module(bookkeeping.GDI_2022_M_1, ["Original"], "GDI_2022_M_1", output_file, ti.Score_Metric.EXAM)
    plot.plot_module(bookkeeping.GDI_2022_M_2, ["Original"], "GDI_2022_M_2", output_file, ti.Score_Metric.EXAM)
    plot.plot_module(bookkeeping.GDI_2022_M_3, ["Original"], "GDI_2022_M_3", output_file, ti.Score_Metric.EXAM)
    plot.plot_module(bookkeeping.GDI_2022_M_4, ["Original"], "GDI_2022_M_4", output_file, ti.Score_Metric.EXAM)
    plot.plot_module(bookkeeping.GDI_2022_M_5, ["Original"], "GDI_2022_M_5", output_file, ti.Score_Metric.EXAM)
    plot.plot_module(bookkeeping.GDI_2022_M_6, ["Original"], "GDI_2022_M_6", output_file, ti.Score_Metric.EXAM)
    
    plot.plot_module(bookkeeping.GDI_2021_M_1, ["Original"], "GDI_2021_M_1", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2021_M_2, ["Original"], "GDI_2021_M_2", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2021_M_3, ["Original"], "GDI_2021_M_3", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2021_M_4, ["Original"], "GDI_2021_M_4", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2021_M_5, ["Original"], "GDI_2021_M_5", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2021_M_6, ["Original"], "GDI_2021_M_6", output_file, ti.Score_Metric.PRESENTATION)

    plot.plot_module(bookkeeping.GDI_2022, "GDI_2022", ["Original"], output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2022, "GDI_2022", ["Original"], output_file, ti.Score_Metric.EXAM)
    plot.plot_module(bookkeeping.GDI_2022_DO, "GDI_2022_DO", ["Original"], output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2022_DO, "GDI_2022_DO", ["Original"], output_file, ti.Score_Metric.EXAM)

    plot.plot_module(bookkeeping.GDI_2021, "GDI_2021", ["Original"], output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2021_DO, "GDI_2021_DO", ["Original"], output_file, ti.Score_Metric.PRESENTATION)

def run_for_chosen(output_file=""):
    collect.setup_and_prepare_directories()
    if output_file == "":
        output_file = collect.one_csv_to_rule_them_all()
    plot.plot_project("APRO_2022_M_5_SA_1_Hotel", ["APRO_2022_M_5_SA_1_Hotel_Test_Cases_Chosen", "APRO_2022_M_5_SA_1_Hotel_Test_Cases_Chosen_ChatGPT", "APRO_2022_M_5_SA_1_Hotel_Test_Cases_Chosen_V0_Longer_Side_Effect",
                                                   "APRO_2022_M_5_SA_1_Hotel_Test_Cases_Chosen_V1_Export_Functions", "APRO_2022_M_5_SA_1_Hotel_Test_Cases_Chosen_V2_Check_and_Get_Function", "APRO_2022_M_5_SA_1_Hotel_Test_Cases_Chosen_V3_Check_Class", 
                                                   "APRO_2022_M_5_SA_1_Hotel_Test_Cases_Chosen_V4_Try_Catch", "APRO_2022_M_5_SA_1_Hotel_Test_Cases_Chosen_V5_Lenient"], output_file, ti.Score_Metric.PRESENTATION)

def sample():
    collect.setup_and_prepare_directories()
    output_file = collect.one_csv_to_rule_them_all()
    plot.clear_plots()
    plot.plot_project(bookkeeping.SAMPLE[0], ["Original"], output_file, ti.Score_Metric.PRESENTATION)
    

if __name__ == '__main__':
    # sample()
    run_for_chosen() # os.path.join(bookkeeping.TARGET_DIRECTORY, f"out.csv")