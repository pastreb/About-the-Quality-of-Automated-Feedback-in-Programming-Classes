import bookkeeping
import extract

if __name__ == "__main__":
    extract.setup_and_prepare_directories(clear_target_directory=False)
    extract.extract_projects(
        include=["GDI_2022_M_1_A_2_Temperaturberechnung"], exclude=[]
    )
