import os
from pathlib import Path
import logging

logging.basicConfig(level = logging.INFO ,format = '[%(asctime)s]: %(message)s:')

project_name = "textSummarizer"

list_of_files = [
    ".github/workflows/.gitkeep",        #.github is used while doing CI/CD deployment
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/components/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuration.py",
    f"src/{project_name}/pipeline/__init__.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    "config/config.yaml",
    "params.yaml",               #contains all parameters for the project
    "app.py",
    "main.py",
    "Dockerfile",
    "requirements.txt",
    "setup.py",                  #contains information about the package(helps in local package installation)
    "research/trials.ipynb",     #contains all the trials done for the project
    "README.md",                #contains information about the project
]

for filepath in list_of_files:
    filepath = Path(filepath)
    filedir, filename = os.path.split(filepath)
    
    if filedir != "":
        os.makedirs(filedir, exist_ok=True)
        logging.info(f"Creating directory: {filedir}")
    
    if (not os.path.exists(filepath)) or (os.path.getsize(filepath) == 0):
        with open(filepath, 'w') as f:
            pass
            logging.info(f"Creating file: {filepath}")
    else:
        logging.info(f"File already exists: {filename}") 