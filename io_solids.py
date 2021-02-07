from dagster import solid, composite_solid, OutputDefinition, Output
import pandas as pd
from dagster_baby_pipeline import constants, utils
from dagster_aws.s3 import s3_resource


@solid(output_defs=[
        OutputDefinition(name="local_path", is_required=False),
        OutputDefinition(name="s3_coordninates", is_required=False),
    ])
def get_data_location(context, path: str):
    if path.startswith("s3://"):
        bucket, key = utils.parse_s3_path(path)
        yield Output((bucket,key), "s3_coordninates")
    else:
        yield Output(path, "local_path")

@solid
def read_csv_as_df_locally(context, local_path: str) -> constants.PandasDataFrame:
    context.log.info(f"Reading csv data locally from {local_path}")
    return pd.read_csv(local_path)

@solid
def read_csv_as_df_s3(context, s3_coordninates) -> constants.PandasDataFrame:
    bucket = s3_coordninates[0]
    key = s3_coordninates[1]
    context.log.info(f"Got S3 Coordniates: {bucket}/{key}")
    return pd.DataFrame()

    # csv_file = get_from_s3(bucket=bucket, key=key)
    # return pd.read_csv(csv_file)

"""
Get any file from S3 given proper bucket, key
"""
@solid(required_resource_keys={'s3'})
def get_from_s3(context, bucket: str, key: str):
    context.log.info(f"Attempting to get file from S3 from {bucket}/{key}")
    return context.resource.s3.get_object(Bucket=bucket, Key=key)

@solid
def save_df(context, df: constants.PandasDataFrame, path: str) -> None:
    if path.startswith("s3://"):
        context.log.info(f"Saving DataFrame as CSV to S3: {path}")
    else:
        context.log.info(f"Saving DataFrame as CSV to Local Storage: {path}")
        df.to_csv(path, index=False)

        
