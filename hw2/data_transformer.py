if 'transformer' not in globals():
    from mage_ai.data_preparation.decorators import transformer
if 'test' not in globals():
    from mage_ai.data_preparation.decorators import test


@transformer
def transform(data, *args, **kwargs):

    data = data[data['passenger_count']>0]
    data = data[data['trip_distance']>0]

    data['lpep_pickup_date'] = data['lpep_pickup_datetime'].dt.date
    data.columns = [''.join(['_'+c.lower() if c.isupper() 
                    and s[max(0,i-1)].islower() else c.lower() 
                    for i, c in enumerate(s)])
                    for s in data.columns]

    return data


@test
def test_output(output, *args) -> None:
    """
    Template code for testing the output of the block.
    """
    assert output['vendor_id'].isin(output['vendor_id'].unique()).all(), 'The output is not one of the existing values in the column (currently)'
    assert output['passenger_count'].isin([0]).sum() == 0, '0 passengers encountered'
    assert (output['trip_distance'] <= 0).sum() == 0, 'Trip with 0 distance encountered'