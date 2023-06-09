
"""
this file contan all component config details
"""

from collections import namedtuple

DataIngestionConfig = namedtuple(
    "DataIngestionConfig",
    [
        "dataset_download_url",
        "tgz_download_dir",
        "raw_data_dir",
        "ingested_train_dir",
        "ingested_test_dir",
    ],
)


DataValidationConfig = namedtuple(
    "DataValidationConfig",
    ["schema_file_path", "report_file_path", "report_page_file_path"],
)


DataTransformationConfig = namedtuple(
    "DataTransformationConfig",
    [
        "add_bedroom_per_room",
        "transformed_train_dir",
        "transformed_test_dir",
        "preprocessed_object_file_path",
        "json_info_file_path"
        
    ],
)


ModelTrainerConfig = namedtuple(
    "ModelTrainerConfig",
    ["trained_model_dir", "base_accuracy", 
        "model_config_file_path","model_info_jaon_file_path",
        "cluster_model_file_path",
        "overall_models_info_json_path"],
)

ModelEvaluationConfig = namedtuple(
    "ModelEvaluationConfig", [  "current_model_report_json_path"
                                ]
)


ModelPusherConfig = namedtuple("ModelPusherConfig", ["production_models_dir","old_production_model_dir",
                                "cluster_model_dir"])

TrainingPipelineConfig = namedtuple("TrainingPipelineConfig", ["artifact_dir"])

