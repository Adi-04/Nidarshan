from Nidarshan import logger
from Nidarshan.pipeline.stage_01_data_ingestion import DataIngestionTrainingPipeline
# from Nidarshan.pipeline.stage_02_prepare_base_model import PrepareBaseModelTrainingPipeline
# from Nidarshan.pipeline.stage_03_training import ModelTrainingPipeline
# from Nidarshan.pipeline.stage_04_evaluation import EvaluationPipeline

STAGE_NAME = "Data Ingestion Stage"
try:
    logger.info(f">>>>>> stage {STAGE_NAME} started <<<<<<<")
    obj = DataIngestionTrainingPipeline()
    obj.main()
    logger.info(f">>>>>> stage {STAGE_NAME} completed <<<<<<< \n\nx====================x")
except Exception as e:
    logger.exception(e)
    raise e 