from housing.entity.config_entity import DataIngestionConfig, DataTransformationConfig, DataValidationConfig, ModelEvaluationConfig, ModelPusherConfig,ModelTrainerConfig,TrainingPipelineConfig

from housing.util.util import read_yaml_file
from housing.constatnt import *

import os
 
ROOT_DIR = os.getcwd()     ## to get current working directory

class Configuration:
    def __init__(self) -> None:
        pass

    def get_data_ingestion_config(self) ->DataIngestionConfig:
        pass

    def get_data_validation_config(self) ->DataValidationConfig:
        pass

    def get_data_transformation_config(self) ->DataTransformationConfig:
        pass

    def get_model_trainer_config(self) ->ModelTrainerConfig:
        pass

    def get_model_evaluation_config(self) ->ModelEvaluationConfig:
        pass

    def get_mode_pusher_config(self) ->ModelPusherConfig:
        pass

    def get_training_pipeline_config(self) ->TrainingPipelineConfig:
        pass