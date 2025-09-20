import pandas as pd
from sklearn.linear_model import LinearRegression
from sklearn.model_selection import train_test_split

def _prepare_features(df: pd.DataFrame) -> pd.DataFrame:
    df = df.copy()
    df['month'] = pd.to_datetime(df['date']).dt.month
    return df[['month', 'promo', 'sales']]

def train_simple_model(df: pd.DataFrame):
    df_feat = _prepare_features(df)
    X = df_feat[['month', 'promo']]
    y = df_feat['sales']
    X_train, X_test, y_train, y_test = train_test_split(X, y, test_size=0.2, random_state=42)
    model = LinearRegression()
    model.fit(X_train, y_train)
    return model, X_test, y_test

def predict(model, X):
    return model.predict(X)
