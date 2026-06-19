"""
News Data Fetch + Clean + Excel + Chart
Dependencies: requests, pandas, openpyxl, matplotlib
Installation:
pip install requests pandas openpyxl matplotlib
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# ==================== Configuration ====================
"""
News Data Fetch + Clean + Excel + Chart
Dependencies: requests, pandas, openpyxl, matplotlib
Installation:
pip install requests pandas openpyxl matplotlib
"""

import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# ==================== Configuration ====================
import os  # Make sure os has been imported.
API_KEY = os.getenv("NEWS_API_KEY", "your-api-key-here")
QUERY = "technology"              # Search keyword, can be changed to "business", "china", etc.
DAYS_BACK = 3                     # Fetch news from the past N days (max 30)
PAGE_SIZE = 50                    # Articles per page, max 100
OUTPUT_EXCEL = "news_data.xlsx"
OUTPUT_CHART = "news_chart.png"
# ======================================================

def fetch_news(api_key, query, days_back=3, page_size=50):
    """
    Fetch news data from NewsAPI
    """
    # Calculate the 'from' date (days_back days ago)
    from_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")
    # Note: Free tier only allows data from the last 30 days
    url = "https://newsapi.org/v2/everything"
    params = {
        "q": query,
        "from": from_date,
        "sortBy": "publishedAt",
        "pageSize": page_size,
        "apiKey": api_key,
        "language": "en",          # English, can be changed to "zh" but need to verify support
    }
    
    print(f"Requesting news data: {query} ...")
    response = requests.get(url, params=params)
    
    # ========== Diagnostic Code ==========
    print(f"Status code: {response.status_code}")
    data = response.json()
    print(f"API response structure: status={data.get('status')}, totalResults={data.get('totalResults')}")
    if data.get('message'):
        print(f"API message: {data['message']}")
    # ====================================
    
    if response.status_code != 200:
        print(f"Request failed: {response.status_code} - {response.text}")
        return None
    
    # Note: data already parsed above, use directly, do not call response.json() again
    
    if data.get("status") != "ok":
        print(f"API error: {data.get('message', 'Unknown error')}")
        return None
    
    articles = data.get("articles", [])
    print(f"Fetched {len(articles)} articles")
    return articles

def clean_news_data(articles):
    """
    Clean data:
    - Remove rows with null values
    - Format dates
    - Remove duplicates (based on title)
    - Handle missing source names
    """
    if not articles:
        return pd.DataFrame()
    
    df = pd.DataFrame(articles)
    
    # Select required columns (can be adjusted as needed)
    keep_cols = ["source", "author", "title", "description", 
                 "url", "publishedAt", "content"]
    df = df[[c for c in keep_cols if c in df.columns]]
    
    # Extract source_name from source dictionary
    if "source" in df.columns:
        df["source_name"] = df["source"].apply(lambda x: x.get("name") if isinstance(x, dict) else None)
        df.drop(columns=["source"], inplace=True)
    
    # Remove rows with empty title
    df.dropna(subset=["title"], inplace=True)
    
    # Remove duplicate titles (keep first occurrence)
    df.drop_duplicates(subset=["title"], keep="first", inplace=True)
    
    # Date formatting: convert publishedAt to datetime object
    if "publishedAt" in df.columns:   # ← note the 4-space indent on this line
        df["publishedAt"] = pd.to_datetime(df["publishedAt"], errors="coerce")
        # Remove timezone info if present (Excel does not support timezone)
        if df["publishedAt"].dt.tz is not None:
            df["publishedAt"] = df["publishedAt"].dt.tz_localize(None)
        # Remove rows with invalid dates
        df.dropna(subset=["publishedAt"], inplace=True)
    
    # Fill missing author and description with "N/A"
    df["author"] = df["author"].fillna("N/A")
    df["description"] = df["description"].fillna("No description")
    df["content"] = df["content"].fillna("No content")
    
    # Reset index
    df.reset_index(drop=True, inplace=True)
    
    print(f"After cleaning, {len(df)} valid records remain")
    return df

def save_to_excel(df, filename):
    """
    Save DataFrame to Excel file
    """
    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="News", index=False)
        # Adjust column widths
        worksheet = writer.sheets["News"]
        for column in worksheet.columns:
            max_length = 0
            col_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = min(max_length + 2, 50)
            worksheet.column_dimensions[col_letter].width = adjusted_width
    print(f"Data saved to {filename}")

def generate_chart(df, output_path):
    """
    Generate chart: bar chart showing article count per news source
    """
    if df.empty:
        print("No data, cannot generate chart")
        return
    
    # Count articles per source
    source_counts = df["source_name"].value_counts().head(10)  # Take top 10
    
    if source_counts.empty:
        print("Not enough source data to generate chart")
        return
    
    plt.figure(figsize=(10, 6))
    source_counts.plot(kind="barh", color="skyblue")
    plt.xlabel("Number of Articles")
    plt.ylabel("News Source")
    plt.title(f"Top 10 News Sources - {QUERY}")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.show()
    print(f"Chart saved to {output_path}")

def main():
    # 1. Fetch news
    if API_KEY == "YOUR_API_KEY":
        print("Error: Please set a valid API_KEY first!")
        return
    
    articles = fetch_news(API_KEY, QUERY, DAYS_BACK, PAGE_SIZE)
    if not articles:
        print("Unable to fetch data. Exiting.")
        return
    
    # 2. Clean data
    df = clean_news_data(articles)
    if df.empty:
        print("No valid data after cleaning.")
        return
    
    # 3. Save to Excel
    save_to_excel(df, OUTPUT_EXCEL)
    
    # 4. Generate chart
    generate_chart(df, OUTPUT_CHART)
    
    print("All done!")

if __name__ == "__main__":
    main()
QUERY = "technology"              # Search keyword, can be changed to "business", "china", etc.
DAYS_BACK = 3                     # Fetch news from the past N days (max 30)
PAGE_SIZE = 50                    # Articles per page, max 100
OUTPUT_EXCEL = "news_data.xlsx"
OUTPUT_CHART = "news_chart.png"
# ======================================================

def fetch_news(api_key, query, days_back=3, page_size=50):
    """
    Fetch news data from NewsAPI
    """
    # Calculate the 'from' date (days_back days ago)
    from_date = (datetime.now() - timedelta(days=days_back)).strftime("%Y-%m-%d")
    # Note: Free tier only allows data from the last 30 days
    url = "https://newsapi.org/v2/everything"
    params = {
    "q": query,
    "from": from_date,
    "sortBy": "publishedAt",
    "pageSize": page_size,
    "apiKey": api_key,
    "language": "en"
}
    
    print(f"Requesting news data: {query} ...")
    response = requests.get(url, params=params)
    
    # ========== Diagnostic Code ==========
    print(f"Status code: {response.status_code}")
    data = response.json()
    print(f"API response structure: status={data.get('status')}, totalResults={data.get('totalResults')}")
    if data.get('message'):
        print(f"API message: {data['message']}")
    # ====================================
    
    if response.status_code != 200:
        print(f"Request failed: {response.status_code} - {response.text}")
        return None
    
    # Note: data already parsed above, use directly, do not call response.json() again
    
    if data.get("status") != "ok":
        print(f"API error: {data.get('message', 'Unknown error')}")
        return None
    
    articles = data.get("articles", [])
    print(f"Fetched {len(articles)} articles")
    return articles

def clean_news_data(articles):
    """
    Clean data:
    - Remove rows with null values
    - Format dates
    - Remove duplicates (based on title)
    - Handle missing source names
    """
    if not articles:
        return pd.DataFrame()
    
    df = pd.DataFrame(articles)
    
    # Select required columns (can be adjusted as needed)
    keep_cols = ["source", "author", "title", "description", 
                 "url", "publishedAt", "content"]
    df = df[[c for c in keep_cols if c in df.columns]]
    
    # Extract source_name from source dictionary
    if "source" in df.columns:
        df["source_name"] = df["source"].apply(lambda x: x.get("name") if isinstance(x, dict) else None)
        df.drop(columns=["source"], inplace=True)
    
    # Remove rows with empty title
    df.dropna(subset=["title"], inplace=True)
    
    # Remove duplicate titles (keep first occurrence)
    df.drop_duplicates(subset=["title"], keep="first", inplace=True)
    
    # Date formatting: convert publishedAt to datetime object
    if "publishedAt" in df.columns:   # ← note the 4-space indent on this line
        df["publishedAt"] = pd.to_datetime(df["publishedAt"], errors="coerce")
        # Remove timezone info if present (Excel does not support timezone)
        if df["publishedAt"].dt.tz is not None:
            df["publishedAt"] = df["publishedAt"].dt.tz_localize(None)
        # Remove rows with invalid dates
        df.dropna(subset=["publishedAt"], inplace=True)
    
    # Fill missing author and description with "N/A"
    df["author"] = df["author"].fillna("N/A")
    df["description"] = df["description"].fillna("No description")
    df["content"] = df["content"].fillna("No content")
    
    # Reset index
    df.reset_index(drop=True, inplace=True)
    
    print(f"After cleaning, {len(df)} valid records remain")
    return df

def save_to_excel(df, filename):
    """
    Save DataFrame to Excel file
    """
    with pd.ExcelWriter(filename, engine="openpyxl") as writer:
        df.to_excel(writer, sheet_name="News", index=False)
        # Adjust column widths
        worksheet = writer.sheets["News"]
        for column in worksheet.columns:
            max_length = 0
            col_letter = column[0].column_letter
            for cell in column:
                try:
                    if len(str(cell.value)) > max_length:
                        max_length = len(str(cell.value))
                except:
                    pass
            adjusted_width = min(max_length + 2, 50)
            worksheet.column_dimensions[col_letter].width = adjusted_width
    print(f"Data saved to {filename}")

def generate_chart(df, output_path):
    """
    Generate chart: bar chart showing article count per news source
    """
    if df.empty:
        print("No data, cannot generate chart")
        return
    
    # Count articles per source
    source_counts = df["source_name"].value_counts().head(10)  # Take top 10
    
    if source_counts.empty:
        print("Not enough source data to generate chart")
        return
    
    plt.figure(figsize=(10, 6))
    source_counts.plot(kind="barh", color="skyblue")
    plt.xlabel("Number of Articles")
    plt.ylabel("News Source")
    plt.title(f"Top 10 News Sources - {QUERY}")
    plt.tight_layout()
    plt.savefig(output_path, dpi=150)
    plt.show()
    print(f"Chart saved to {output_path}")

def main():
    # 1. Fetch news
    if API_KEY == "YOUR_API_KEY":
        print("Error: Please set a valid API_KEY first!")
        return
    
    articles = fetch_news(API_KEY, QUERY, DAYS_BACK, PAGE_SIZE)
    if not articles:
        print("Unable to fetch data. Exiting.")
        return
    
    # 2. Clean data
    df = clean_news_data(articles)
    if df.empty:
        print("No valid data after cleaning.")
        return
    
    # 3. Save to Excel
    save_to_excel(df, OUTPUT_EXCEL)
    
    # 4. Generate chart
    generate_chart(df, OUTPUT_CHART)
    
    print("All done!")

if __name__ == "__main__":
    main()