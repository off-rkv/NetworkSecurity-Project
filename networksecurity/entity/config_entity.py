from datetime import datetime
import os

from networksecurity.constant import training_pipeline

print(training_pipeline.PIPELINE_NAME)
print(training_pipeline.ARTIFACT_DIR)

class training_pipeline_config:
    def __init__(self,timestamp=datetime.now()):
        timestamp=timestamp.strftime('%d_%m_%Y_%H_%M_%S')
        self.pipeline_name=training_pipeline.PIPELINE_NAME
        self.artifact_name=training_pipeline.ARTIFACT_DIR
        self.artifact_dir=os.path.join(self.artifact_name,timestamp)
        self.timestamp:str=timestamp

class DataIngestionConfig:
    def __init__(self,training_pipeline_config):
        self.data_ingestion_dir:str=os.path.join(
            training_pipeline_config.artifact_dir,training_pipeline.DATA_INGESTION_INGESTION_DIR
        )
        '''
        Artifacts/
            └── 25_05_2025_13_15_20/
                └── ingestion/      ← This is data_ingestion_dir

        '''

        self.feature_store_file_path:str=os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_FEATURE_STORE_DIR,training_pipeline.FILE_NAME
        )
        '''
        Artifacts/
            └── 25_05_2025_13_15_20/
                └── ingestion/
                    └── feature_store/
                        └── Phishing_Legitimate_full.csv  ← feature_store_file_path

        '''
        self.training_file_path:str=os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTION_DIR,training_pipeline.TRAIN_FILE_NAME
        )

        self.testing_file_path:str=os.path.join(
            self.data_ingestion_dir,training_pipeline.DATA_INGESTION_INGESTION_DIR,training_pipeline.TEST_FILE_NAME
        )

        self.train_test_split_ratio:float=training_pipeline.DATA_INGESTION_TRAIN_TEST_SPLIT_RATION
        self.collection_name:str=training_pipeline.DATA_INGESTION_COLLECTION_NAME
        self.database_name:str=training_pipeline.DATA_INGESTION_DATABASE_NAME
        '''
        Artifacts/
            └── 25_05_2025_13_15_20/        ← timestamp folder
                └── ingestion/
                    ├── feature_store/
                    │   └── Phishing_Legitimate_full.csv
                    └── ingestion/
                        ├── train.csv          ← 60% training data
                        └── test.csv           ← 40% testing data

        '''
    
    
class DataValidationConfig:
    def __init__(self,training_pipeline_config:training_pipeline_config):
        self.data_validation_dir:str=os.path.join(training_pipeline_config.artifact_dir,training_pipeline.DATA_VALIDATION_DIR_NAME)
        self.valid_data_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_VALID_DIR)
        self.invalid_data_dir: str = os.path.join(self.data_validation_dir, training_pipeline.DATA_VALIDATION_INVALID_DIR)
        self.valid_train_file_path:str=os.path.join(self.valid_data_dir,training_pipeline.TRAIN_FILE_NAME)
        self.valid_test_file_path:str=os.path.join(self.valid_data_dir,training_pipeline.TEST_FILE_NAME)
        self.invalid_train_file_path:str=os.path.join(self.invalid_data_dir,training_pipeline.TRAIN_FILE_NAME)
        self.invalid_test_file_path:str=os.path.join(self.invalid_data_dir,training_pipeline.TEST_FILE_NAME)

        self.drift_report_file_path:str=os.path.join(
            self.data_validation_dir,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_DIR,
            training_pipeline.DATA_VALIDATION_DRIFT_REPORT_FILE_NAME
        )
        """
        Artifacts/
            └── 27_05_2025_14_10_05/
                ├── ingestion/
                │   ├── feature_store/
                │   │   └── Phishing_Legitimate_full.csv
                │   └── ingestion/
                │       ├── train.csv
                │       └── test.csv
                └── data_validation/
                    ├── valid/
                    │   ├── train.csv
                    │   └── test.csv
                    ├── invalid/
                    │   ├── train.csv
                    │   └── test.csv
                    └── drift_report/
                        └── drift_report.yaml
                """


class DataTransformationConfig:
    def __init__(self, training_pipeline_config: training_pipeline_config):
        self.data_transformation_dir: str = os.path.join(
            training_pipeline_config.artifact_dir,
            training_pipeline.DATA_TRANSFORMATION_DIR_NAME
        )

        self.transformed_train_file_path: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.TRAIN_FILE_NAME.replace('csv','npy')
        )

        self.transformed_test_file_path: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_DATA_DIR,
            training_pipeline.TEST_FILE_NAME.replace('csv','npy')
        )

        self.transformed_object_file_path: str = os.path.join(
            self.data_transformation_dir,
            training_pipeline.DATA_TRANSFORMATION_TRANSFORMED_OBJECT_DIR,
            training_pipeline.PREPROCESSING_OBJECT_FILE_NAME
        )
    '''
    Artifacts/
        └── data_transformation/
            ├── transformed_
            |        └── train.npy
            |        └── test.npy
            └──transformed_object
                    
    '''

class ModelTrainerConfig:
    def __init__(self,training_pipeline_config:training_pipeline_config):
        self.model_trainer_dir=os.path.join(
            training_pipeline_config.artifact_dir,training_pipeline.MODEL_TRAINER_DIR_NAME
        )
        self.trained_model_file_path:str=os.path.join(
            self.model_trainer_dir,training_pipeline.MODEL_TRAINER_TRAINED_MODEL_DIR,
            training_pipeline.MODEL_TRAINER_TRAINED_MODEL_NAME
        )
        self.expected_accuracy:float=training_pipeline.MODEL_TRAINER_EXPECTED_SCORE
        self.overfitting_underfitting_threshold=training_pipeline.MODEL_TRAINER_OVER_FITTING_UNDER_FITTING_THRESHOLD