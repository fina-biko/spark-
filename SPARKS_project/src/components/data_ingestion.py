from abc import abstractmethod,ABC
import pandas as pd
import yaml
from pathlib import Path
import numpy as np
from typing import Annotated
from zenml import step, pipeline
from SPARKS_project.src.utils.loggingfiles import logger
'''
This module has 2 classes
first class is the entity config , by use of   abstract method way, not the dataclass
2 nd class is the ingestion of the data from the source, which overides the first class
 zenml  is used to automatically keep a log of the artifacts instead of use having to keep it in memory
'''

class DataIngestionStrategy(ABC):
    @abstractmethod
    def ingest_data(self,data:pd.DataFrame)->Annotated[pd.DataFrame, "data"]:
        pass

class Dataingestion(DataIngestionStrategy):
    def __init__(self,datapath) :
        self.path=datapath

    def ingest_data(self)->Annotated[pd.DataFrame, "data"]:
        try:
            
            data=pd.read_csv(self.path)
            return data
        except Exception as e:
            print(f"could not read data from {self.path}   : {e}")

                                                      
    


    