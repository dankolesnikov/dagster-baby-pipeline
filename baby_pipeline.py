from dagster import pipeline, solid
import io_solids as io
import logic

@pipeline
def pipeline():
    df_input = io.read_csv_as_df()
    df_processed = logic.transform_data(df_input)
    io.save_df(df_processed)