import os 
import sys
from exception_handling import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
from data_transformation import DataTransformation
from data_transformation import DataTransformationConfig

from src.components.model_trainer import ModelTrainerConfig
from src.components.model_trainer import ModelTrainer

from dataclasses import dataclass
@dataclass
class DataIngestionConfig:
    train_data_path : str=os.path.join('artifactcs',"train.csv")
    test_data_path : str=os.path.join('artifactcs',"test.csv")
    raw_data_path : str=os.path.join('artifactcs',"data.csv")

class DataIngestion:
    def __init__(self):
        self.ingestion_config=DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Entered the data igestion method or config")
        try:
            df=pd.read_csv("notebook\data\stud.csv")
            logging.info("Read the dataset as dataframe")
        
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path),exist_ok=True)

            df.to_csv(self.ingestion_config.raw_data_path,index=False,header=True)
            logging.info("Trian test split is initiated")
            train_set,test_set=train_test_split(df,test_size=0.2,random_state=42)

            train_set.to_csv(self.ingestion_config.train_data_path,index=False,header=True)
            test_set.to_csv(self.ingestion_config.test_data_path,index=False,header=True)
            logging.info("Ingestion is completed")

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path

            )
        except Exception as e:
            raise CustomException(e,sys)

if __name__=='__main__':
    obj=DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()
    data_transformation=DataTransformation()
    
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)
    model_trainer=ModelTrainer()
    print(model_trainer.initiate_model_trainer(train_arr,test_arr))
     