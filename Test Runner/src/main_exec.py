import sys

path_to_main = "/main.py"

def main_exec():
  sys.path.append(path_to_main)
  # If a (patched) module is loaded, delete it
  if 'main' in sys.modules:
    del sys.modules["main"]
  import main
  sys.path.remove(path_to_main)