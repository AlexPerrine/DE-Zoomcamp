import pandas as pd
import re

if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test




@transformer
def transform(data, *args, **kwargs):
    passenger_distance = data[(data['passenger_count'] == 0) | (data['trip_distance'] == 0)].index
    data.drop(passenger_distance, inplace=True)
    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data.columns = (data.columns
                .str.replace('(?<=[a-z])(?=[A-Z])', '_', regex=True).str.lower())
    return data


@test
def test_passenger(output, *args) -> None:
    """
    Testing passenger count does not have a 0
    """
    assert output['passenger_count'].isin([0]).sum() == 0, 'There are rides with 0 passengers'


@test
def test_distance(output, *args) -> None:
    """
    Testing trip distance is greater than 0.
    """
    assert output['trip_distance'].isin([0]).sum() == 0, 'There are rides with 0 distance'