import pandas as pd
import pyarrow as pa
import pyarrow.parquet as pq
import os
from io import BytesIO
import requests
from mage_ai.settings.repo import get_repo_path
from mage_ai.io.config import ConfigFileLoader
from mage_ai.io.google_cloud_storage import GoogleCloudStorage
from os import path
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_from_google_cloud_storage(*args, **kwargs):
    url = 'https://d37ci6vzurychx.cloudfront.net/trip-data/'
    months = ['01','02','03','04','05','06','07','08','09','10','11','12']
    bucket_name = 'mage-zoomcamp-ap'
    os.environ['GOOGLE_APPLICATION_CREDENTIALS'] = '/home/src/intro-to-bq-411701-a981485785c5.json'

    df = pd.DataFrame()

    taxi_dtypes = {
                    'VendorID':pd.Int64Dtype(),
                    'passenger_count':pd.Int64Dtype(),
                    'trip_distance':float,
                    'RatecodeID':pd.Int64Dtype(),
                    'store_and_fwd_flag':str,
                    'PULocationID': pd.Int64Dtype(),
                    'DOLocationID' :pd.Int64Dtype(),
                    'payment_type': pd.Int64Dtype(),
                    'trip_type': pd.Int64Dtype(),
                    'fare_amount': float,
                    'extra': float,
                    'mta_tax': float,
                    'tip_amount':float,
                    'tolls_amount':float,
                    'ehail_fee':float,
                    'improvement_surcharge':float,
                    'total_amount':float,
                    'congestion_surcharge':float
                }

    for month in months:
        month_file = f'green_tripdata_2022-{month}.parquet'
        parquet_url = url + month_file
        response = requests.get(parquet_url)
        data = pd.read_parquet(BytesIO(response.content))
        df = pd.concat([df,data], ignore_index = True)
        df = df.astype(taxi_dtypes)
        df[['lpep_pickup_datetime','lpep_dropoff_datetime']] = df[['lpep_pickup_datetime','lpep_dropoff_datetime']].apply(pd.to_datetime)

        print(f'Concate of green_tripdata_2022-{month} sucessful.')
    return df

@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output is not None, 'The output is undefined'
