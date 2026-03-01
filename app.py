import streamlit as st
import pandas as pd
import plotly.express as px
from autogluon.tabular import TabularPredictor

st.title("Customer Churn ML Dashboard")
df = pd.read_csv("data.csv")
predictor = TabularPredictor.load("models/")

contract_filter = st.selectbox(
    "Select Contract Type",
    df["contract_type"].unique()
)

filtered_df = df[df["contract_type"] == contract_filter]

# Graph 1: Churn Distribution
fig1 = px.histogram(
    filtered_df,
    x="churn",
    title="Churn Distribution"
)
st.plotly_chart(fig1)

# Graph 2: Monthly Charge vs Age
fig2 = px.scatter(
    filtered_df,
    x="age",
    y="monthly_charge",
    color="churn",
    title="Age vs Monthly Charge"
)
st.plotly_chart(fig2)


# Graph 3: Feature Importance
importance = pd.read_csv("feature_importance.csv")

fig3 = px.bar(
    importance,
    x="importance",
    y="Unnamed: 0",
    orientation="h",
    title="Feature Importance"
)
st.plotly_chart(fig3)

# Prediction Section

st.subheader("Predict New Customer")

age = st.slider("Age", 18, 70, 30)
monthly = st.slider("Monthly Charge", 300, 2000, 800)
contract = st.selectbox("Contract Type", df["contract_type"].unique())

input_data = pd.DataFrame({
    "age": [age],
    "monthly_charge": [monthly],
    "contract_type": [contract]
})

if st.button("Predict"):
    prediction = predictor.predict(input_data)
    st.success(f"Prediction: {prediction.values[0]}")

# The End