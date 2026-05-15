# demo_web_scraping.py
"""
Quick demo: Fetch data from a public API or simple webpage.
Illustrates how I can collect raw data before processing it with the main pipeline.
"""

import requests
import pandas as pd

# Example: Fetch public COVID-19 data (or any other open data)
url = "https://api.publicapis.org/entries"
response = requests.get(url)
data = response.json()

# Convert to DataFrame (simulates 'raw data' from web)
df_raw = pd.DataFrame(data['entries'])
df_raw.to_csv('sample_web_data.csv', index=False)
print("Demo: Fetched data from web and saved as CSV.")
## 🔧 Extensibility & Custom Services

This project demonstrates a **general-purpose data processing pipeline** (cleaning → calculation → Excel report → charts).

For **web scraping** needs, I can:

1. Write a **custom data collection script** based on your target website (supports static pages, APIs, dynamic content, etc.)
2. Feed the collected data **directly into this data processing pipeline**
3. Deliver the final output: **clean Excel report + visual charts + full source code**

👉 In short, you just tell me "where to scrape from and what data to collect", and I can deliver a complete solution from **collection to report**.

📌 Ideal for: competitor price monitoring, job board scraping, real estate data aggregation, sentiment analysis, and other **recurring or long-term data needs**.
