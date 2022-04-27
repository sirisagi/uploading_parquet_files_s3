import boto3
import pandas as pd
from io import BytesIO
import os


def upload_files(event, context):
    bucket_name = os.environ.get('BUCKET_NAME')
    file_prefix = os.environ.get('FILE_PREFIX')
    baseline_file = os.environ.get('BASELINE_FILE')
    bucket, filename = bucket_name, file_prefix
    s3 = boto3.resource('s3')
    obj = s3.Object(bucket, filename)
    with BytesIO(obj.get()['Body'].read()) as bio:
        df = pd.read_json(bio, lines=True)
        splits = list(df.groupby("order_status"))
        for split in splits:
            s3_url = f'{baseline_file}/{split[0]}.parquet.gzip'
            split[1].to_parquet(s3_url, compression='gzip')


upload_files(None, None)
