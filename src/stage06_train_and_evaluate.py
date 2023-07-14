import os
import yaml
import sys
import pandas as pd
import numpy as np
import argparse
import joblib
import json

from stage01_get_data import read_params
from application_logging import logging
from app_exception.app_exception import CustomException

from sklearn.model_selection import RandomizedSearchCV
from sklearn.ensemble import RandomForestClassifier
from sklearn.metrics import accuracy_score, confusion_matrix, classification_report



def train_and_evaluate(config_path):
    
    config = read_params(config_path)

    train_data_path = config["split_data"]["train_path"]
    test_data_path = config["split_data"]["test_path"]
    random_state = config["base"]["random_state"]
    model_dir = config["model_dirs"]
    target = config["base"]["target_col"]


    try:
    
        train = pd.read_csv(train_data_path,sep=",")
        logging.info("train data read successfully")
        test = pd.read_csv(test_data_path,sep=',')
        logging.info("test data read successfully")

        train_y = train[target]
        test_y = test[target]
        
        train_X = train.drop(target,axis=1)
        test_X = test.drop(target, axis=1)


        # Hyper parameter tuning
        n_estimators = config["estimators"]["RandomForestClassifier"]["params"]["n_estimators"]
        min_samples_split = config["estimators"]["RandomForestClassifier"]["params"]["min_samples_split"]
        min_samples_leaf = config["estimators"]["RandomForestClassifier"]["params"]["min_samples_leaf"]
        max_features = config["estimators"]["RandomForestClassifier"]["params"]["max_features"]
        max_depth = config["estimators"]["RandomForestClassifier"]["params"]["max_depth"]
        criterion = config["estimators"]["RandomForestClassifier"]["params"]["criterion"]
        
        
        
        rf_clf = RandomForestClassifier(
                                        n_estimators=n_estimators,
                                        min_samples_split=min_samples_split,
                                        min_samples_leaf=min_samples_leaf,
                                        max_features = max_features,
                                        max_depth=max_depth,
                                        criterion=criterion
                                        )
        logging.info("Model Training on RandomForestClassifier Initiated")
        rf_clf.fit(train_X, train_y)
        logging.info("Model Trained on RandomForestClassifier successfully")

        y_pred = rf_clf.predict(test_X)
        
        accuracy = accuracy_score(test_y,y_pred)
        print(accuracy)
        clf_report = classification_report(test_y,y_pred)
        print(clf_report)


        scores_file = config["reports"]["scores"]
        params_file = config['reports']['params']

        with open(scores_file, 'w') as f:
            scores = {
                'accuracy': accuracy,
                'classification_report': clf_report
            }

            json.dump(scores, f, indent=4)
        logging.info("scores written to file")

        with open(params_file, 'w') as f:
            params = {
                "n_estimators":n_estimators,
                "min_samples_split":min_samples_split,
                "min_samples_leaf": min_samples_leaf,
                "max_features": max_features,
                "max_depth": max_depth,
                "criterion": criterion
                
            }
            json.dump(params, f, indent=4)
        logging.info("Params written to file")


        os.makedirs(model_dir, exist_ok=True)
        model_path = os.path.join(model_dir,"model.joblib")
        joblib.dump(rf_clf, model_path)

    
    
    except Exception as e:
        raise CustomException(e,sys)



if __name__ == '__main__':
    args = argparse.ArgumentParser()
    args.add_argument('--config', default='params.yaml')
    parsed_args = args.parse_args()
    train_and_evaluate(config_path=parsed_args.config)