from dagster import OutputDefinition,Output,pipeline, solid, PresetDefinition, composite_solid
from dagster_baby_pipeline import constants, configs, io_solids, logic

@composite_solid(output_defs=[
        OutputDefinition(name="df_from_local", is_required=False),
        OutputDefinition(name="df_from_s3", is_required=False),
    ])
def get_data() -> constants.PandasDataFrame:
    local_path, s3_coordninates = io_solids.get_data_location()
    df_local = io_solids.read_csv_as_df_locally(local_path)
    df_s3 = io_solids.read_csv_as_df_s3(s3_coordninates)
    yield Output(df_local, "df_from_local")
    yield Output(df_s3, "df_from_s3")
    

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
    df_input = get_data()
    df_processed = logic.transform_data(df_input)
    io_solids.save_df(df_processed)