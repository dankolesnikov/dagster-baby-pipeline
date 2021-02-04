from dagster import solid
import pandas as pd
import dagster_pandas as d_pd

@solid
def transform_data(context, df):
    context.log.info("Performing the most simple transformation, which is no transformation")
    return df