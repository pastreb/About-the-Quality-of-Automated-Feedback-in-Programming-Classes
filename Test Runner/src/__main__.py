import bookkeeping
import extract


def run_for_gdi():
    extract.setup_and_prepare_directories(clear_target_directory=False)
    extract.extract_projects(include=bookkeeping.GDI_2021, exclude=[], run_tests=False)
    extract.extract_projects(include=bookkeeping.GDI_2022, exclude=[], run_tests=True)


def run_for_chosen():
    extract.setup_and_prepare_directories(clear_target_directory=False)
    extract.extract_projects(include=bookkeeping.CHOSEN, exclude=[], run_tests=True)


def sample():
    extract.setup_and_prepare_directories(clear_target_directory=False)
    extract.extract_projects(include=bookkeeping.SAMPLE, exclude=[])


if __name__ == "__main__":
    # sample()
    run_for_chosen()
