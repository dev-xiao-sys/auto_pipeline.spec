# newsapi-data-pipeline

**Stop manually collecting news data for market research.**

Tired of dealing with missing fields, duplicate articles, and timezone chaos from raw APIs? This script does one thing and does it well: fetch news data from NewsAPI, clean it, deduplicate, normalize dates, and export to Excel with a chart.

> **Note:** This is a **demonstration project** built to showcase my data pipeline workflow (fetch → clean → export). The same **pattern** can be adapted for other data sources — e.g., e‑commerce listings, financial data, social media metrics — but each source requires its own custom integration logic. If you have a specific data source in mind, I can build a tailored solution for your business needs, scoped separately per project.

---

## What this demo does

- Fetches latest news by keyword (default: `"technology"`)
- Cleans and standardizes messy API responses (missing fields → `N/A`)
- Removes duplicate articles (by title)
- Strips timezone info for Excel compatibility (no more `ValueError`)
- Exports to a clean Excel file with auto-adjusted column widths
- Generates a bar chart of the top 10 news sources

---

## Quick start

```bash
# 1. Install dependencies
pip install requests pandas openpyxl matplotlib

# 2. Set your API key (choose ONE line based on your OS):
#    Mac/Linux:  export NEWS_API_KEY="your-api-key-here"
#    Windows (CMD):        set NEWS_API_KEY="your-api-key-here"
#    Windows (PowerShell): $env:NEWS_API_KEY="your-api-key-here"

# 3. Run it
python news_crawler.py
Zero config — just set your NewsAPI key and run. Full source code included.

Example output
50 articles → 48 clean rows → news_data.xlsx → news_chart.png

Handles real-world API mess:

Missing authors → filled with N/A

Duplicate headlines → removed (first kept)

Timezone‑aware timestamps → stripped for Excel

Empty descriptions → replaced with "No description"

Performance: Processes 50 articles — from raw API to clean Excel — in about 30 seconds. (Network speed may vary.)

Configuration
Edit these variables at the top of news_crawler.py:

Variable	Default	Description
QUERY	"technology"	Search keyword (e.g., "business", "AI", "crypto")
DAYS_BACK	3	Days to look back (max 30 for free tier)
PAGE_SIZE	50	Articles per request (max 100)
OUTPUT_EXCEL	"news_data.xlsx"	Output Excel filename
OUTPUT_CHART	"news_chart.png"	Output chart filename
Who this is for
Perfect for: market researchers, small business owners, or anyone who needs daily news briefs without manually browsing 10+ sites.

Tech stack
Python 3 + requests + pandas + openpyxl + matplotlib — lightweight, dependency‑minimal, and easy to modify.

Scope note
This is a turnkey solution for public API‑based news data.
For custom scraping of websites that require:

Captcha solving

Dynamic rendering (JavaScript‑heavy pages)

IP rotation / proxy management

Advanced anti‑detection measures

...that is a separate scope and can be quoted as an additional service. Feel free to contact me for a tailored solution.

Terms
Full source code included — modify and reuse as needed.

Works out‑of‑the‑box with a valid API key. If it doesn't, I'll help you debug it — free.

