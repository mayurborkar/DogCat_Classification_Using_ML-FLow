from src.utils.common import read_yaml, create_directories, unzip_files
import urllib.request as req
from tqdm import tqdm
import argparse
import logging
import random
import shutil
import os

STAGE = "GET_DATA" ## <<< change stage name 

logging.basicConfig(
                    filename=os.path.join("logs", 'running_logs.log'), 
                    level=logging.INFO, 
                    format="[%(asctime)s: %(levelname)s: %(module)s]: %(message)s",
                    filemode="a"
                    )


def main(config_path):

    ## read config files
    config = read_yaml(config_path)
    URL = config["data"]["source_url"]

    local_dir = config["data"]["local_dir"]
    create_directories([local_dir])

    data_file = config["data"]["data_file"]
    data_file_path = os.path.join(local_dir, data_file)

    #Check The File Is Present Or Not
    if not os.path.isfile(data_file_path):
        logging.info(f"Downloading Started....")

        filename, headers = req.urlretrieve(URL, data_file_path)
        logging.info(f"filename:{filename} created with info \n{headers}")

    else:
        logging.info(f"Filename {data_file} Already present")

    #Unzip The Data
    unzip_data_dir= config["data"]["unzip_data_dir"]
    if not os.path.exists(unzip_data_dir):
        create_directories([unzip_data_dir])
        unzip_files(source=data_file_path, dest=unzip_data_dir)
    else:
        logging.info(f"Data Already Extracted")


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument("--config", "-c", default="configs/config.yaml")
    parsed_args = args.parse_args()

    try:
        logging.info("\n********************")
        logging.info(f">>>>> stage {STAGE} started <<<<<")
        main(config_path=parsed_args.config)
        logging.info(f">>>>> stage {STAGE} completed!<<<<<\n")
    except Exception as e:
        logging.exception(e)
        raise e