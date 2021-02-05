from dagster import solid
import pandas as pd
from .constants import *

@solid
def transform_data(context, df: PandasDataFrame) -> PandasDataFrame:
    context.log.info("Performing the most simple transformation, which is no transformation")
    return df