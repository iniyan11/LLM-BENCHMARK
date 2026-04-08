import streamlit as st
import pandas as pd
import plotly.express as px

# Load data
df = pd.read_csv("results.csv")

st.title("📊 LLM Benchmark Dashboard")

# Show raw data
st.subheader("📋 Raw Results")
st.dataframe(df)

# Calculate average values per model
avg_df = df.groupby("model").mean(numeric_only=True).reset_index()

# Latency Chart
st.subheader("⏱️ Average Latency (Seconds)")
fig1 = px.bar(avg_df, x="model", y="latency", color="model")
st.plotly_chart(fig1)

# Memory Chart
st.subheader("💾 Average Memory Usage (MB)")
fig2 = px.bar(avg_df, x="model", y="memory_MB", color="model")
st.plotly_chart(fig2)

# Quality Chart
st.subheader("🧠 Answer Quality (Word Count)")
fig3 = px.bar(avg_df, x="model", y="quality", color="model")
st.plotly_chart(fig3)

# Best Model Based on Quality
best_model = avg_df.sort_values("quality", ascending=False).iloc[0]["model"]

st.success(f"🏆 Best Model (Highest Quality): {best_model}")

# Fastest Model
fastest_model = avg_df.sort_values("latency").iloc[0]["model"]

st.info(f"⚡ Fastest Model: {fastest_model}")

# Least Memory Model
efficient_model = avg_df.sort_values("memory_MB").iloc[0]["model"]

st.warning(f"💡 Most Memory Efficient Model: {efficient_model}")
