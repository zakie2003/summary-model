from text_summarizer.logging import logging
from ensure import ensure_annotations
import pathlib
from typing import Any
from box.exceptions import BoxValueError


@ensure_annotations
def read_yaml_file(file_path: str) -> Any:
    """
    Reads a YAML file and returns its content as a dictionary.

    Args:
        file_path (str): The path to the YAML file.

    Returns:
        Any: The content of the YAML file.
    """
    try:
        from box import Box
        return Box.from_yaml(filename=file_path)
    except BoxValueError as e:
        logging.error(f"Error reading YAML file {file_path}: {e}")
        raise
    except Exception as e:
        logging.error(f"Unexpected error reading YAML file {file_path}: {e}")
        raise

@ensure_annotations
def create_directories(paths: list[str]) -> None:
    """
    Creates directories for the given paths if they do not exist.

    Args:
        paths (list[str]): List of directory paths to create.
    """
    for path in paths:
        try:
            pathlib.Path(path).mkdir(parents=True, exist_ok=True)
            logging.info(f"Directory created: {path}")
        except Exception as e:
            logging.error(f"Error creating directory {path}: {e}")
            raise

@ensure_annotations
def get_size(file_path: str) -> int:
    """
    Returns the size of the file at the given path.

    Args:
        file_path (str): The path to the file.

    Returns:
        int: The size of the file in bytes.
    """
    try:
        return pathlib.Path(file_path).stat().st_size
    except FileNotFoundError as e:
        logging.error(f"File not found: {file_path}. Error: {e}")
        raise
    except Exception as e:
        logging.error(f"Error getting size of file {file_path}: {e}")
        raise