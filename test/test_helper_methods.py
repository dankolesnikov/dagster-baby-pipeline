import pytest
from dagster_baby_pipeline import utils

"""
Happy path
"""
def test_parse_s3_path():
    path = "s3://some_bucket/some_folder/file.csv"
    bucket = "some_bucket"
    key = "some_folder/file.csv"
    assert bucket, key == utils.parse_s3_path(path)

"""
Sad Path
"""
def test_parse_s3_path_sad():
    path = "sdsad3://some_bucket/some_folder/file.csv"
    with pytest.raises(ValueError):
        utils.parse_s3_path(path)
