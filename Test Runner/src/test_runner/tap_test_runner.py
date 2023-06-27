## Testrunner - Python
## Version 2.1
## Authors: Oliver Probst, Nicole Wenzinger, Antoine Suter, Markus Dahinden
## Maintainer: Markus Dahinden
## Changelog:
## [2.12] Optimized Output when no solution hint should be given
## [2.11] Add codeblock and optional output-hint
## [2.1] Add subtests, improve multiline support
## [2.02] Improve Sanitize yml-Error Output (Bail out!, not ok, ok, ---)
## [2.01] Sanitize yml-Error Output (...)
## [2.0] Optimized writing of testcases (class Testcase() added)
## [1.9] switched to tap output

import io
import sys
import time
from datetime import datetime

from unittest import TextTestRunner
import unittest
from test_runner.tap_test_result import TapTestResult

import re


UTF8 = "UTF-8"

class Testcase():
  pattern = ""
  seen = ""
  expected = ""
  result = False
  hint = ""
  
  def __init__(self, pattern, haystack, hint=None):
    self.pattern = pattern
    if(hint == None):
      self.hint = self.make_pretty(self.pattern)
    else:  
      self.hint = hint
      
    if(isinstance(haystack, unittest.mock.MagicMock)):
      self.seen = str(haystack.call_args_list).replace("[]", "")
    elif(isinstance(haystack, io.StringIO)):
      self.seen = self.sanitize_tap_yml(haystack.getvalue())
    elif(isinstance(haystack, str)):
      self.seen = self.sanitize_tap_yml(haystack)
    else:
      exit("Wrong type of haystack! Type is: " + str(type(haystack)))
    self.result = self.validate()
    
  def sanitize_tap_yml(self, txt):
    return txt.replace("...", ". . .")    \
              .replace("---", "- - -")    \
              .replace("Bail out!", "Bail out")
    
  def validate(self, ignorecase=True):
    if(ignorecase):
      result = re.search(self.pattern, self.seen, re.IGNORECASE | re.MULTILINE | re.DOTALL)
    else:
      result = re.search(self.pattern, self.seen, re.MULTILINE | re.DOTALL)
    return result
  
  def get_errormessage(self):
    if(self.hint != ""):
      return "Dein Output:\n```text\n" + self.seen + "\n```\nErwarteter Output:\n```text\n" + self.hint + "\n```"
    else:
      return "Dein Output:\n```text\n" + self.seen + "```"
    
  def make_pretty(self,string):
    return string.replace("(.|\\n)*", "\n") \
                 .replace("(","'")        \
                 .replace(")","'")        \
                 .replace("|","' oder '") \
                 .replace("^","")         \
                 .replace("$","")         \
                 .replace(".?","")        \
                 .replace(".*"," ")       \
                 .replace(".+"," ")       \
                 .replace("!?","!")       \
                 .replace("\??","?")      \
                 .replace("\s+"," ")      \
                 .replace("\s?","")       \
                 .replace(":?","")        \
                 .replace("\[", "[")      \
                 .replace("\]", "]")      \
                 .replace("\\","")


class TimeoutError(Exception):
    pass


class TapTestRunner(TextTestRunner):
    """" A test runner class that output the results. """

    time_format = "%Y-%m-%d_%H-%M-%S"

    def __init__(self, output="./reports/", verbosity=2, stream=sys.stderr,
                 descriptions=True, failfast=False, buffer=False,
                 report_name=None, add_timestamp=True):
        self.verbosity = verbosity
        self.output = output
        self.encoding = UTF8

        TextTestRunner.__init__(self, stream, descriptions, verbosity,
                                failfast=failfast, buffer=buffer)

        if add_timestamp:
            self.timestamp = time.strftime(self.time_format)
        else:
            self.timestamp = ""

        self.resultclass = TapTestResult
        self.report_name = report_name

        self.start_time = 0
        self.time_taken = 0

    def _make_result(self):
        """ Create a TestResult object which will be used to store
        information about the executed tests. """
        return self.resultclass(self.stream, self.descriptions, self.verbosity)

    def run(self, test):
        """ Runs the given testcase or testsuite. """
        try:

            result = self._make_result()
            result.failfast = self.failfast
            if hasattr(test, 'properties'):
                # junit testsuite properties
                result.properties = test.properties

            # self.stream.writeln()
            # self.stream.writeln("Running tests... ")
            # self.stream.writeln(result.separator2)

            self.start_time = time.process_time()
            test(result)
            stop_time = time.process_time()
            self.time_taken = stop_time - self.start_time

            result.printErrors()
            # self.stream.writeln(result.separator2)
            run = result.testsRun
            # self.stream.writeln("Ran {} test{} in {}".format(run, run != 1 and "s" or "", str(self.time_taken)[:7]))
            # self.stream.writeln()

            expectedFails = len(result.expectedFailures)
            unexpectedSuccesses = len(result.unexpectedSuccesses)
            skipped = len(result.skipped)

            infos = []
            if not result.wasSuccessful():
                # self.stream.writeln("FAILED")
                failed, errors = map(len, (result.failures, result.errors))
                if failed:
                    infos.append("Failures={0}".format(failed))
                if errors:
                    infos.append("Errors={0}".format(errors))
            # else:
            #   self.stream.writeln("OK")

            if skipped:
                infos.append("Skipped={}".format(skipped))
            if expectedFails:
                infos.append("Expected Failures={}".format(expectedFails))
            if unexpectedSuccesses:
                infos.append("Unexpected Successes={}".format(
                    unexpectedSuccesses))

            # if infos:
            #    self.stream.writeln(" ({})".format(", ".join(infos)))
            # else:
            #    self.stream.writeln("\n")

            # self.stream.writeln()
            # self.stream.writeln('Generating HTML reports... ')
            result.generate_reports(self)

        finally:
            pass
        return result