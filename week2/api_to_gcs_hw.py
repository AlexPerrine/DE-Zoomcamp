import io
import pandas as pd
import requests
import re
if 'data_loader' not in globals():
    from mage_ai.data_preparation.decorators import data_loader
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@data_loader
def load_data_from_api(*args, **kwargs):
    """
    Template for loading data from API
    """
    urls = ['https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-10.csv.gz',
    'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-11.csv.gz',
    'https://github.com/DataTalksClub/nyc-tlc-data/releases/download/green/green_tripdata_2020-12.csv.gz']

    df = pd.DataFrame()

    taxi_dtypes = {
                    'VendorID':pd.Int64Dtype(),
                    'passenger':pd.Int64Dtype(),
                    'trip_distance':float,
                    'RatecodeID':pd.Int64Dtype(),
                    'store_and_fwd_flag':str,
                    'PULocationID': pd.Int64Dtype(),
                    'DOLcationID' :pd.Int64Dtype(),
                    'payment_type': pd.Int64Dtype(),
                    'fare_amount': float,
                    'extra': float,
                    'mta_tax': float,
                    'tip_amount':float,
                    'tolls_amount':float,
                    'improvement_surcharge':float,
                    'total_amount':float,
                    'congestion_surcharge':float
                }
    parse_dates = ['lpep_pickup_datetime','lpep_dropoff_datetime']

    for url in urls:
        response = requests.get(url)
        if response.status_code == 200:
            data = pd.read_csv(url, sep=",", compression = "gzip", dtype = taxi_dtypes, parse_dates = parse_dates)
            df = pd.concat([df,data], ignore_index = True)
            print(f'concate of {url} successful.')
        else:
            print(f'Concate failed.')
    
    return df