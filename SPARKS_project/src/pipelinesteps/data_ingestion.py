from zenml import step
from typing import Annotated
from SPARKS_project.src.utils.common import read_yaml,read_yaml_keys
from SPARKS_project.src.components.data_ingestion import Dataingestion
import pandas as pd

@step(enable_cache=False)
def data_ingestion_pipeline()-> Annotated[pd.DataFrame,"csv_file"]:
    try:
        path=read_yaml_keys()
        print(path)
        path_obj=Dataingestion(path)
        data=path_obj.ingest_data()
        print(data.head(5))
        return data
       
    except Exception as e:
      
        print(f"an error     {e}    occured while ingesting data    :")