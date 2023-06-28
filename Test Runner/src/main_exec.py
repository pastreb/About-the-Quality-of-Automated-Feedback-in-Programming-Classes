import os
from importlib.machinery import SourceFileLoader

path_to_main = ""


def main_exec():
    return SourceFileLoader("main", os.path.join(path_to_main, "main.py")).load_module()
