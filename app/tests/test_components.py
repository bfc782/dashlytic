# %%
from ..components import Components
from ..data import df_fake_data as data


c = Components(data)
d = data


def test_init_data_dims():
    c = Components(d)
    expected = ["amount", "customer", "product", "transaction_date"]
    output = c.data_dims

    assert expected == output


# %%
