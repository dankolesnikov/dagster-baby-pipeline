local_config_raw = {
        "solids": {
            "read_csv_as_df": {
                "inputs": {"path": {"value": "/Users/danil/Desktop/dagster-pipelines/dagster_baby_pipeline/data/forestfires.csv"}}
            },
            "save_df": {
                "inputs": {"path": {"value": "/Users/danil/Desktop/dagster-pipelines/dagster_baby_pipeline/data/processsed_df.csv"}}
            }
        }
    }

prod_config_raw = {
        "solids": {
            "read_csv_as_df": {
                "inputs": {"path": {"value": "s3://fable.data/dagster_baby_pipeline/in/forestfires.csv"}}
            },
            "save_df": {
                "inputs": {"path": {"value": "s3://fable.data/dagster_baby_pipeline/out/processed_df.csv"}}
            }
        }
    }

"""
Generic function to get a dag config
"""
def get_dag_config(config: dict):
    dag_config = {
        "solids": {
            "read_csv_as_df": {
                "inputs": {"path": {"value": config["data_in"]}}
            },
            "save_df": {
                "inputs": {"path": {"value": config["data_out"]}}
            }
        }
    }
    return dag_config