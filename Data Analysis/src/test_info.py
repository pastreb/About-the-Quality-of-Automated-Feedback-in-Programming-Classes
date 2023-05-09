from enum import Enum
from termcolor import colored # for printing funny colored text

CSV_ERRORS = "Errors"

CSV_TP_PS = "True Positives (Presentation Score)"
CSV_FP_PS = "False Positives (Presentation Score)"
CSV_TN_PS = "True Negatives (Presentation Score)"
CSV_FN_PS = "False Negatives (Presentation Score)"
CSV_PS_COUNTS = [CSV_TP_PS, CSV_TN_PS, CSV_FP_PS, CSV_FN_PS, CSV_ERRORS]

CSV_A_PS = "Accuracy (Presentation Score)"
CSV_R_PS = "Recall (Presentation Score)"
CSV_P_PS = "Precision (Presentation Score)"
CSV_PS_SCORES = [CSV_A_PS, CSV_R_PS, CSV_P_PS]

CSV_TP_ER = "True Positives (Exam Results)"
CSV_FP_ER = "False Positives (Exam Results)"
CSV_TN_ER = "True Negatives (Exam Results)"
CSV_FN_ER = "False Negatives (Exam Results)"
CSV_ER_COUNTS = [CSV_TP_ER, CSV_TN_ER, CSV_FP_ER, CSV_FN_ER, CSV_ERRORS]

CSV_A_ER = "Accuracy (Exam Results)"
CSV_R_ER = "Recall (Exam Results)"
CSV_P_ER = "Precision (Exam Results)"
CSV_ER_SCORES = [CSV_A_ER, CSV_R_ER, CSV_P_ER]

CSV_HEADER = ["Project", "Test", "Submissions", 
              "Successes", "Fails", CSV_ERRORS, "Skips", 
              
              CSV_TP_PS, # test successful, student strong (according to presentation score)
              CSV_FP_PS, # test successful, student weak (according to presentation score)
              CSV_TN_PS, # test unsuccessful, student weak (according to presentation score)
              CSV_FN_PS, # test unsuccesful, student strong (according to presentation score)
              
              CSV_A_PS, # (true positives + true negatives)/submissions (according to presentation score)
              CSV_R_PS, # (true positives)/(true positives + false negatives) (according to presentation score)
              CSV_P_PS, # (true positives)/(true positives + true negatives) (according to presentation score)

              CSV_TP_ER, # test successful, student strong (according to exam results)
              CSV_FP_ER, # test successful, student weak (according to exam results)
              CSV_TN_ER, # test unsuccessful, student weak (according to exam results)
              CSV_FN_ER, # test unsuccesful, student strong (according to exam results)
              
              CSV_A_ER, # (true positives + true negatives)/submissions (according to exam results)
              CSV_R_ER, # (true positives)/(true positives + false negatives) (according to exam results)
              CSV_P_ER # (true positives)/(true positives + true negatives) (according to exam results)
            ]

Score_Metric = Enum("Score_Metric", ["PRESENTATION", "EXAM"])

class TestInfo:
    
    """
    A class to store information about a specific test, including its project and name, number of submissions, and results.

    Attributes
    ----------
    project (str): The name of the project to which the test belongs.
    name (str): The name of the test.
    submissions (int): The total number of submissions for the test.
    
    successes (int): The number of successful submissions for the test.
    fails (int): The number of failed submissions for the test.
    errors (int): The number of erroneous submissions for the test.
    skips (int): The number of skipped submissions for the test.
    
    t_p_p (int): The number of true positives based on the presentation score.
    f_p_p (int): The number of false positives based on the presentation score.
    t_n_p (int): The number of true negatives based on the presentation score.
    f_n_p (int): The number of false negatives based on the presentation score.
    
    accuracy_p (float): The accuracy score based on the presentation score.
    recall_p (float): The recall score based on the presentation score.
    precision_p (float): The precision score based on the presentation score.
    
    t_p_e (int): The number of true positives based on the exam result.
    f_p_e (int): The number of false positives based on the exam result.
    t_n_e (int): The number of true negatives based on the exam result.
    f_n_e (int): The number of false negatives based on the exam result.
    
    accuracy_e (float): The accuracy score based on the exam result.
    recall_e (float): The recall score based on the exam result.
    precision_e (float): The precision score based on the exam result.

    Methods
    -------
    add_submission(result: str, presentation_score: float, exam_result: float) -> None
        Adds a new submission result to the test.
    compute_indicators() -> None
        Computes the presentation score and exam result indicators based on the current results.
    make_row() -> list[str]
        Returns a list of string values that represent the test's information.
    """

    def __init__(self, project : str, name : str) -> None:
        
        """
        Initializes a new TestInfo object with the specified project and name.

        Args:
            project (str): The name of the project to which the test belongs.
            name (str): The name of the test.
        
        Returns:
            None
        """

        # Metadata
        self.project = project
        self.name = name
        # Results
        self.submissions, self.successes, self.fails, self.errors, self.skips = 0, 0, 0, 0, 0
        # True/False Positives/Negatives and Indicators based on Presentation Score
        self.t_p_p, self.f_p_p, self.t_n_p, self.f_n_p = 0, 0, 0, 0
        self.accuracy_p, self.recall_p, self.precision_p = 0, 0, 0
        # True/False Positives/Negatives and Indicators based on Exam Result
        self.t_p_e, self.f_p_e, self.t_n_e, self.f_n_e = 0, 0, 0, 0
        self.accuracy_e, self.recall_e, self.precision_e = 0, 0, 0

    def add_submission(self, result: str, presentation_score: float, exam_result: float) -> None:

        """
        Adds a test submission and updates the metrics based on the given result, presentation score, and exam result.

        Args:
            result (str): The result of the test (Success, Fail, Error, or Skip).
            presentation_score (float): The presentation score for the test submission.
            exam_result (float): The exam result for the test submission.

        Returns:
            None
        """
        
        self.submissions += 1
        if "Success" in result:
            self.successes += 1
            if presentation_score == 1.0: self.t_p_p += 1 
            else: self.f_p_p += 1
            if exam_result >= 0.6: self.t_p_e += 1 
            else: self.f_p_e += 1
        elif "Fail" in result:
            self.fails += 1
            if presentation_score == 1.0: self.f_n_p += 1 
            else: self.t_n_p += 1
            if exam_result >= 0.6: self.f_n_e += 1 
            else: self.t_n_e += 1
        elif "Error" in result: self.errors += 1
        elif "Skip" in result: self.skips += 1
        else: print(colored(f"Unknown test result {result}", "yellow"))
    
    def compute_indicators(self) -> None:

        """
        Computes the presentation score and exam result indicators based on the current results.

        Args:
            None

        Returns:
            None
        """
        
        # Calculate indicators based on presentation score
        self.accuracy_p = (self.t_p_p + self.t_n_p)/self.submissions if self.submissions > 0 else 0
        self.recall_p = self.t_p_p/(self.t_p_p + self.f_n_p) if self.t_p_p + self.f_n_p > 0 else 0
        self.precision_p = self.t_p_p/(self.t_p_p + self.f_p_p) if self.t_p_p + self.f_p_p > 0 else 0
        # Calculate indicators based on exam result
        self.accuracy_e = (self.t_p_e + self.t_n_e)/self.submissions if self.submissions > 0 else 0
        self.recall_e = self.t_p_e/(self.t_p_e + self.f_n_e) if self.t_p_e + self.f_n_e > 0 else 0
        self.precision_e = self.t_p_e/(self.t_p_e + self.f_p_e) if self.t_p_e + self.f_p_e > 0 else 0

    def make_row(self) -> list[str]:

        """
        Returns a list of string values that represent the test's information.

        Args:
            None

        Returns:
            List[str]: A list of string values containing the test's information.
        """

        return [self.project, self.name, self.submissions,
                self.successes, self.fails, self.errors, self.skips,
                self.t_p_p, self.f_p_p, self.t_n_p, self.f_n_p,
                format(self.accuracy_p, '.2f'), format(self.recall_p, '.2f'), format(self.precision_p, '.2f'),
                self.t_p_e, self.f_p_e, self.t_n_e, self.f_n_e,
                format(self.accuracy_e, '.2f'), format(self.recall_e, '.2f'), format(self.precision_e, '.2f')]



class ProjectTestInfo:

    """
    A class that represents information about the test cases for a project.

    Attributes:
    -----------
    project (str): The name of the project.
    n_test_cases (int): The number of test cases for the project.
    test_info (list[TestInfo]): A list containing TestInfo objects for each test case.

    Methods:
    --------
    __check_rows_format(self, rows: list[list[str]]) -> bool
        A private method to check if the format of the rows is correct for adding a submission.
    add_submission(self, rows: list[list[str]]) -> None
        Adds a submission for the project to the list of test cases.
        If the format of the rows is incorrect, the submission is ignored.
    finalize(self) -> list[list[str]]:
        Finalizes the list of test cases and returns the result as a list of lists.
        Each inner list contains the results of a single test case.
    """

    def __init__(self, project : str) -> None:
        
        """
        Initializes a new ProjectTestInfo object with the given project name.
        
        Args:
            project (str): The name of the project to which the test belongs.
        
        Returns:
            None
        """

        self.project = project
        self.n_test_cases = 0
        self.test_info = []

    def __check_rows_format(self, rows : list[list[str]]) -> bool:

        """
        Private method that checks whether the rows representing a submission have the correct format.
        
        Args:
            rows (list[list[str]]): A list of lists of strings representing the rows of a submission.
        
        Returns:
            Boolean: Indicator whether the rows have the correct format.
        """

        try:
            self.n_test_cases = int(rows[0][1])
            if len(rows) == self.n_test_cases+3:
                return "Presentation" in rows[1][0] and "Exam" in rows[2][0] and all("Test" in row[0] for row in rows[3:])
            if len(rows) == 2*self.n_test_cases+3:
                self.n_test_cases *= 2
                return "Presentation" in rows[1][0] and "Exam" in rows[2][0] and all("Test" in row[0] for row in rows[3:3+self.n_test_cases]) and all("fixed_main_exec" in row[0] for row in rows[3+self.n_test_cases:])
        except Exception as e:
            print(colored(f"{type(e)}\n{e.args}\n{e}", "red"))
        return False
            
        
    def add_submission(self, rows : list[list[str]]) -> None:

        """
        Adds the results of a submission to the test information of the project.
        
        Args:
            rows (list[list[str]]): A list of lists of strings representing the rows of a submission.
        
        Returns:
            None
        """
        # Check the row format
        if not self.__check_rows_format(rows):
            print(colored(f"Cannot regognize row format in {self.project}\n{rows}", "red"))
            return
        # Setup self.test_info if this is the first submission
        if not len(self.test_info):
            for i in range(self.n_test_cases):
                self.test_info.append(TestInfo(self.project, rows[3+i][0]))
        # Extract information from rows
        presentation_score = float(rows[1][1])
        exam_result = float(rows[2][1])
        for i in range(self.n_test_cases):
            self.test_info[i].add_submission(rows[3+i][1], presentation_score, exam_result)

    def finalize(self) -> list[list[str]]:

        """
        Computes the indicators for each test case and returns a list of rows representing the test information of the project.
        
        Args:
            None
        
        Returns:
            List[list[str]]: A list of lists of strings representing the test information of the project.
        """
        out = []
        for test in self.test_info:
            test.compute_indicators()
            out.append(test.make_row())
        return out