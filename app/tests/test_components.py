
import pytest
from pandas.testing import assert_frame_equal

from ..components import Components
from ..data import df_fake_data as fake_data


@pytest.fixture
def fake_component():
    return Components(fake_data)


def test_init_data_dims(fake_component):
    expected = ["amount", "customer", "product", "transaction_date"]
    output = fake_component.data_dim_options

    assert expected == output

def test_init_data_dim_val(fake_component):
    expected = "customer"
    output = fake_component.dropdown_dim.value

    assert expected == output

def test_get_data_dim(fake_component):
    time_ix = fake_component.time_ix
    measure = fake_component.measure
    col = "customer"
    expected = [
        {
            "amount": 100,
            "customer": "abc",
            # "product": "uvw",
            "transaction_date": "2024-05-31",
        },
        {
            "amount": 120,
            "customer": "abc",
            "product": "xyz",
            "transaction_date": "2024-05-30",
        },
        {
            "amount": 120,
            "customer": "def",
            # "product": "uvw",
            "transaction_date": "2024-05-31",
        },
    ]
    output_df = fake_component.get_data_dim(col)

    output = output_df.to_dict('records')

    assert expected == output
    # assert assert_frame_equal(expected, output)

# def test_filter_data_value_empty(fake_component):
#     expected = fake_data
#     output = fake_component.filter_data("customer", "")
    
#     assert expected == output
    