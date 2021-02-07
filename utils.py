"""
Convert S3 string path into bucket, key pair
path - S3 string like s3://fable_bucket/data/file.csv
"""
def parse_s3_path(path: str):
    if (not path.startswith("s3://")):
        raise ValueError("S3 path isn't in the precise format")
    lst = path.replace("s3://", "").split('/')
    bucket = lst[0]
    key = "/".join(lst[1:])
    return bucket, key
