import os
import yaml
import sys
import pandas as pd
import argparse
from application_logging import logging
from app_exception.app_exception import AppException




def read_params(config_path):
    try:
        logging.info("Reading all params from config_path")
        with open(config_path) as f:
            config = yaml.safe_load(f)
            logging.info("parameters readed from config_path successfully!!!")
            
            return config
        
    except Exception as e:
        logging.info(f"Exception Occurred while reading parameters from config_path -->{e}")
        raise AppException(e,sys)


def get_data(config_path):
    try:
        logging.info("getting the data from the source")
        config = read_params(config_path)
        data_path = config['data_source']['s3_source']
        df = pd.read_csv(data_path)
        logging.info(f"Data Fetched from the source Successfully !!!")
        return df
    except Exception as e:
        logging.info(
                f"Exception Occurred while getting data from the source -->{e}")
        raise AppException(e, sys)
    
    
    
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    get_data(config_path=parsed_args.config)