import os
import pathlib

project_name="text_summarizer"

file_list=[
    f"config/",
    f"src/{project_name}/__init__.py",
    f"src/{project_name}/component/__init__.py",
    f"src/{project_name}/utils/__init__.py",
    f"src/{project_name}/utils/common.py",
    f"src/{project_name}/logging/__init__.py",
    f"src/{project_name}/logging/common.py",
    f"src/{project_name}/config/__init__.py",
    f"src/{project_name}/config/configuation.py",
    f"src/{project_name}/entity/__init__.py",
    f"src/{project_name}/constants/__init__.py",
    f"src/{project_name}/config.py",
    f"config/configuration.yaml",
    f"params.yaml",
    "app.py",
    "main.py",
    "README.md",
    "requirements.txt",
    "setup.py",
    "Dockerfile",
    "research/training.ipynb"
]


for file in file_list:
    file_path = pathlib.Path(file)
    file_dir, file_name = os.path.split(file_path)
    if file_dir and not os.path.exists(file_dir):
        os.makedirs(file_dir)
    if not os.path.exists(file_path):
        with open(file_path, 'w') as f:
            if file_name == "__init__.py":
                f.write("# This is an init file for the package\n")
            elif file_name == "README.md":
                f.write("# Project Title\n\nThis is a placeholder for the project README.\n")
            elif file_name == "requirements.txt":
                f.write("# List of project dependencies\n")
            elif file_name == "setup.py":
                f.write("# Setup script for the project\n")
            else:
                f.write(f"# Placeholder for {file_name}\n")
    print(f"Created file: {file_path}")
