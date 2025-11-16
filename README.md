**Interactive Stock Analysis Dashboard**
This Streamlit application visualizes daily stock performance using pre-aggregated Parquet files.
It provides charts and tables for close prices, sector volume, and daily returns with interactive filters.

**Features**
Select multiple tickers
Optional 7-day rolling average
Optional daily returns line chart
Optional sector volume bar chart
Interactive tabs: Charts, Raw Data
Fast loading using Parquet files

**Data Files**
Place the following files in the /data folder:
agg1.parquet -- Daily average close price by ticker
agg2.parquet -- Average trading volume by sector
agg3.parquet -- Daily simple return per ticker

**Cleaning Steps Performed**

- Converted all column headers to snake_case
- Trimmed whitespace from both column names and data fields
- Normalized missing values ("", "NA", "N/A", "null", "-") to `pd.NA`
- Converted all date fields to YYYY-MM-DD format
- Cast numeric fields (prices, volumes, etc.) to float
- Removed all duplicate rows to ensure data consistency


cleaned.parquet —  cleaned and normalized dataset.

Dashboard Usage :
After generating all Parquet files using the data-cleaning notebook, launch the dashboard with: streamlit run app.py


