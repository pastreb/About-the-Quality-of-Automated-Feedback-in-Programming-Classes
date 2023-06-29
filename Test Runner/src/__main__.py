import bookkeeping
import extract


def run_for_gdi():
    extract.setup_and_prepare_directories(clear_target_directory=False)
    extract.extract_projects(include=bookkeeping.GDI_2021, exclude=[], run_tests=False)
    extract.extract_projects(include=bookkeeping.GDI_2022, exclude=[], run_tests=True)


def sample():
    extract.setup_and_prepare_directories(clear_target_directory=False)
    extract.extract_projects(include=bookkeeping.SAMPLE, exclude=[])


if __name__ == "__main__":
    run_for_gdi()
    # PROBLEMATIC: GDI_2022_M_2_A_2_Pin, GDI_2022_M_4_A_1_Lieferschein
