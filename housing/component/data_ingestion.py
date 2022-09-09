from housing.entity.config_entity import DataIngestionConfig
import os,sys
from housing.exception import HousingException

from housing.logger import logging




class DataIngestion:
    def __init__(self,data_ingestion_config):
        try:
            logging.info((f"{'>>'*20}Data Ingestion log started.{'<<'*20} ")
            self.data_ingestion_config=data_ingestion_config
        except Exception as e:
            raise HousingException(e,sys)
        

