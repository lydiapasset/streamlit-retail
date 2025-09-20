import pandas as pd

def load_data(path: str) -> pd.DataFrame:
    df = pd.read_csv(path, parse_dates=['date'])
    return df

def filter_by_store_and_date(df: pd.DataFrame, store_id, start_date, end_date) -> pd.DataFrame:
    # conversion sûre
    start_date = pd.to_datetime(start_date)
    end_date = pd.to_datetime(end_date)

    mask = (
        (df['store_id'] == store_id) &
        (df['date'] >= start_date) &
        (df['date'] <= end_date)
    )
    return df.loc[mask].sort_values('date').reset_index(drop=True)
