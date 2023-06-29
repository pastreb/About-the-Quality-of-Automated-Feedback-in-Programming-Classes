import bookkeeping
import collect
import plot
import test_info as ti

def run_for_gdi():
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



def sample():
    output_file = collect.one_csv_to_rule_them_all()
    plot.clear_plots()
    plot.plot_project(bookkeeping.SAMPLE[0], output_file, ti.Score_Metric.PRESENTATION)


if __name__ == '__main__':
    # sample()
    run_for_gdi()