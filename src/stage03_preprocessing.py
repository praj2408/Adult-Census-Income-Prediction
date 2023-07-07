import os
import yaml
import sys
import pandas as pd
import argparse
from stage01_get_data import read_params, get_data
from application_logging import logging
from app_exception.app_exception import CustomException





def preprocessing(config_path):
    try:
        logging.info("'column_imputation' FUNCTION STARTED")
        config = read_params(config_path)
        df = get_data(config_path)
        df.columns = df.columns.str.lower()
        df.columns = df.columns.str.replace('-', '_')
        logging.info("'column_imputation' FUNCTION COMPILED SUCCESSFULLY")
        
        
        
        logging.info("'impute_missing' FUNCTION STARTED")
        
        
            
    except Exception as e:
        raise CustomException(e,sys)












if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    preprocessing(config_path=parsed_args.config)