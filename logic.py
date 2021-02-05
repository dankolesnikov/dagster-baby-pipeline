from dagster import solid
import pandas as pd
from dagster_baby_pipeline import constants

@solid
def transform_data(context, df: constants.PandasDataFrame) -> constants.PandasDataFrame:
    context.log.info("Performing the most simple transformation, which is no transformation")
    return df