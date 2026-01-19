import os
import sys 

from networksecurity.exception.exception import NetworkSecurityException
from networksecurity.logging.logger import logging

from networksecurity.components.data_ingestion import DataIngestion
from networksecurity.components.data_validation import DataValidation
from networksecurity.components.data_transformation import DataTransformation
from networksecurity.components.model_trainer import ModelTrainer

from networksecurity.entity.config_entity import TrainingPipelineConfig, DataIngestionConfig, DataValidationConfig, DataTransformationConfig, ModelTrainerConfig
from networksecurity.entity.artifact_entity import DataIngestionArtifact, DataValidationArtifact, DataTransformationArtifact, ModelTrainerArtifact

class TrainingPipeline:
    def __init__(self):
        try:
            logging.info(f"{'>>'*20} Training Pipeline Starting {'<<'*20}")
            self.training_pipeline_config = TrainingPipelineConfig()
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def start_data_ingestion(self):
        try:
            self.data_ingestion_config = DataIngestionConfig(training_pipeline_config=self.training_pipeline_config)
            logging.info(f"{'>>'*20} Starting Data Ingestion {'<<'*20}")
            data_ingestion = DataIngestion(data_ingestion_config=self.data_ingestion_config)
            data_ingestion_artifact: DataIngestionArtifact = data_ingestion.initiate_data_ingestion()
            logging.info(f"Data Ingestion Artifact: {data_ingestion_artifact}")
            logging.info(f"{'>>'*20} Data Ingestion Completed {'<<'*20}")
            return data_ingestion_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
        
    def start_data_validation(self, data_ingestion_artifact: DataIngestionArtifact):
        try:
            data_validation_config = DataValidationConfig(training_pipeline_config=self.training_pipeline_config)
            data_validation = DataValidation(data_validation_config=data_validation_config,
                                             data_ingestion_artifact=data_ingestion_artifact)
            logging.info(f"{'>>'*20} Starting Data Validation {'<<'*20}")
            data_validation_artifact: DataValidationArtifact = data_validation.initiate_data_validation()
            return data_validation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
    
    def start_data_transformation(self, data_validation_artifact: DataValidationArtifact):
        try:
            data_transformation_config = DataTransformationConfig(training_pipeline_config=self.training_pipeline_config)
            data_transformation = DataTransformation(data_transformation_config=data_transformation_config,
                                                     data_validation_artifact=data_validation_artifact)
            logging.info(f"{'>>'*20} Starting Data Transformation {'<<'*20}")
            data_transformation_artifact: DataTransformationArtifact = data_transformation.initiate_data_transformation()
            return data_transformation_artifact
        except Exception as e:
            raise NetworkSecurityException(e, sys)
            