import bookkeeping
import extract
import plot
import test_info as ti

def run_for_gdi(output_file):
    extract.setup_and_prepare_directories(clear_target_directory=False)
    extract.extract_projects(include=bookkeeping.GDI_2021+bookkeeping.GDI_2022, exclude=[])
    output_file = extract.one_csv_to_rule_them_all()
    plot.clear_plots()

    for project in bookkeeping.GDI_2022:
        plot.plot_project(project, output_file, ti.Score_Metric.PRESENTATION)
        plot.plot_project(project, output_file, ti.Score_Metric.EXAM)
        plot.plot_project(project, output_file, ti.Score_Metric.PRESENTATION, include_fixed_main_exec=True)
        plot.plot_project(project, output_file, ti.Score_Metric.EXAM, include_fixed_main_exec=True)
    
    for project in bookkeeping.GDI_2021:
        plot.plot_project(project, output_file, ti.Score_Metric.PRESENTATION)
    
    for project_2022 in bookkeeping.GDI_2022:
        for project_2021 in bookkeeping.GDI_2021:
            if bookkeeping.extract_name_from_project(project_2022) in project_2021:
                plot.plot_projects_against_each_other(project_2021, project_2022, output_file, ti.Score_Metric.PRESENTATION)
    
    plot.plot_module(bookkeeping.GDI_2022_M_1, "GDI_2022_M_1", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2022_M_2, "GDI_2022_M_2", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2022_M_3, "GDI_2022_M_3", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2022_M_4, "GDI_2022_M_4", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2022_M_5, "GDI_2022_M_5", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2022_M_6, "GDI_2022_M_6", output_file, ti.Score_Metric.PRESENTATION)
    
    plot.plot_module(bookkeeping.GDI_2022_M_1, "GDI_2022_M_1", output_file, ti.Score_Metric.EXAM)
    plot.plot_module(bookkeeping.GDI_2022_M_2, "GDI_2022_M_2", output_file, ti.Score_Metric.EXAM)
    plot.plot_module(bookkeeping.GDI_2022_M_3, "GDI_2022_M_3", output_file, ti.Score_Metric.EXAM)
    plot.plot_module(bookkeeping.GDI_2022_M_4, "GDI_2022_M_4", output_file, ti.Score_Metric.EXAM)
    plot.plot_module(bookkeeping.GDI_2022_M_5, "GDI_2022_M_5", output_file, ti.Score_Metric.EXAM)
    plot.plot_module(bookkeeping.GDI_2022_M_6, "GDI_2022_M_6", output_file, ti.Score_Metric.EXAM)
    
    plot.plot_module(bookkeeping.GDI_2021_M_1, "GDI_2021_M_1", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2021_M_2, "GDI_2021_M_2", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2021_M_3, "GDI_2021_M_3", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2021_M_4, "GDI_2021_M_4", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2021_M_5, "GDI_2021_M_5", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2021_M_6, "GDI_2021_M_6", output_file, ti.Score_Metric.PRESENTATION)

    plot.plot_module(bookkeeping.GDI_2022, "GDI_2022", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2022, "GDI_2022", output_file, ti.Score_Metric.EXAM)
    plot.plot_module(bookkeeping.GDI_2022_DO, "GDI_2022_DO", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2022_DO, "GDI_2022_DO", output_file, ti.Score_Metric.EXAM)

    plot.plot_module(bookkeeping.GDI_2021, "GDI_2021", output_file, ti.Score_Metric.PRESENTATION)
    plot.plot_module(bookkeeping.GDI_2021_DO, "GDI_2021_DO", output_file, ti.Score_Metric.PRESENTATION)



def sample():
    extract.setup_and_prepare_directories(clear_target_directory=False)
    extract.extract_projects(include=bookkeeping.SAMPLE, exclude=[])
    output_file = extract.one_csv_to_rule_them_all()
    plot.clear_plots()
    plot.plot_project(bookkeeping.SAMPLE[0], output_file, ti.Score_Metric.PRESENTATION)


if __name__ == '__main__':
    # sample()
    run_for_gdi("out.txt")