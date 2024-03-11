from SPARKS_project.src.pipelinesteps.data_ingestion import data_ingestion_pipeline
class DataIngestion:
    def main(self):
        data_ingestion_pipeline()
    

if __name__ =='__main__':
    DataIngestion().main()