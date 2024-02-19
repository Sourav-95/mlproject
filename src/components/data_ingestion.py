import os
import sys
from src.exception import CustomException
from src.logger import logging

import pandas as pd
from sklearn.model_selection import train_test_split
from dataclasses import dataclass

#decorator, instead of using __init__ we can directly define our class variables
#here we are defining class to save the location of the dataset
@dataclass  
class DataIngestionConfig:
    train_data_path: str=os.path.join('artifacts', "train.csv")
    test_data_path: str=os.path.join('artifacts', "test.csv")
    raw_data_path: str=os.path.join('artifacts', "data.csv")

#In this step we defining a class for DataIngestion
class DataIngestion:
    def __init__(self):
        self.ingestion_config =DataIngestionConfig()

    def initiate_dataingestion(self):
        logging.info("Enter the data ingestion method or component")
        try:
            #reading the dataset from the source, this can be from API or any source
            df=pd.read_csv('notebook/stud.csv')                
            logging.info('Read the dataset as info')

            #making the directory
            os.makedirs(os.path.dirname(self.ingestion_config.train_data_path), exist_ok=True)   
            df.to_csv(self.ingestion_config.raw_data_path, index=False, header=True)              #converting to csv file

            logging.info("Train_test_split initiated")
            train_set, test_set=train_test_split(df, test_size=0.2, random_state=42)             #train_test split
            train_set.to_csv(self.ingestion_config.train_data_path, index=False, header=True)    #saved the train file
            test_set.to_csv(self.ingestion_config.test_data_path, index=False, header=True)      #saved the test file
            
            #returning the train data path and test data path to next step which is data transformation
            logging.info("Ingestion of the data is completed")
            return(
                self.ingestion_config.train_data_path,
                self.ingestion_config.test_data_path
            )
        except Exception as e:
            raise CustomException(e, sys)
        
if __name__=='__main__':
    data_ingestion_obj=DataIngestion()
    data_ingestion_obj.initiate_dataingestion()