## List of Possible Changes to our Current Test-Setting

- Always run tests when program is run:
    - Create `/scripts/run_and_test.sh` with the following content:
        ```bash
        python test_exec.py
        python main.py
        ```
    - Add to `conf.yml`:
        ```yml
        script:
            run: /scripts/run_and_test.sh
        ```
- Add general information on test-run in Console-Tab:
    - Modify `test_exec.py` as follows:
        ```python
        from termcolor import colored
        test_outcomes = list(result._get_info_by_testcase().values())[0]
        total_n_tests = len(test_outcomes)
        successful_n_tests = [test_outcome.outcome for test_outcome in test_outcomes].count(0)
        fail_n_tests = total_n_tests - successful_n_tests
        graphic_test_result = "[" + colored("==="*successful_n_tests, "green") + "   "*fail_n_tests + "] (" + colored(str(successful_n_tests), "green") + "/" + str(total_n_tests) + ")"
        print("Test-Fortschritt:\n", graphic_test_result)
        if(successful_n_tests == total_n_tests):
            print(colored("Super gemacht!", "green"))
        elif(successful_n_tests == total_n_tests-1):
            print(colored("Schaffst du auch den letzten Test-Case noch? :)", "green"))
        elif(successful_n_tests > total_n_tests/2):
            print(colored("Schon mehr als die Hälfte der Test-Cases sind erfolgreich!", "green"))
        elif(successful_n_tests == total_n_tests/2):
            print(colored("Schon die Hälfte der Test-Cases sind erfolgreich!", "green"))
        elif(successful_n_tests > 1):
            print(colored("Einige Test-Cases sind bereits erfolgreich!", "green"))
        elif(successful_n_tests == 1):
            print(colored("Ein erster Test-Case ist erfolgreich!", "green"))
        else:
            print(colored("Schau dir doch mal die Test-Cases an!", "green"))
        general_message = "Weitere Infos findest du im Tab 'Test Results' im unteren Fensterbereich."
        print(general_message)
        print("-"*len(general_message))
        ```
- Add specific information about the first failing test in Console-Tab:
    - Modify `test_exec.py` as follows:
        ```python
        import re
        from termcolor import colored
        test_outcomes = list(result._get_info_by_testcase().values())[0]
        for test_info in test_outcomes:
            if test_info.check_outcome() == test_info.FAILURE:
                if "AssertionError" in test_info.get_error_info(): # "expected" case where some assertion is not valid
                    print(colored(re.findall("Hint:.*", test_info.get_description())[0], "yellow")) # print relevant hint from feedback
                else: # other problems, e.g. syntax errors
                    print(colored("Es scheint allgemeine Probleme mit Ihrem Code zu geben.", "red"))
                    print(colored("Weitere Infos erhalten Sie, wenn Sie versuchen, das Programm via 'Run' auszuführen.", "red"))
                break # print at most one hint
        print("Klicken Sie im unteren Fensterbereich auf das Tab 'Test Results' für das detaillierte Testergebnis.")
        ```
- Subtests & Location:
    - Modify `test_cases.py` as follows (example test case with subtest):
        ```python
        @util.timeout(0.5)
        @unittest.mock.patch('builtins.input', side_effect=input_list)
        def test_a(self, mocked_input, mocked_stdout):
            """ Teste, ob die Funktion "setup" existiert.
                Hint: Definieren Sie eine Funktion mit dem Namen "setup" mit einem Parameter (das Spielbrett).
                Location: Funktion "setup"."""
            if 'main' in sys.modules:
                del sys.modules["main"]
            import main
            with self.subTest("Die Funktion \"setup\" existiert."):
                assert "setup" in dir(main), "Es scheint, als würden Sie keine Funktion \"setup\" definieren."
            with self.subTest("Die Funktion \"setup\" erwartet einen Parameter."):
                assert "setup" in dir(main), "Es scheint, als würden Sie keine Funktion \"setup\" definieren." # do this again otherwise this subtest prints the error given by python
                n_params = len(signature(main.setup).parameters)
                assert n_params == 1, "Die Funktion \"setup\" muss 1 Parameter entgegennehmen, aktuell erwartet sie aber " + str(n_params) + " Parameter."
        ```
- Shorter Error Messages (based on Edit Distance) and slightly clearer Test Output:
    - Add to `utillib.py`:
        ```python
        # Find minimum number operations to convert s1 to s2
        def find_edit_distance(s1, s2):
        n = len(s1)
        m = len(s2)
        prev = [j for j in range(m+1)]
        curr = [0] * (m+1)
        for i in range(1, n+1):
            curr[0] = i
            for j in range(1, m+1):
            if s1[i-1] == s2[j-1]:
                curr[j] = prev[j-1]
            else:
                mn = min(1 + prev[j], 1 + curr[j-1])
                curr[j] = min(mn, 1 + prev[j-1])
            prev = curr.copy()
        return prev[m]
        ```
    - Modify class `Testcase` in `tap_test_runner.py` follows:
        ```python
        ## [2.14] Added is_input_test to return in that case "Dein Input..." instead of "Dein Output..."
        ## [2.13] Added get_clean_errormessage to reduce the non-relevant output in failing test cases

        class Testcase():
            # [...]
            is_input_test = False
            # [...]

        def __init__(self, pattern, haystack, hint=None):
            # [...]
            if(isinstance(haystack, unittest.mock.MagicMock)):
                # [...]
                self.is_input_test = True
            # [...]
        ```
    - Modify function `get_errormessage` in `tap_test_runner.py` as follows:
        ```python
        def get_clean_errormessage(self): # tries to identify the relevant (wrong) line in self.seen
            if(self.hint != ""):
                best_candidate = ""
                best_candidate_edit_distance = len(self.seen)
                for line in self.seen.split("\n"): # consider edit distance between line and self.hint
                    next_edit_distance = find_edit_distance(line, self.hint)
                    if next_edit_distance < best_candidate_edit_distance:
                        best_candidate = line
                        best_candidate_edit_distance = next_edit_distance
                if "call" in best_candidate: # if we are checking the input then we want to remove the "[call('...')]" around the relevant "..."
                    try:
                        best_candidate = re.findall("\'.*\'", best_candidate)[0][1:-1]
                    except:
                        pass
                if best_candidate_edit_distance > len(self.hint)/2: # prevent "totally false matches"
                    best_candidate = ""
                if self.is_input_test:
                    return "Relevanter Ausschnitt aus deinem Input:\n```text\n" + best_candidate + "\n```\nErwarteter Input:\n```text\n" + self.hint + "\n```"
                else:
                    return "Relevanter Ausschnitt aus deinem Output:\n```text\n" + best_candidate + "\n```\nErwarteter Output:\n```text\n" + self.hint + "\n```"
            else:
            return get_errormessage(self)
        ``` 
- Generally Mock Plots (to speed up tests):
    ```python
    with unittest.mock.patch('matplotlib.pyplot.show') and unittest.mock.patch('matplotlib.pyplot.savefig'):
    [...]
    ```
- Use contents from `main.py` (e.g. variables or functions) in `test_cases.py`:
    ```python
    if 'main' in sys.modules:  
      del sys.modules["main"]
    import main
    assert "size" in dir(main), "Du definierst keine Variable \"size\", welche existieren und die Grösse des Spielfelds steuern soll"
    assert main.size == 7, "Die Grösse des Spielfelds sollte 7 sein, deine Variable \"size\" hat aber den Wert " + str(main.size)
    ```
- Add specific information on test-run in Console-Tab if there are multiple parts of test-sets:
    ```python
    test_outcomes = list(result._get_info_by_testcase().values())[0]
    total_n_tests = len(test_outcomes)
    successful_n_tests = [test_outcome.outcome for test_outcome in test_outcomes].count(0)
    teil_1 = test_outcomes[0:4]
    teil_2 = test_outcomes[4:8]
    teil_3 = test_outcomes[8:]
    teil_1_successful = False not in [(test.outcome == 0) for test in teil_1]
    teil_2_successful = False not in [(test.outcome == 0) for test in teil_2]
    teil_3_successful = False not in [(test.outcome == 0) for test in teil_3]
    if(successful_n_tests == total_n_tests):
        print(colored("Super gemacht!", "green"))
    elif teil_1_successful and teil_2_successful:
        print(colored("Teile 1 und 2 abgeschlossen! Schaffst du auch Teil 3 noch? :)", "green"))
    elif teil_1_successful and 0 in teil_2:
        print(colored("Teil 1 abgeschlossen und auch mit Teil 2 gehts vorwärts!", "green"))
    elif teil_1_successful:
        print(colored("Teil 1 abgeschlossen! Schaffst du auch Teil 2? :)", "green"))
    elif 0 in teil_1:
        print(colored("Ein erster Test-Case ist erfolgreich!", "green"))
    else:
        print(colored("Schau dir doch mal die Test-Cases an!", "green"))
    ```
- Example for checking and getting a function in a Test Case:
    ```python
    def check_and_get_palindrome_function(self):
        # If a (patched) module is loaded, delete it
        if 'main' in sys.modules:  
        del sys.modules["main"]
        import main
        if "is_palindrome" in dir(main):
        n_params = len(signature(main.is_palindrome).parameters)
        assert n_params == 1, "Die Funktion \"is_palindrome\" soll 1 Parameter entgegennehmen, aktuell erwartet sie aber " + str(n_params) + " Parameter"
        ret = main.is_palindrome("dummy")
        assert ret in [True, False], "Die Funktion \"is_palindrome\" soll immer einen Boolean (True oder False) zurückgeben, für den Input \"dummy\" gibt sie aber " + str(ret) + " zurück"
        return main.is_palindrome # if we reach this we have successfully tested the signature of is_palindrome
        for element in dir(main): # if the function has another name, we try to find it as well
        if find_edit_distance("palindrom", element) <= abs(len("palindrom") - len(element)) + 1:
            n_params = len(signature(getattr(main, element)).parameters)
            assert n_params == 1, "Die Funktion " + element + " soll 1 Parameter entgegennehmen, aktuell erwartet sie aber " + str(n_params) + " Parameter"
            ret = getattr(main, element)("dummy")
            assert ret in [True, False], "Die Funktion " + element + " soll immer einen Boolean (True oder False) zurückgeben, für den Input \"dummy\" gibt sie aber " + str(ret) + " zurück"
            return getattr(main, element) # if we reach this we have successfully tested the signature of some palindrome function
        assert False, "Du scheinst keine Funktion zu definieren, welche die Spezifikationen erfüllt"
        return None
    ```