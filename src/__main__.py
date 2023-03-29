from extract import *

if __name__ == '__main__':
    if os.name == 'nt': os.system("color") # if on Windows we need to activate colored print
    source_directory = os.path.join(os.path.dirname(__file__), "..", "data", "raw_student_data")
    target_directory = os.path.join(os.path.dirname(__file__), "..", "data", "processed_student_data")
    if(os.path.exists(target_directory)):
        print(colored("There is already something at " + target_directory, "yellow"))
        if(input("Delete? (Y/N)") not in ["Yes", "Y", "y", "ye"]):
            exit()
        try:
            shutil.rmtree(target_directory)
        except OSError as error:
            print("Failed to delete directory\n", error)
            exit()
    os.mkdir(target_directory)
    for source_project in os.listdir(source_directory):
        source_project_directory = os.path.join(source_directory, source_project)
        target_project_directory = os.path.join(target_directory, source_project)
        # DONE:
        # APro_2021_M_1A_A_1_Temperaturberechnung
        # APro_2021_M_1A_A_2_Zeichenketten_und_Variablentausch
        # APro_2021_M_1A_A_3_Kreisberechnung
        if os.path.isdir(source_project_directory) and source_project == "GDI_2021_M_6_SA_2_Tic_Tac_Toe_Spiel":
            print("Processing", source_project)
            os.mkdir(target_project_directory)
            extract_project(source_project_directory, target_project_directory)
        elif os.path.isfile(source_project_directory):
            shutil.copy(source_project_directory, target_directory)
    for project in (f.path for f in os.scandir(target_directory) if f.is_dir()): # traverse course projects
        scoreboard_file = os.path.join(target_directory, re.findall("GDI|APro|AIT|SAMPLE", project)[0] + "_" + re.findall("2021|2022|2023", project)[0] + "_" + "Scoreboard.csv")
        student_grades = extract_presentation_grades_from_scoreboard(project, scoreboard_file)
        print(str(collect_student_data_from_project(project, student_grades)).replace(",", "\n"))