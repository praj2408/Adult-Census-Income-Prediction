import os
import yaml
import sys
import pandas as pd
import numpy as np
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
        
        
        logging.info("# there is an extra space before each value of categorical column so correct it.")
        categorical_feature = [feature for feature in df.columns if df[feature].dtype == 'O']
        for col in categorical_feature:
            df[col] = df[col].str.strip()
        
        
        
        logging.info("Repalcing '?' to 'NaN' Initiated")
        df['workclass'] = np.where(df['workclass']=='?',np.NaN, df['workclass'])
        df['occupation'] = np.where(df['occupation']=='?',np.NaN, df['occupation'])
        df['country'].replace('?', np.NaN, inplace=True) 
        logging.info("Repalcing '?' to 'NaN' Completed")

        
        logging.info("Dropping Dulipcates initiated")
        df.drop_duplicates(inplace=True)
        logging.info("Dropping Duplicates Completed")
        
        
        
        logging.info("'impute_missing' FUNCTION STARTED")
        df['workclass'].fillna(df['workclass'].mode()[0], inplace=True)
        df['occupation'].fillna(df['occupation'].mode()[0], inplace=True)
        df['country'].fillna(df.country.mode()[0], inplace=True)
        logging.info("'impute_missing' FUNCTION COMPLETED")


        data_path = config["preprocessing"]["processed"]
        
        logging.info("'Processes Data' Saving initiated")
        df.to_csv(data_path, index=False)
        logging.info("'Processed Data' Saving completed")
            
    except Exception as e:
        raise CustomException(e,sys)












if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    preprocessing(config_path=parsed_args.config)