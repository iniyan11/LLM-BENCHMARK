import streamlit as st
import pandas as pd
import plotly.express as px

df = pd.read_csv("results.csv")

st.title("LLM Benchmark Dashboard")

# Average metrics per model
avg_df = df.groupby("model").mean(numeric_only=True).reset_index()

st.subheader("Average Latency")
fig1 = px.bar(avg_df, x="model", y="latency", color="model")
st.plotly_chart(fig1)

st.subheader("Average Memory Usage")
fig2 = px.bar(avg_df, x="model", y="memory_MB", color="model")
st.plotly_chart(fig2)

st.subheader("Average Answer Quality")
fig3 = px.bar(avg_df, x="model", y="quality", color="model")
st.plotly_chart(fig3)

# Best model selection
best_model = avg_df.sort_values("quality", ascending=False).iloc[0]["model"]

st.success(f"🏆 Best Quality Model: {best_model}")

# Full table
st.subheader("Full Results")
st.dataframe(df)