import ast
import astunparse
import io
import os
import sys
from importlib.machinery import SourceFileLoader

path_to_main = ""


def export_functions_and_classes():
    with open(os.path.join(path_to_main, "main.py"), "r") as file:
        tree = ast.parse(file.read())
        relevant_parts = []
        for node in ast.iter_child_nodes(tree):
            if isinstance(node, ast.FunctionDef) or isinstance(node, ast.ClassDef):
                relevant_parts.append(node)
        with open(os.path.join(path_to_main, "temp_main.py"), "w") as file:
            for part in relevant_parts:
                file.write(astunparse.unparse(part))
        return SourceFileLoader(
            "temp_main", os.path.join(path_to_main, "temp_main.py")
        ).load_module()


def main_exec():
    return SourceFileLoader("main", os.path.join(path_to_main, "main.py")).load_module()
