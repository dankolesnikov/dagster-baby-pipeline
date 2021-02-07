local_config_raw = {
    "solids": {
        "get_data": {
            "solids": {
                "get_data_location": {
                    "inputs": {
                        "path": {
                            "value": "/Users/danil/Desktop/dagster-pipelines/dagster_baby_pipeline/data/forestfires.csv"
                        }
                    }
                }
            }
        },
        "save_df": {
            "inputs": {
                "path": {
                    "value": "/Users/danil/Desktop/dagster-pipelines/dagster_baby_pipeline/data/processsed_df.csv"
                }
            }
        },
    }
}


prod_config_raw = {
    "solids": {
        "get_data": {
            "solids": {
                "get_data_location": {
                    "inputs": {
                        "path": {
                            "value": "s3://fable.data/baby_pipeline/forestfires.csv"
                        }
                    }
                }
            }
        },
        "save_df": {
            "inputs": {
                "path": {"value": "s3://fable.data/baby_pipeline/processed_df.csv"}
            }
        },
    }
}
