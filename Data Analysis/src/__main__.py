from extract import *

gdi_2022_modul_1 = ["GDI_2022_M_1_A_1_Ein_erstes_Programm_und_Datentypen",
                    "GDI_2022_M_1_A_2_Temperaturberechnung",
                    "GDI_2022_M_1_A_3_Zeichenketten_und_Variablentausch",
                    "GDI_2022_M_1_A_4_Kreisberechnung",
                    "GDI_2022_M_1_SA_1_Geldautomat",
                    "GDI_2022_M_1_SA_2_Verschluesselung"]
gdi_2022_modul_2 = ["GDI_2022_M_2_A_1_Berechnungsreihe",
                    "GDI_2022_M_2_A_2_Pin_Code",
                    "GDI_2022_M_2_SA_1_Zahlen_raten",
                    "GDI_2022_M_2_SA_2_Notenprogramm",
                    "GDI_2022_M_2_SA_3_Pokern",
                    "GDI_2022_M_3_A_2_Kartenspiel"]
gdi_2022_modul_3 = ["GDI_2022_M_3_A_3_Medikamenten_Simulation",
                    "GDI_2022_M_3_SA_1_To_Do_Liste",
                    "GDI_2022_M_3_SA_2_Such_und_Sortieralgorithmen",
                    "GDI_2022_M_3_SA_3_1_Auswerten_von_Einzelbasen",
                    "GDI_2022_M_3_SA_3_2_Auswerten_von_Basen_Sequenzen",
                    "GDI_2022_M_3_SA_3_3_Auswerten_einer_Liste_von_Basen_Sequenzen",
                    "GDI_2022_M_3_SA_3_4_Testen_einer_Hypothese_mittels_DNA_Sequenzanalyse"]
                    # TODO:
                    # GDI_2022_M_3_A_1_Planeten
gdi_2022_modul_4 = ["GDI_2022_M_4_A_1_Lieferschein",
                    "GDI_2022_M_4_A_2_Simulation_einer_ansteckenden_Krankheit",
                    "GDI_2022_M_4_SA_1_Bowling",
                    "GDI_2022_M_4_SA_2_Erweiterungen_zur_Case_Study",
                    "GDI_2022_M_4_SA_3_Schere_Stein_Papier_Spiel"]
gdi_2022_modul_5 = ["GDI_2022_M_5_A_1_Erdbebendaten",
                    "GDI_2022_M_5_SA_1_Wetterstationen"]
gdi_2022_modul_6 = ["GDI_2022_M_6_A_1_Vektoren",
                    "GDI_2022_M_6_A_2_Matrizen_Boss_Puzzle",
                    "GDI_2022_M_6_A_3_Waermeausbreitung_in_einem_Metallstab",
                    "GDI_2022_M_6_A_4_Waermeausbreitung_in_einer_Platte"]
gdi_2022 = gdi_2022_modul_1 + gdi_2022_modul_2 + gdi_2022_modul_3 + gdi_2022_modul_4 + gdi_2022_modul_5 + gdi_2022_modul_6

# DONE:
# APro_2021_M_1A_A_1_Temperaturberechnung
# APro_2021_M_1A_A_2_Zeichenketten_und_Variablentausch
# APro_2021_M_1A_A_3_Kreisberechnung

def setup(source, target, clear_target_directory):
    if os.name == 'nt': 
        os.system("color") # if on Windows we need to activate colored print
    source_directory = os.path.join(os.path.dirname(__file__), "..", "data", source)
    if not os.path.exists(source_directory):
        exit(colored("Source directory", source_directory, "does not exist", "red"))
    target_directory = os.path.join(os.path.dirname(__file__), "..", "data", target)
    if os.path.exists(target_directory) and clear_target_directory:
        try:
            shutil.rmtree(target_directory)
        except OSError as error:
            exit(colored("Failed to delete directory\n", error, "red"))
        os.mkdir(target_directory)    
    return source_directory, target_directory

if __name__ == '__main__':
    source_directory, target_directory = setup(source="raw_student_data", target="processed_student_data", clear_target_directory=True)
    for source_project in os.listdir(source_directory):
        source_project_directory = os.path.join(source_directory, source_project)
        target_project_directory = os.path.join(target_directory, source_project)

        if os.path.isdir(source_project_directory) and (source_project == "GDI_2022_M_6_SA_1_Galton_Board" or source_project == ""):
            print("Processing", source_project)
            os.mkdir(target_project_directory)
            extract_project(source_project_directory, target_project_directory)
        elif os.path.isfile(source_project_directory):
            shutil.copy(source_project_directory, target_directory)
    for project in (f.path for f in os.scandir(target_directory) if f.is_dir()): # traverse course projects
        scoreboard_file = os.path.join(target_directory, re.findall("GDI|APro|AIT|SAMPLE", project)[0] + "_" + re.findall("2021|2022|2023", project)[0] + "_" + "Scoreboard.csv")
        student_grades = extract_presentation_grades_from_scoreboard(project, scoreboard_file)
        print(str(collect_student_data_from_project(project, student_grades)).replace(",", "\n"))