import extract
import bookkeeping

if __name__ == '__main__':
    extract.setup_and_prepare_directories(clear_target_directory=True)
    extract.extract_projects(include=bookkeeping.SAMPLE, exclude=[])
    extract.one_csv_to_rule_them_all()