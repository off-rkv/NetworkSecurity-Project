import os
import sys
import numpy as np
import pandas as pd

#CLASS_LABEL 0= Legitimad=te website , 1= Phishing website
"""
define common constant variable for training pipeline
"""
TARGET_COLUMN="CLASS_LABEL"
PIPELINE_NAME:str="NetworkSecurity"
ARTIFACT_DIR:str="Artifacts"
FILE_NAME:str="Phishing_Legitimate_full.csv"

TRAIN_FILE_NAME:str='train.csv'
TEST_FILE_NAME:str='test.csv'

SCHEMA_FILE_PATH=os.path.join('data_schema','schema.yaml')
"""
Data Ingestion related constant start with DATA_INGESTION VAR NAME
"""

DATA_INGESTION_COLLECTION_NAME:str='NetworkData'
DATA_INGESTION_DATABASE_NAME: str = 'offrkv'
DATA_INGESTION_DATA_NAME: str = 'data_ingestion'
DATA_INGESTION_FEATURE_STORE_DIR: str = 'feature_store'
DATA_INGESTION_INGESTION_DIR: str = 'ingestion'
DATA_INGESTION_TRAIN_TEST_SPLIT_RATION: float = 0.4

"""
Data Validation related constant start with DATA_VALIDATION VAR NAME
"""

DATA_VALIDATION_DIR_NAME:str='data_validation'
DATA_VALIDATION_VALID_DIR:str='validated'
DATA_VALIDATION_INVALID_DIR:str='invalid'
DATA_VALIDATION_DRIFT_REPORT_DIR:str='drift_report'
DATA_VALIDATION_DRIFT_REPORT_FILE_NAME:str='report.yaml'
