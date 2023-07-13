import os
import yaml
import sys
import pandas as pd
import numpy as np
import argparse
from stage01_get_data import read_params
from application_logging import logging
from app_exception.app_exception import CustomException
from sklearn.model_selection import train_test_split




def split_data(config_path):
    logging.info("Reading all the params from config")
    config = read_params(config_path)
    logging.info("Reading all the params from config completed")

    
    data = config["final_data"]["transformed_data"]

    logging.info("Reading the transformed data")
    df = pd.read_csv(data)
    logging.info("Reading the transformed data completed")

    
    logging.info("Reading all the params from params.yaml")
    train_data = config["split_data"]["train_path"]
    test_data = config["split_data"]["test_path"]
    split_ratio = config["split_data"]["split_ratio"]
    random_state = config["base"]["random_state"]

    
    logging.info("Train test split Initiated")
    train, test = train_test_split(
                df, test_size=split_ratio, random_state=random_state)
    logging.info("Train test split completed successfully")

    train.to_csv(train_data, sep=",",
                              index=False, encoding="UTF-8")
    test.to_csv(test_data, sep=",",
                             index=False, encoding="UTF-8")
    logging.info("'split_data' function successfully compiled")


if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    split_data(config_path=parsed_args.config)