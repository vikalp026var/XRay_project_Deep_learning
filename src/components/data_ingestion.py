import sys
from src.logger.logging import logging
from src.cloud_storage.s3_operation import S3Operation
from src.entity.artifact_entity import DataIngestionArtifact
from src.entity.config_entity import DataIngestionConfig
from src.exception.exception import CustomException

class DataIngestion:
     def __init__(self):
          pass
     
     def get_data_from_s3(self):
          try:
               pass
          except Exception as e:
               raise CustomException(e,sys)
          
          
     def initiate_data_ingestion(self):
          try:
               pass
          except Exception as e:
               raise CustomException(e,sys) 
          