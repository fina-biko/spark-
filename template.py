import os
from pathlib import Path
import logging
logging.basicConfig(level=logging.INFO)
'''- SPARKS_project/
  - src/
    - __init__.py
    - steps/
      - __init__.py
    - components/
      - __init__.py
      - data_ingestion.py
    - utils/
      - __init__.py
    - artifacts/
      - model.json
- main.py
- Dockerfile
- setup.py
- requirements.txt

'''
SOURCE='SPARKS_project'
PROJECT='src'
structures=[
    f"{SOURCE}/__init__.py",
    f"{SOURCE}/{PROJECT}/__init__.py",
    
    f"{SOURCE}/{PROJECT}/pipelinesteps/__init__.py",
    
    f"{SOURCE}/{PROJECT}/components/__init__.py",
    f"{SOURCE}/{PROJECT}/components/data_ingestion.py",
    f"{SOURCE}/{PROJECT}/utils/__init__.py",
    #f"src/{project_name}/components/__init__.py",
    f"{SOURCE}/{PROJECT}/artifacts/model.json",
    f"{SOURCE}/{PROJECT}/AllPipelines/__init__.py",
    'main.py',
    'Dockerfile',
    'setup.py',
    'requirements.txt']


for filepath in structures:
    filepath = Path(filepath)
    filedir = filepath.parent
    filename = filepath.name

    if filedir != "":
        os.makedirs(filedir, exist_ok=True)

    full_filepath = filedir / filename

    if not os.path.exists(full_filepath):
        with open(full_filepath, 'w'):
            pass   

    '''if filename:  # if it's a file
        with open(path, 'w') as f:
            f.write('')'''

logging.info('Creating the directory')
   
'''for filepath in list_of_files:
    filepath=Path(filepath)
    filedir,filename=os.path.split(filepath)

    if filedir!="":
        os.makedirs(filedir,exist_ok=True)
    if(not os.path.exists(filename)):
        with open(filename,'w') as f:
            pass'''
