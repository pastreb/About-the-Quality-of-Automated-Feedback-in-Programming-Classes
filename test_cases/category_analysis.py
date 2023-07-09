import csv
import random as rd

class Testcase:

    def __init__(self, course, module_number, project_name, project_type, test_case_number) -> None:
        self.course = course
        self.module_number = module_number
        self.project_name = project_name
        self.project_type = project_type
        self.test_case_number = test_case_number
        self.categories = set()

    def __str__(self):
        return f"{self.course} {self.module_number} {self.project_name} {self.project_type} {self.test_case_number}"
    
    def belongs_to_category(self, category):
        return category in self.categories

    def add_category(self, category):
        if self.belongs_to_category(category):
            print(f"Duplicated test case \"{self.__str__()}\" in category {category}")
        self.categories.add(category)

    def get_categories(self):
        return self.categories

    def __eq__ (self, other):
        return self.__str__() == other.__str__()

    def __ne__ (self, other):
        return not self.__eq__(other)

def check_issues(test_cases):

    print("\nChecking Potential Issues:")
    for test_case in test_cases:
        
        test_case = test_cases[test_case]

        if not test_case.belongs_to_category("Explicit Correctness Check") and not test_case.belongs_to_category("Implicit Correctness Check"):
            print(f"{str(test_case)} seems to have been forgotten w.r.t. Correctness Check")
        if test_case.belongs_to_category("Explicit Correctness Check") and test_case.belongs_to_category("Implicit Correctness Check"):
            print(f"{str(test_case)} seems to be both explicit and implicit")

        if not test_case.belongs_to_category("Black Box Testing") and not test_case.belongs_to_category("White Box Testing"):
            print(f"{str(test_case)} seems to have been forgotten w.r.t. Visibility")
        if test_case.belongs_to_category("Black Box Testing") and test_case.belongs_to_category("White Box Testing"):
            print(f"{str(test_case)} seems to be both blackbox and whitebox")
        
        if not test_case.belongs_to_category("Relevant Side Effect") and not test_case.belongs_to_category("Non-Relevant Side Effect") and not test_case.belongs_to_category("No Side Effect"):
            print(f"{str(test_case)} seems to have been forgotten w.r.t. Side Effect")
        if test_case.belongs_to_category("Relevant Side Effect") and test_case.belongs_to_category("Non-Relevant Side Effect"):
            print(f"{str(test_case)} seems to be both relevant and non-relevant")
        if (test_case.belongs_to_category("Relevant Side Effect") or test_case.belongs_to_category("Non-Relevant Side Effect")) and test_case.belongs_to_category("No Side Effect"):
            print(f"{str(test_case)} seems to have a side effect but also not")

        if not test_case.belongs_to_category("Dynamic Feedback") and not test_case.belongs_to_category("Static Feedback"):
            print(f"{str(test_case)} seems to have been forgotten w.r.t. Feedback Type")
        if test_case.belongs_to_category("Dynamic Feedback") and test_case.belongs_to_category("Static Feedback"):
            print(f"{str(test_case)} seems to have both dynamic and static feedback")

        if not test_case.belongs_to_category("Informative Feedback") and not test_case.belongs_to_category("Corrective Feedback") and not test_case.belongs_to_category("Suggestive Feedback"):
            print(f"{str(test_case)} seems to have been forgotten w.r.t. Feedback Purpose")
        if test_case.belongs_to_category("Informative Feedback") and test_case.belongs_to_category("Corrective Feedback"):
            print(f"{str(test_case)} seems to have both informative and corrective feedback")
        if test_case.belongs_to_category("Informative Feedback") and test_case.belongs_to_category("Suggestive Feedback"):
            print(f"{str(test_case)} seems to have both informative and suggestive feedback")
        if test_case.belongs_to_category("Corrective Feedback") and test_case.belongs_to_category("Suggestive Feedback"):
            print(f"{str(test_case)} seems to have both corrective and suggestive feedback")

    print("DONE\n")

def read_test_cases(filename):

    test_cases = {} # maps string representations to test case objects collecting categories
    categories = {} # maps categories to counts
    assignments = set()

    with open(filename, 'r') as file:
        reader = csv.reader(file, delimiter=";", quotechar='"', quoting=csv.QUOTE_MINIMAL, lineterminator="\n",)
        header = next(reader)
        for row in reader:

            super_category = row[0]
            category = row[1]
            test_case = Testcase(row[2], row[3], row[4], row[5], row[6])

            if str(test_case) not in test_cases: # did not yet encounter this test case
                test_cases[str(test_case)] = test_case
            test_cases[str(test_case)].add_category(category)

            if category in categories:
                categories[category] += 1
            else:
                categories[category] = 1

            assignments.add(f"{test_case.course} {test_case.project_name}")
        
        print(f"Scanned {len(assignments)} assignments")
    
    return test_cases, categories

def find_representative_test_cases(test_cases, categories):

    rd.seed(42)

    print("Looking for a small set of representative test cases...")
    while(True):

        working_set_of_chosen_test_cases = True

        remaining_categories = set(categories.keys())
        remaining_categories.remove("Fast")
        remaining_categories.remove("Input Call Count")
        chosen_test_cases = {}
        test_case_categories = {}
        projects_to_be_included = {"Geldautomat", "Such Sort", "Hotel", "Palindrom"}
        projects_to_ignore = {"Todo", "Bio 2", "Pandemie", "Vier Gewinnt", "Schere Stein Papier Erweiterung", "Wetterstationen"}
        
        while len(remaining_categories) > 0:
            
            max_intersection = set()
            max_intersection_test_case = None

            keys = list(test_cases.keys())
            rd.shuffle(keys)

            for test_case in keys:

                test_case = test_cases[test_case]

                if "2022" not in test_case.course or "SA" != test_case.project_type:
                    continue # we wanna consider DIY projects in the most recent iterations
                
                if any(chosen_test_cases[chosen_test_case].project_name == test_case.project_name for chosen_test_case in chosen_test_cases) and test_case.project_name not in projects_to_be_included:
                    continue # have each project at most once
                
                if any(project in test_case.project_name for project in projects_to_ignore):
                    continue # some projects are not suited
                
                intersection = test_case.get_categories().intersection(remaining_categories)

                if (len(intersection) > len(max_intersection)):

                    max_intersection = intersection
                    max_intersection_test_case = test_case

            if len(max_intersection) == 0:
                # print("Could not find a suitable set of test cases that satisfies all requirements.")
                working_set_of_chosen_test_cases = False
                break
                
            chosen_test_cases[str(max_intersection_test_case)] = max_intersection_test_case
            test_case_categories[str(max_intersection_test_case)] = max_intersection
            
            for category in max_intersection_test_case.get_categories():
                if category in remaining_categories:
                    remaining_categories.remove(category)

        if working_set_of_chosen_test_cases and len(chosen_test_cases) <= 10 and all(any(project_to_be_included in test_case for test_case in chosen_test_cases) for project_to_be_included in projects_to_be_included):    
            print(f"\nChosen Testcases ({len(chosen_test_cases)}):")
            for test_case in sorted(chosen_test_cases.keys()):
                print(f"{str(test_case)} ({test_case_categories[test_case]})")
            print()
            break


def main():
        filename = "all_categories.csv"
        
        test_cases, categories = read_test_cases(filename)
        
        check_issues(test_cases)
        
        find_representative_test_cases(test_cases, categories)

        for category in categories:
            print(f"{category}: {categories[category]}/{len(test_cases)}")

main()