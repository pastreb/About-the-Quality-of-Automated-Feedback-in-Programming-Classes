import bookkeeping
import extract

if __name__ == '__main__':
    extract.setup_and_prepare_directories(clear_target_directory=False)
    extract.extract_projects(include=bookkeeping.APRO_2023_M_1, exclude=[])