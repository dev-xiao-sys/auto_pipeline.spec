# Data Automation Pipeline

**Clean data → Calculate metrics → Excel report + Charts**

This project demonstrates a complete data processing workflow. It reads messy data (CSV/Excel), cleans it, calculates key metrics, and outputs a professional Excel report with auto‑adjusted columns and a visualization chart.

> ✅ **For potential clients:** This is a working demo of my data automation skills. I can adapt this pipeline to your specific needs — whether it's web scraping, data cleaning, recurring reports, or multi‑source data integration.

---

## 🔧 What This Demo Shows

- **Read data** from CSV / Excel (or built‑in demo data)
- **Clean & validate** (remove duplicates, handle missing values, fix data types)
- **Calculate metrics** (e.g., profit = revenue – cost)
- **Generate Excel report** with auto‑adjusted column widths (no more `####` in cells)
- **Create visualization chart** (trend line, bar chart, etc.)
- **Full logging** + command‑line support

**Tech stack:** Python, Pandas, Matplotlib, OpenPyXL

---

## 📌 For Web Scraping & Multi‑Site Projects

I separate the **scraping** and **processing** stages:

1. **Scraping stage** – I write custom extractors per website / API / state  
   (supports static pages, dynamic content, JSON APIs, login sessions, pagination)
2. **Processing stage** – I feed the extracted data into this pipeline → clean Excel + charts

### Multi‑State / Multi‑Site Approach (e.g., FL, GA, NC, SC, TN, AL, LA)

When extracting data from **multiple websites with different structures**, I do:

| Step | What I do |
|------|-----------|
| 1 | **Inspect & document** each target site (layout, API, fields) |
| 2 | **Build a separate extractor** for each site / state |
| 3 | **Normalize** the data into a unified format |
| 4 | **Feed into this pipeline** for cleaning + Excel + charts |

Why this works:
- ✅ **Reliable** – one site changing doesn't break the others  
- ✅ **Maintainable** – each state can be updated independently  
- ✅ **Scalable** – new states / sites added without rewriting everything

📩 **Need multi‑state public records or business data?** I can deliver separate scrapers for FL, GA, NC, SC, TN, AL, LA and combine everything into a clean, unified Excel file.

---

## 🧪 Quick Start (Run the Demo)

```bash
# Clone & install dependencies
pip install pandas matplotlib openpyxl

# Run with built‑in demo data
python auto_pipeline.py

# Or run with your own file
python auto_pipeline.py --input your_data.csv
