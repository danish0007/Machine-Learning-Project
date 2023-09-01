import os
import sys
from src.exception import CustomException
from src.logger import logging
import pandas as pd
from sklearn.model_selection import train_test_split
import pandas as pd
from dataclasses import dataclass
from src.components.data_transformation import DataTransformation

@dataclass
class DataIngestionConfig:
    train_data_path :str = os.path.join('artifacts', 'train.csv')
    test_data_path :str = os.path.join('artifacts', 'test.csv')
    raw_data_path :str = os.path.join('artifacts', 'data.csv')

class DataIngestion:
    def __init__(self):
        self.ingestion_config = DataIngestionConfig()

    def initiate_data_ingestion(self):
        logging.info("Data Ingestion Initiated")

        try:
            df = pd.read_csv('notebook/data/stud.csv')
            logging.info("Reading data as dataframe")

            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)

            train_data , test_data = train_test_split(df, test_size=0.2, random_state=7)
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)
            train_data.to_csv(self.ingestion_config.train_data_path, index=False, header=True)
            test_data.to_csv(self.ingestion_config.test_data_path, index=False, header=True)

            logging.info('Ingestion of data Completed')

            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        
        except Exception as e:
            raise CustomException(e, sys)

if __name__ == "__main__":
    obj = DataIngestion()
    train_data,test_data=obj.initiate_data_ingestion()

    data_transformation=DataTransformation()
    train_arr,test_arr,_=data_transformation.initiate_data_transformation(train_data,test_data)