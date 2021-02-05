from dagster import pipeline, solid, PresetDefinition
from dagster_baby_pipeline import constants, configs, io_solids, logic

@pipeline(
    name="BabyPipeline",
    preset_defs=[
        PresetDefinition(
            name="local",
            run_config=configs.local_config_raw
        ),
        PresetDefinition(
            name="prod",
            run_config=configs.prod_config_raw
        )
    ]
)
def pipeline():
    df_input = io_solids.read_csv_as_df()
    df_processed = logic.transform_data(df_input)
    io_solids.save_df(df_processed)