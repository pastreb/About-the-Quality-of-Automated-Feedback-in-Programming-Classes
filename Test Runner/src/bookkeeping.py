import os
import re
import sys

SOURCE_DIRECTORY = os.path.join(
    os.path.dirname(os.path.realpath(sys.argv[0])),
    "..",
    "..",
    "data",
    "raw_student_data",
)
TARGET_DIRECTORY = os.path.join(
    os.path.dirname(os.path.realpath(sys.argv[0])),
    "..",
    "..",
    "data",
    "processed_student_data",
)
TEST_CASES_DIRECTORY = os.path.join(
    os.path.dirname(os.path.realpath(sys.argv[0])), "..", "..", "Test Cases"
)
# os.path.dirname(os.path.realpath(sys.argv[0])) is an alternative approach for obtaining the directory path of the current script

COURSE_PREFIXES = ["GDI", "APRO", "AIT", "SAMPLE"]
YEARS = ["2020", "2021", "2022", "2023"]

SAMPLE = ["SAMPLE_2023_M_1_Test"]

GDI_2022_M_1 = [
    "GDI_2022_M_1_A_1_Hello",
    "GDI_2022_M_1_A_2_Temperaturberechnung",
    "GDI_2022_M_1_A_3_Zeichenketten",
    "GDI_2022_M_1_A_4_Kreisberechnung",
    "GDI_2022_M_1_SA_1_Geldautomat",
    "GDI_2022_M_1_SA_2_Verschluesselung",
]

GDI_2022_M_2 = [
    "GDI_2022_M_2_A_1_Berechnungsreihe",
    "GDI_2022_M_2_A_2_Pin",
    "GDI_2022_M_2_SA_1_Raten",
    "GDI_2022_M_2_SA_2_Noten",
    "GDI_2022_M_2_SA_3_Pokern",
]

GDI_2022_M_3 = [
    "GDI_2022_M_3_A_1_Karten",
    "GDI_2022_M_3_A_2_Medikamente",
    "GDI_2022_M_3_SA_1_Todo",
    "GDI_2022_M_3_SA_2_Such_Sort",
    "GDI_2022_M_3_SA_3_1_DNA_1",
    "GDI_2022_M_3_SA_3_2_DNA_2",
    "GDI_2022_M_3_SA_3_3_DNA_3",
    "GDI_2022_M_3_SA_3_4_DNA_4",
]

GDI_2022_M_4 = [
    "GDI_2022_M_4_A_1_Lieferschein",
    "GDI_2022_M_4_A_2_Pandemie",
    "GDI_2022_M_4_SA_1_Bowling",
    "GDI_2022_M_4_SA_2_Pandemie_Erweiterung",
    "GDI_2022_M_4_SA_3_Schere_Stein_Papier",
]

GDI_2022_M_5 = [
    "GDI_2022_M_5_A_1_Erdbeben",
    "GDI_2022_M_5_SA_1_Wetterstationen",
]

GDI_2022_M_6 = [
    "GDI_2022_M_6_A_1_Vektoren",
    "GDI_2022_M_6_A_2_Matrizen",
    "GDI_2022_M_6_A_3_Waermestab",
    "GDI_2022_M_6_A_4_Waermeplatte",
    "GDI_2022_M_6_SA_1_Galton",
    "GDI_2022_M_6_SA_2_Tic_Tac_Toe",
    "GDI_2022_M_6_SA_3_Schere_Stein_Papier_Erweiterung",
]

GDI_2022_EXAM = [
    # "GDI_2022_EXAM_DNA", # TODO: include in __get_scores_for_export
    # "GDI_2022_EXAM_Noten", # TODO: include in __get_scores_for_export
    # "GDI_2022_EXAM_SQL", # TODO: include in __get_scores_for_export
    # "GDI_2022_EXAM_Waldbrand" # TODO: include in __get_scores_for_export
]

GDI_2022 = (
    GDI_2022_M_1
    + GDI_2022_M_2
    + GDI_2022_M_3
    + GDI_2022_M_4
    + GDI_2022_M_5
    + GDI_2022_M_6
    + GDI_2022_EXAM
)
GDI_2022_TRY = [project for project in GDI_2022 if "_A_" in project] + [
    project + "_fixed_main_exec" for project in GDI_2022 if "_A_" in project
]
GDI_2022_DO = [project for project in GDI_2022 if "_SA_" in project] + [
    project + "_fixed_main_exec" for project in GDI_2022 if "_SA_" in project
]

GDI_2021_M_1 = [
    "GDI_2021_M_1_A_1_Temperaturberechnung",
    "GDI_2021_M_1_A_2_Zeichenketten",
    "GDI_2021_M_1_A_3_Kreisberechnung",
    "GDI_2021_M_1_SA_1_Geldautomat",
    "GDI_2021_M_1_SA_2_Verschluesselung",
]

GDI_2021_M_2 = [
    "GDI_2021_M_2_A_1_Berechnungsreihe",
    "GDI_2021_M_2_A_2_Pin",
    "GDI_2021_M_2_SA_1_Raten",
    "GDI_2021_M_2_SA_2_Noten",
    "GDI_2021_M_2_SA_3_Pokern",
]

GDI_2021_M_3 = [
    "GDI_2021_M_3_A_1_Karten",
    "GDI_2021_M_3_A_2_Medikamente",
    "GDI_2021_M_3_SA_1_Todo",
    "GDI_2021_M_3_SA_2_Such_Sort",
    "GDI_2021_M_3_SA_3_Bowling",
    "GDI_2021_M_3_SA_4_1_Bio_1",
    "GDI_2021_M_3_SA_4_2_Bio_2",
]

GDI_2021_M_4 = [
    "GDI_2021_M_4_A_1_Lieferschein",
    "GDI_2021_M_4_A_2_Pandemie",
    "GDI_2021_M_4_SA_1_Merge_Sort",
    "GDI_2021_M_4_SA_2_Pandemie_Erweiterung",
    "GDI_2021_M_4_SA_3_Schere_Stein_Papier",
]

GDI_2021_M_5 = ["GDI_2021_M_5_A_1_Erdbeben", "GDI_2021_M_5_SA_1_Wetterstationen"]

GDI_2021_M_6 = [
    "GDI_2021_M_6_A_1_Vektoren",
    "GDI_2021_M_6_A_2_Matrizen",
    "GDI_2021_M_6_A_3_Waermestab",
    "GDI_2021_M_6_A_4_Waermeplatte",
    "GDI_2021_M_6_SA_1_Galton",
    "GDI_2021_M_6_SA_2_Tic_Tac_Toe",
    "GDI_2021_M_6_SA_3_Schere_Stein_Papier_Erweiterung",
]

GDI_2021 = (
    GDI_2021_M_1
    + GDI_2021_M_2
    + GDI_2021_M_3
    + GDI_2021_M_4
    + GDI_2021_M_5
    + GDI_2021_M_6
)
GDI_2021_TRY = [project for project in GDI_2021 if "_A_" in project]
GDI_2021_DO = [project for project in GDI_2021 if "_SA_" in project]

APRO_2022_M_1 = [
    "APRO_2022_M_1A_A_1_Temperaturberechnung",  # TODO: check
    "APRO_2022_M_1A_A_2_Zeichenketten",  # TODO: check
    "APRO_2022_M_1A_A_3_Kreisberechnung",  # TODO: check
    "APRO_2022_M_1A_SA_1_Geldautomat",  # TODO: check
    "APRO_2022_M_1A_SA_2_Verschluesselung",  # TODO: check
    "APRO_2022_M_1B_A_1_Berechnungsreihe",  # TODO: check
    "APRO_2022_M_1B_A_2_Pin",  # TODO: check
    "APRO_2022_M_1B_SA_1_Raten",  # TODO: check
    "APRO_2022_M_1B_SA_2_Noten",  # TODO: check
    "APRO_2022_M_1B_SA_2_Pokern",  # TODO: check
]

APRO_2022_M_2 = [
    "APRO_2022_M_2_A_1_Karten",  # TODO: check
    "APRO_2022_M_2_A_2_Medikamente",  # TODO: check
    "APRO_2022_M_2_SA_1_Todo",  # TODO: check
    "APRO_2022_M_2_SA_2_Such_Sort",  # TODO: check
    "APRO_2022_M_2_SA_3_Bowling",  # TODO: check
    "APRO_2022_M_2_SA_4_1_Bio_1",  # TODO: check
    "APRO_2022_M_2_SA_4_2_Bio_2",  # TODO: check
]

APRO_2022_M_3 = [
    "APRO_2022_M_3_A_1_Lieferschein",  # TODO: check
    "APRO_2022_M_3_A_2_Pandemie",  # TODO: check
    "APRO_2022_M_3_SA_1_Merge_Sort",  # TODO: check
    "APRO_2022_M_3_SA_2_Pandemie_Erweiterung",  # TODO: check
    "APRO_2022_M_3_SA_3_Schere_Stein_Papier",  # TODO: check
]

APRO_2022_M_4 = [
    "APRO_2022_M_4_A_1_Vektoren",  # TODO: check
    "APRO_2022_M_4_A_2_Matrizen",  # TODO: check
    "APRO_2022_M_4_A_3_Waermestab",  # TODO: check
    "APRO_2022_M_4_A_4_Waermeplatte",  # TODO: check
    "APRO_2022_M_4_SA_1_Galton",  # TODO: check
    "APRO_2022_M_4_SA_2_Tic_Tac_Toe",  # TODO: check
    "APRO_2022_M_4_SA_3_Schere_Stein_Papier_Erweiterung",  # TODO: check
]

APRO_2022_M_5 = [
    "APRO_2022_M_5_A_1_Meerestiere",  # TODO: check
    "APRO_2022_M_5_SA_1_Hotel",
    "APRO_2022_M_5_SA_2_Erdbeben",  # TODO: check
]

APRO_2022_M_6 = [
    "APRO_2022_M_6_SA_1_Vier_Gewinnt",  # TODO: check
]

APRO_2022 = (
    APRO_2022_M_1
    + APRO_2022_M_2
    + APRO_2022_M_3
    + APRO_2022_M_4
    + APRO_2022_M_5
    + APRO_2022_M_6
)
APRO_2022_TRY = [project for project in APRO_2022 if "_A_" in project]
APRO_2022_DO = [project for project in APRO_2022 if "_SA_" in project]

APRO_2021_M_1 = [
    "APRO_2021_M_1A_A_1_Temperaturberechnung",  # TODO: check
    "APRO_2021_M_1A_A_2_Zeichenketten",  # TODO: check
    "APRO_2021_M_1A_A_3_Kreisberechnung",  # TODO: check
    "APRO_2021_M_1A_SA_1_Geldautomat",  # TODO: check
    "APRO_2021_M_1A_SA_2_Verschluesselung",  # TODO: check
    "APRO_2021_M_1B_A_1_Berechnungsreihe",  # TODO: check
    "APRO_2021_M_1B_A_2_Pin",  # TODO: check
    "APRO_2021_M_1B_SA_1_Raten",  # TODO: check
    "APRO_2021_M_1B_SA_2_Noten",  # TODO: check
    "APRO_2021_M_1B_SA_2_Pokern",  # TODO: check
]

APRO_2021_M_2 = [
    "APRO_2021_M_2_A_1_Karten",  # TODO: check
    "APRO_2021_M_2_A_2_Medikamente",  # TODO: check
    "APRO_2021_M_2_SA_1_Bowling",  # TODO: check
    "APRO_2021_M_2_SA_2_Such_Sort",  # TODO: check
    "APRO_2021_M_2_SA_3_1_Bio_1",  # TODO: check
    "APRO_2021_M_2_SA_3_2_Bio_2",  # TODO: check
]

APRO_2021_M_3 = [
    "APRO_2021_M_3_A_1_Lieferschein",  # TODO: check
    "APRO_2021_M_3_A_2_Pandemie",  # TODO: check
    "APRO_2021_M_3_SA_1_Bubble_Sort",  # TODO: check
    "APRO_2021_M_3_SA_2_Pandemie_Erweiterung",  # TODO: check
    "APRO_2021_M_3_SA_3_Schere_Stein_Papier",  # TODO: check
]

APRO_2021_M_4 = [
    "APRO_2021_M_4_A_1_Vektoren",  # TODO: check
    "APRO_2021_M_4_A_2_Matrizen",  # TODO: check
    "APRO_2021_M_4_A_3_Waermestab",  # TODO: check
    "APRO_2021_M_4_A_4_Waermeplatte",  # TODO: check
    "APRO_2021_M_4_SA_1_Galton",  # TODO: check
    "APRO_2021_M_4_SA_2_Geburtstagsparadoxon",  # TODO: check
]

APRO_2021_M_5 = [
    "APRO_2021_M_5_A_1_Meerestiere",  # TODO: check
    "APRO_2021_M_5_SA_1_Hotel",  # TODO: check
    "APRO_2021_M_5_SA_2_Erdbeben",  # TODO: check
]

APRO_2021_M_6 = [
    "APRO_2021_M_6_SA_1_Grundspiel",  # TODO: check
    "APRO_2021_M_6_SA_2_Gegenspieler",  # TODO: check
    "APRO_2021_M_6_SA_3_Kroenchenaufgabe",  # TODO: check
]

APRO_2021 = (
    APRO_2021_M_1
    + APRO_2021_M_2
    + APRO_2021_M_3
    + APRO_2021_M_4
    + APRO_2021_M_5
    + APRO_2021_M_6
)
APRO_2021_TRY = [project for project in APRO_2021 if "_A_" in project]
APRO_2021_DO = [project for project in APRO_2021 if "_SA_" in project]

APRO_2023_M_1 = ["APRO_2023_M_1A_A_1_Temperaturberechnung"]

APRO_2023 = APRO_2023_M_1
APRO_2023_TRY = [project for project in APRO_2023 if "_A_" in project]
APRO_2023_DO = [project for project in APRO_2023 if "_SA_" in project]

CHOSEN = [
    # "APRO_2022_M_2_SA_4_1_Bio_1",
    "APRO_2022_M_5_SA_1_Hotel",
    # "GDI_2022_M_1_SA_1_Geldautomat",
    # "GDI_2022_M_3_SA_2_Such_Sort",
    # "GDI_2022_M_4_SA_3_Schere_Stein_Papier",
    # "GDI_2022_M_6_SA_1_Galton",
    # "GDI_2022_M_6_SA_2_Tic_Tac_Toe",
    # "GDI_2022_EXAM_Palindrom",
    # "GDI_2022_EXAM_SQL",
]


def extract_name_from_project(project):
    course_prefixes = "|".join(COURSE_PREFIXES)
    years = "|".join(YEARS)
    regex = f"(?:{course_prefixes})_(?:{years})_M_\d*_(?:A|SA)_\d*_*\d*_*"
    project_metadata = re.findall(regex, project)
    return (
        project.replace(project_metadata[0], "")
        if len(project_metadata) == 1
        else project
    )
