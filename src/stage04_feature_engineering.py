import os
import yaml
import sys
import pandas as pd
import numpy as np
import argparse
from stage01_get_data import read_params
from application_logging import logging
from app_exception.app_exception import CustomException
from sklearn.preprocessing import LabelEncoder




def feature_engineering(config_path):

    config = read_params(config_path)
    
    
    logging.info("Feature Engineering Process Started")
    data = config["preprocessing"]["processed"]
    
    logging.info("Reading preprocessed data...")
    df = pd.read_csv(data)
    logging.info("Reading preprocessed data Completed")
    
    
    
    logging.info( "'feature_engineering' FUNCTION STARTED")
    df["sex"] = pd.get_dummies(df["sex"], drop_first=True, dtype='int')
    df["salary"] = pd.get_dummies(df["salary"], drop_first=True, dtype='int')

    categorical = [feature for feature in df.columns if df[feature].dtype == 'O']

    for col in categorical:
        labels = df.groupby(col)['salary'].mean().sort_values().index
        mapping_dict = {k: i for i, k in enumerate(labels, 0)}
        # apply encoding to the data
        df[col] = df[col].map(mapping_dict)

    logging.info( "'feature_engineering' FUNCTION Completed")


    data_path = config["final_data"]["transformed_data"]

    logging.info("Saving the transformed data initiated")
    df.to_csv(data_path, index=False)
    logging.info("Saving the transformed data Completed")

    
if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    feature_engineering(config_path=parsed_args.config)