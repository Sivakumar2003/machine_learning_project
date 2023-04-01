from collections import namedtuple

DataInjectionArtifacts = namedtuple(
    "DataInjectionArtifacts",
    ["train_file_path", "test_file_path", "is_injected", "message"],
)

DataValidationArtifacts = namedtuple(
    "DataValidationArtifacts", ["all_correct_or_not", "json_report_file_path"]
)

FeatureEngineeringArtifacts = namedtuple(
    "FeatureEngineeringArtifacts",
    [
        "transformed_train_file_path",
        "transformed_test_file_path",
        "tranformation_model_path",
        "is_done_for_FE",
        "message",
    ]
)

ModelTrainingArtifacts = namedtuple("DataTrainingArtifacts", [
    "model_training_json_file_path",
])

ModelEvaluationArtifacts=namedtuple("ModelEvaluationArtifacts", [
    "to_change_or_not",
    "to_changed_model_cluster_grp",
    "new_model_path"
])