
import os 
import json


# List of your file names
file_names = os.listdir()  # replace with your file names

# Minimal Jupyter notebook structure
notebook = {
"cells": [],
"metadata": {},
"nbformat": 4,
"nbformat_minor": 4
}

for file_name in file_names:
  with open(f"{file_name}.ipynb", 'w') as f:
    json.dump(notebook, f)
