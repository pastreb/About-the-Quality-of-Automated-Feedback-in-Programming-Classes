import os

SOURCE_DIRECTORY = os.path.join(os.path.dirname(__file__), "..", "data", "raw_student_data")
TARGET_DIRECTORY = os.path.join(os.path.dirname(__file__), "..", "data", "processed_student_data")

COURSE_PERFIXES = ["GDI", "APRO", "AIT", "SAMPLE"]
YEARS = ["2020", "2021", "2022", "2023"]

SAMPLE =       [   
                    "SAMPLE_2023_M_1_Testprogramm"
                    ]

GDI_2022_M_1 = [
                    "GDI_2022_M_1_A_1_Ein_erstes_Programm_und_Datentypen",
                    "GDI_2022_M_1_A_2_Temperaturberechnung",
                    "GDI_2022_M_1_A_3_Zeichenketten_und_Variablentausch",
                    "GDI_2022_M_1_A_4_Kreisberechnung",
                    "GDI_2022_M_1_SA_1_Geldautomat",
                    "GDI_2022_M_1_SA_2_Verschluesselung"
                    ]

GDI_2022_M_2 = [
                    "GDI_2022_M_2_A_1_Berechnungsreihe",
                    "GDI_2022_M_2_A_2_Pin_Code",
                    "GDI_2022_M_2_SA_1_Zahlen_raten",
                    "GDI_2022_M_2_SA_2_Notenprogramm",
                    "GDI_2022_M_2_SA_3_Pokern", # TODO: regrade with fixed main_exec
                    ]

GDI_2022_M_3 = [
                    "GDI_2022_M_3_A_1_Planeten", # TODO: export, regrade with fixed main_exec
                    "GDI_2022_M_3_A_2_Kartenspiel",
                    "GDI_2022_M_3_A_3_Medikamenten_Simulation",
                    "GDI_2022_M_3_SA_1_To_Do_Liste",
                    "GDI_2022_M_3_SA_2_Such_und_Sortieralgorithmen",
                    "GDI_2022_M_3_SA_3_1_Auswerten_von_Einzelbasen",
                    "GDI_2022_M_3_SA_3_2_Auswerten_von_Basen_Sequenzen",
                    "GDI_2022_M_3_SA_3_3_Auswerten_einer_Liste_von_Basen_Sequenzen",
                    "GDI_2022_M_3_SA_3_4_Testen_einer_Hypothese_mittels_DNA_Sequenzanalyse"
                    ]

GDI_2022_M_4 = [
                    "GDI_2022_M_4_A_1_Lieferschein",
                    "GDI_2022_M_4_A_2_Simulation_einer_ansteckenden_Krankheit",
                    "GDI_2022_M_4_SA_1_Bowling",
                    "GDI_2022_M_4_SA_2_Erweiterungen_zur_Case_Study",
                    "GDI_2022_M_4_SA_3_Schere_Stein_Papier"
                    ]

GDI_2022_M_5 = [
                    "GDI_2022_M_5_A_1_Erdbebendaten", # TODO: regrade with fixed main_exec
                    "GDI_2022_M_5_SA_1_Wetterstationen" # TODO: regrade with fixed main_exec
                    ]

GDI_2022_M_6 = [
                    "GDI_2022_M_6_A_1_Vektoren",
                    "GDI_2022_M_6_A_2_Matrizen_Boss_Puzzle",
                    "GDI_2022_M_6_A_3_Waermeausbreitung_in_einem_Metallstab", # TODO: regrade with fixed main_exec
                    "GDI_2022_M_6_A_4_Waermeausbreitung_in_einer_Platte", # TODO: regrade with fixed main_exec
                    "GDI_2022_M_6_SA_1_Galton_Board",
                    "GDI_2022_M_6_SA_2_Tic_Tac_Toe",
                    "GDI_2022_M_6_SA_3_Monte_Carlo_Erweiterung_Schere_Stein_Papier"
                    ]

GDI_2022_SEMTEST = [
                    "GDI_2022_SEMTEST_Notenprogramm",
                    "GDI_2022_SEMTEST_Waldbrand"
                    ]

GDI_2022_EXAM = [
                    "GDI_2022_EXAM_SQL_Notenauswertung",
                    "GDI_2022_EXAM_DNA"
                    ]

GDI_2022 = GDI_2022_M_1 + GDI_2022_M_2 + GDI_2022_M_3 + GDI_2022_M_4 + GDI_2022_M_5 + GDI_2022_M_6
GDI_2022_TRY = [project for project in GDI_2022 if "_A_" in project] + [project + "_fixed_main_exec" for project in GDI_2022 if "_A_" in project]
GDI_2022_DO = [project for project in GDI_2022 if "_SA_" in project] + [project + "_fixed_main_exec" for project in GDI_2022 if "_SA_" in project]

GDI_2021_M_1 = [
                    "GDI_2021_M_1_A_1_Temperaturberechnung",
                    "GDI_2021_M_1_A_2_Zeichenketten_und_Variablentausch",
                    "GDI_2021_M_1_A_3_Kreisberechnung",
                    "GDI_2021_M_1_SA_1_Geldautomat",
                    "GDI_2021_M_1_SA_2_Verschluesselung"
                    ]

GDI_2021_M_2 = [
                    "GDI_2021_M_2_A_1_Berechnungsreihe",
                    "GDI_2021_M_2_A_2_Pin_Code",
                    "GDI_2021_M_2_SA_1_Zahlen_raten", # TODO: regrade
                    "GDI_2021_M_2_SA_2_Notenprogramm",
                    "GDI_2021_M_2_SA_3_Pokern"
                    ]

GDI_2021_M_3 = [
                    "GDI_2021_M_3_A_1_Planeten", # TODO: regrade
                    "GDI_2021_M_3_A_2_Kartenspiel",
                    "GDI_2021_M_3_A_3_Medikamenten_Simulation", # TODO: regrade
                    "GDI_2021_M_3_SA_1_To_Do_Liste",
                    "GDI_2021_M_3_SA_2_Such_und_Sortieralgorithmen",
                    "GDI_2021_M_3_SA_3_Bowling",
                    "GDI_2021_M_3_SA_4_1_Simulation_biologischer_Modelle_Teil_1",
                    "GDI_2021_M_3_SA_4_2_Simulation_biologischer_Modelle_Teil_2"
                    ]

GDI_2021_M_4 = [
                    "GDI_2021_M_4_A_1_Lieferschein",
                    "GDI_2021_M_4_A_2_Simulation_einer_ansteckenden_Krankheit",
                    "GDI_2021_M_4_SA_1_Merge_Sort",
                    "GDI_2021_M_4_SA_2_Erweiterungen_zur_Case_Study",
                    "GDI_2021_M_4_SA_3_Schere_Stein_Papier" # TODO: regrade
                    ]

GDI_2021_M_5 = [
                    "GDI_2021_M_5_A_1_Erdbebendaten", # TODO: regrade
                    "GDI_2021_M_5_SA_1_Wetterstationen" # TODO: regrade
                    ]

GDI_2021_M_6 = [
                    "GDI_2021_M_6_A_1_Vektoren", # TODO: regrade
                    "GDI_2021_M_6_A_2_Matrizen_Boss_Puzzle", # TODO: regrade
                    "GDI_2021_M_6_A_3_Waermeausbreitung_in_einem_Metallstab",
                    "GDI_2021_M_6_A_4_Waermeausbreitung_in_einer_Platte",
                    "GDI_2021_M_6_SA_1_Galton_Board", # TODO: regrade
                    "GDI_2021_M_6_SA_2_Tic_Tac_Toe", 
                    "GDI_2021_M_6_SA_3_Monte_Carlo_Erweiterung_Schere_Stein_Papier" # TODO: regrade
                ]

GDI_2021 = GDI_2021_M_1 + GDI_2021_M_2 + GDI_2021_M_3 + GDI_2021_M_4 + GDI_2021_M_5 + GDI_2021_M_6
GDI_2021_TRY = [project for project in GDI_2021 if "_A_" in project]
GDI_2021_DO = [project for project in GDI_2021 if "_SA_" in project]