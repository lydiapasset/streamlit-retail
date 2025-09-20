import streamlit as st
import pandas as pd
from src.data import load_data, filter_by_store_and_date
from src.model import train_simple_model, predict

st.set_page_config(page_title="Retail Sales Explorer", layout="wide")
st.title("Retail Sales Explorer & Forecast")

df = load_data("data/retail_sales.csv")

st.sidebar.header("Filters")
stores = df['store_id'].unique().tolist()
store = st.sidebar.selectbox("Store", options=stores)

min_date = df['date'].min()
max_date = df['date'].max()
date_range = st.sidebar.date_input("Date range", value=(min_date, max_date))

filtered = filter_by_store_and_date(df, store, date_range[0], date_range[1])

st.header("Data preview")
st.dataframe(filtered.head(100))

st.header("Sales time series")
st.line_chart(filtered.set_index('date')['sales'])

st.header("Train simple regression model to predict sales")
if st.button("Train model"):
    model, X_test, y_test = train_simple_model(filtered)
    preds = predict(model, X_test)
    res = pd.DataFrame({'y_true': y_test, 'y_pred': preds})
    st.write("Test results (first 20 rows):")
    st.dataframe(res.head(20))
    st.write(f"MAE: {abs(res['y_true'] - res['y_pred']).mean():.2f}")
