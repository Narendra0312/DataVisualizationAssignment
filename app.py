
import streamlit as st
import pandas as pd
import numpy as np

# ----------------------------
# Load parquet files
# ----------------------------
agg1 = pd.read_parquet(r"C:\Users\Komak\Downloads\agg1.parquet")
agg2 = pd.read_parquet(r"C:\Users\Komak\Downloads\agg2.parquet")
agg3 = pd.read_parquet(r"C:\Users\Komak\Downloads\agg3.parquet")

st.title("📈 Interactive Stock Analysis Dashboard")

st.write("""
This dashboard displays **daily stock performance**, built with data cleaned and aggregated from your raw dataset.
Use the filters below to explore close prices, volumes, and daily returns.
""")

# ----------------------------
# Sidebar Filters (Just like your example)
# ----------------------------
tickers = sorted(agg1["ticker"].unique())
sectors = sorted(agg2["sector"].unique())

with st.container(border=True):
    selected_tickers = st.multiselect("Select Tickers", tickers, default=tickers[:3])
    show_rolling = st.toggle("Apply 7-day Rolling Average")
    show_returns = st.toggle("Show Daily Returns (Agg3)")
    show_volume = st.toggle("Show Sector Volume (Agg2)")

# ----------------------------
# Filter Aggregation Data
# ----------------------------
filtered_agg1 = agg1[agg1["ticker"].isin(selected_tickers)]
filtered_agg3 = agg3[agg3["ticker"].isin(selected_tickers)]

if show_rolling:
    filtered_agg1["avg_close_price"] = (
        filtered_agg1.groupby("ticker")["avg_close_price"]
        .rolling(7).mean().reset_index(level=0, drop=True)
    )

# ----------------------------
# Tabs (Chart + Dataframe) — EXACT STYLE YOU WANT
# ----------------------------
tab1, tab2 = st.tabs(["📊 Charts", "📄 Data"])

# ----------------------------
# Tab 1 → Charts
# ----------------------------
with tab1:

    # Daily Avg Close Line Chart
    st.subheader("📉 Daily Average Close Price")
    st.line_chart(
        filtered_agg1.pivot(index="trade_date", columns="ticker", values="avg_close_price"),
        height=300
    )

    # Optional: Sector Volume Bar Chart
    if show_volume:
        st.subheader("📦 Average Volume by Sector")
        st.bar_chart(
            agg2.pivot(index="sector", columns=None, values="avg_volume"),
            height=300
        )

    # Optional: Daily Returns
    if show_returns:
        st.subheader("📈 Daily Returns (Simple Return %)")
        st.line_chart(
            filtered_agg3.pivot(index="trade_date", columns="ticker", values="daily_return"),
            height=300
        )


# ----------------------------
# Tab 2 → Dataframes
# ----------------------------
with tab2:
    st.subheader("Daily Average Close")
    st.dataframe(filtered_agg1, height=250, width="stretch")

    if show_volume:
        st.subheader("Average Volume by Sector")
        st.dataframe(agg2, height=250, width="stretch")

    if show_returns:
        st.subheader("Daily Returns")
        st.dataframe(filtered_agg3, height=250, width="stretch")
