import os
import sys

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.entity.artifact_entity import DataTransformationArtifact, ModelTrainerArtifact
from networksecurity.entity.config_entity import ModelTrainerConfig

from networksecurity.utils.ml_utils.model.estimator import NetworkModel
from networksecurity.utils.main_utils.utils import load_object, save_object
from networksecurity.utils.main_utils.utils import load_numpy_array_data
from networksecurity.utils.ml_utils.metric.classification_metric import get_classification_score


class ModelTrainer:
    def __init__(self, model_trainer_config: ModelTrainerConfig,
                 data_transformation_artifact: DataTransformationArtifact):
        try:
            logging.info(f"{'>>' * 20} Model Trainer {'<<' * 20}")
            self.model_trainer_config = model_trainer_config
            self.data_transformation_artifact = data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def train_model(self, x, y):
        try:
            model = NetworkModel()
            model.train(x, y)
            return model
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def initiate_model_trainer(self) -> ModelTrainerArtifact:
        try:
            train_file_path = self.data_transformation_artifact.transformed_train_file_path
            test_file_path = self.data_transformation_artifact.transformed_test_file_path

            #loading training array and testing array
            train_array = load_numpy_array_data(train_file_path)
            test_array = load_numpy_array_data(test_file_path)

            x_train, y_train = train_array[:, :-1], train_array[:, -1]
            x_test, y_test = test_array[:, :-1], test_array[:, -1]

            model = self.train_model(x_train, y_train)
        except Exception as e:
            raise NetworkSecurityException(e, sys)