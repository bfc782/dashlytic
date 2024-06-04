import pandas as pd

fake_data = [
    {"amount": 100, "customer": "abc", "transaction_date": "2024-05-31"},
    {"amount": 120, "customer": "abc", "transaction_date": "2024-05-30"},
    {"amount": 105, "customer": "abc", "transaction_date": "2024-05-29"},
    {"amount": 110, "customer": "abc", "transaction_date": "2024-05-28"},
    {"amount": 75, "customer": "abc", "transaction_date": "2024-05-27"},
    {"amount": 120, "customer": "def", "transaction_date": "2024-05-31"},
    {"amount": 130, "customer": "def", "transaction_date": "2024-05-30"},
    {"amount": 140, "customer": "def", "transaction_date": "2024-05-29"},
    {"amount": 120, "customer": "def", "transaction_date": "2024-05-28"},
    {"amount": 120, "customer": "def", "transaction_date": "2024-05-27"},
    {"amount": 120, "customer": "ghi", "transaction_date": "2024-05-31"},
    {"amount": 150, "customer": "ghi", "transaction_date": "2024-05-30"},
    {"amount": 150, "customer": "ghi", "transaction_date": "2024-05-29"},
    {"amount": 140, "customer": "ghi", "transaction_date": "2024-05-28"},
    {"amount": 150, "customer": "ghi", "transaction_date": "2024-05-27"},
]

df_fake_data = pd.DataFrame.from_records(fake_data)
