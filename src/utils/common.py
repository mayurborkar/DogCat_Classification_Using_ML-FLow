from zipfile import ZipFile
import pandas as pd
import logging
import json
import yaml
import time
import os

def read_yaml(path_to_yaml: str) -> dict:
    with open(path_to_yaml) as yaml_file:
        content = yaml.safe_load(yaml_file)
    logging.info(f"yaml file: {path_to_yaml} loaded successfully")
    return content

def create_directories(path_to_directories: list) -> None:
    for path in path_to_directories:
        os.makedirs(path, exist_ok=True)
        logging.info(f"created directory at: {path}")


def save_json(path: str, data: dict) -> None:
    with open(path, "w") as f:
        json.dump(data, f, indent=4)

    logging.info(f"json file saved at: {path}")


def unzip_files(source: str, dest:str) -> None:
    logging.info(f"Extraction Started....")

    with ZipFile(source, 'r') as zip_f:
        zip_f.extractall(dest)
    logging.info(f"Extraction From {source} to {dest}")




