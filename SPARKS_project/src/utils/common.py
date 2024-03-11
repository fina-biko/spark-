# we need a file to read the yaml file
#then another method to extract the  csv data, it takes input from the readyaml file

import yaml
from SPARKS_project.src.CONSTANTS import CONFIG_INGESTION_YAML
def read_yaml(path=CONFIG_INGESTION_YAML):
    with open(path, "r") as file:
        data = yaml.safe_load(file)
        print(data)
        return data
    
def read_yaml_keys():
    try:
        yaml_dict = read_yaml()
        source_url =yaml_dict.get('data_ingestion', {}).get('source_url')
        print(source_url)
        return source_url
    except Exception as e:
        print(f"could not fetch csv path from yaml file   : {e}")
