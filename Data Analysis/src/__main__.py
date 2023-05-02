import bookkeeping
import extract
import plot
import test_info

if __name__ == '__main__':
    extract.setup_and_prepare_directories(clear_target_directory=True)
    extract.extract_projects(include=bookkeeping.SAMPLE, exclude=[])
    output_file = extract.one_csv_to_rule_them_all()
    plot.__plot_project(bookkeeping.SAMPLE[0], output_file, test_info.Score_Metric.PRESENTATION)