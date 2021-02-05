from dagster import solid
import pandas as pd
from dagster_baby_pipeline import constants

@solid
def read_csv_as_df(context, path: str) -> constants.PandasDataFrame:
    if path.startswith("s3://"):
        print("S3 path detected")
        context.log.info(f"Getting csv data from S3 {path}")
    else:
        context.log.info(f"Getting csv data locally from {path}")
        return pd.read_csv(path)

@solid
def save_df(context, df: constants.PandasDataFrame, path: str) -> None:
    if (path.startswith("s3://")):
        context.log.info(f"Saving DataFrame as CSV to S3: {path}")
    else:
        context.log.info(f"Saving DataFrame as CSV to Local Storage: {path}")
        df.to_csv(path, index=False)

        
