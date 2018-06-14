import os
from genericpath import isfile
from os.path import join

path = os.path.join(os.path.dirname(__file__), 'tests/unit_tests')
path = str.replace(path, "\\", "/")
test_files = [f for f in os.listdir(path) if isfile(join(path, f))]
for file in test_files:
    os.system(f"{file} 1")
