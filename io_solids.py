from dagster import solid
import pandas as pd
import dagster_pandas as d_pd

@solid
def read_csv_as_df(context, path: str):
    if path.startswith("s3://"):
        print("S3 path detected")
        context.log.info("Getting csv data from S3 {path}")
    else:
        context.log.info("Getting csv data locally from {path}")
        return pd.read_csv(path)

@solid
def save_df(context, df, path: str) -> None:
    if (path.startswith("s3://")):
        context.log.info("Saving DataFrame as CSV to S3: {path}")
    else:
        context.log.info("Saving DataFrame as CSV to Local Storage: {path}")
        df.to_csv(path, index=False)

        
