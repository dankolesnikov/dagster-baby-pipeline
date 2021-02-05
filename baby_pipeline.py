from dagster import pipeline, solid, PresetDefinition
from .io_solids import *
from .logic import *
from .configs import *

@pipeline(
    name="BabyPipeline",
    preset_defs=[
        PresetDefinition(
            name="local",
            run_config=local_config_raw
        ),
        PresetDefinition(
            name="prod",
            run_config=prod_config_raw
        )
    ]
)
def pipeline():
    df_input = read_csv_as_df()
    df_processed = transform_data(df_input)
    save_df(df_processed)