import os
from src.data import load_data, filter_by_store_and_date

DATA_PATH = os.path.join(os.path.dirname(__file__), '..', 'data', 'retail_sales.csv')

def test_load_data():
    df = load_data(DATA_PATH)
    assert not df.empty
    assert 'date' in df.columns
    assert 'store_id' in df.columns
    assert 'sales' in df.columns

def test_filter_by_store_and_date():
    df = load_data(DATA_PATH)
    store = df['store_id'].iloc[0]
    start = df['date'].min()
    end = df['date'].max()
    filtered = filter_by_store_and_date(df, store, start, end)
    assert all(filtered['store_id'] == store)
    assert filtered['date'].min() >= start
    assert filtered['date'].max() <= end
