# Adult-Census-Income-Prediction

## Problem Statement:
The Goal is to predict whether a person has an income of more than 50K a year or not.
This is basically a binary classification problem where a person is classified into the >50K group or <=50K group.

## Dataset
The dataset used for this project is the Adult Census Income dataset. It contains information about individuals, such as age, workclass, education, marital status, occupation, relationship, race, gender, capital gain, capital loss, hours per week, and native country. Each individual is labeled with their income level, classified as either >50K or <=50K.

The dataset is provided in a CSV (Comma-Separated Values) format, with each row representing a separate individual and each column representing a specific attribute or feature.
## Website

## Methodology
**Data Exploration:** Initially, the dataset should be explored to understand its structure, check for missing values, and gain insights into the relationships between the features and the target variable.

**Data Preprocessing:** This step involves cleaning the dataset, handling missing values, encoding categorical variables, and normalizing numerical variables if necessary.

**Feature Engineering:** It may be beneficial to create new features or transform existing ones to improve the predictive power of the model. This step can involve techniques such as one-hot encoding, feature scaling, or creating interaction variables.

**Model Selection:** Various machine learning algorithms will be evaluated and compared to select the most appropriate one for the given problem. Commonly used algorithms for binary classification include logistic regression, decision trees, random forests, and support vector machines.

**Model Training:** The selected model will be trained on the preprocessed data. This involves splitting the dataset into training and validation subsets, fitting the model to the training data, and tuning its hyperparameters.

**Model Evaluation:** The trained model will be evaluated using appropriate evaluation metrics, such as accuracy, precision, recall, and F1 score, to measure its performance. Cross-validation techniques can be used to obtain more reliable estimates of the model's performance.

**Model Deployment:** Once a satisfactory model is obtained, it can be deployed in a production environment for making predictions on new, unseen data. This may involve creating an API or integrating the model into an existing software system.

## MLOps Level 1: ML Pipeline Automation Architecture
The goal of level 1 is to perform continuous training of the model by automating the ML pipeline; this lets you achieve continuous delivery of model prediction service. To automate the process of using new data to retrain models in production, you need to introduce automated data and model validation steps to the pipeline, as well as pipeline triggers and metadata management.

The following figure is a schematic representation of an automated ML pipeline for CT.
![](https://github.com/praj2408/ETE-Protect/blob/main/images/ML%20pipeline%20automation.jpg)

## MLOps Level 2: CI/CD Pipeline Automation
For a rapid and reliable update of the pipelines in production, you need a robust automated CI/CD system. This automated CI/CD system lets your data scientists rapidly explore new ideas around feature engineering, model architecture, and hyperparameters. They can implement these ideas and automatically build, test, and deploy the new pipeline components to the target environment.

The following diagram shows the implementation of the ML pipeline using CI/CD, which has the characteristics of the automated ML pipelines setup plus the automated CI/CD routines.
![](https://github.com/praj2408/ETE-Protect/blob/main/images/cicd%20pipeline%20automation.jpg)
