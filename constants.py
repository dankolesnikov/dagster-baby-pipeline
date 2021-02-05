from dagster_pandas import *

PandasDataFrame = create_dagster_pandas_dataframe_type(
    name="PandasDataFrame"
)