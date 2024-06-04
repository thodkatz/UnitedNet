# Libraries
from os.path import dirname, basename, isfile, join
import glob

# Get the directory of the current script
current_directory = dirname(__file__)

# Find all Python files in the current directory
modules = glob.glob(join(current_directory, "*.py"))

# Iterate over the found Python files
for f in modules:
    # Check if the file is a regular file and not an __init__.py file
    if isfile(f) and not f.endswith('__init__.py'):
        # Get the base name of the file (without the directory path or extension)
        cur_f = basename(f)[:-3]
        # Import all symbols from the module
        exec(f"from src.configs.{cur_f} import *")