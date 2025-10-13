# Climate Data Scraping – Yeosu

## Overview
This module is designed to scrape daily climate data for Yeosu, South Korea, from [en.tutiempo.net](https://en.tutiempo.net). The dataset spans from **2006 to August 2025** and includes key meteorological variables such as temperature, humidity, precipitation, wind, and visibility.

The scraping process ensures data consistency, handles missing values, and logs errors for traceability.

## Data Sources
- **Website:** [en.tutiempo.net](https://en.tutiempo.net)  
- **Data frequency:** Daily  

**Variables collected:**
- Day (`Day`)  
- Temperature: Average (`T`), Maximum (`TM`), Minimum (`Tm`)  
- Sea level pressure (`SLP`)  
- Humidity (`H`)  
- Precipitation (`PP`)  
- Visibility (`VV`)  
- Wind speed (`V`, `VM`, `VG`)  
- Rain (`RA`), Snow (`SN`), Thunderstorm (`TS`), Fog (`FG`)  
- Month (`Month`), Year (`Year`)  

## Methodology

### Scraper Implementation
- Built using `requests` and `BeautifulSoup`.  
- Scrapes monthly tables for each year.  
- Normalizes rows to ensure **15+2 columns** (meteorological variables + month/year).  
- Converts numeric columns to appropriate `float` or `int` types.  
- Implements polite scraping with **1-second delays** between requests.  
- Logs all events, warnings, and errors to `scraping.log`.  

### Running the Scraper
- The `run_scraping.py` script automates scraping for all years from **2006 to 2025**.  
- Creates directories for **raw** and **processed** data.  
- Saves each year's data as a CSV in `data/raw`.  
- Merges all years into a single CSV in `data/processed`.  

### Error Handling
- HTTP errors or missing tables are logged with warnings.  
- Skipped months are reported but do not halt the process.  
- Ensures only valid rows are stored in the dataset.  
