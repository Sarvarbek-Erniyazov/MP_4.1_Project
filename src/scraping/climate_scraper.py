import requests
from bs4 import BeautifulSoup
import pandas as pd
import logging
import time
import os

# Setup logging
log_path = os.path.join(os.path.dirname(os.path.dirname(__file__)), "..", "logs")
os.makedirs(log_path, exist_ok=True)
logging.basicConfig(
    filename=os.path.join(log_path, "scraping.log"),
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

class ClimateYeosuScraper:
    """
    Scraper for Yeosu climate data from en.tutiempo.net.
    """

    BASE_URL = "https://en.tutiempo.net/climate/{month}-{year}/ws-471680.html"

    def __init__(self, year):
        self.year = year

    def scrape_year(self, last_month=12):
        all_data = []
        months = [f"{i:02d}" for i in range(1, last_month + 1)]

        for month in months:
            url = self.BASE_URL.format(month=month, year=self.year)
            logging.info(f"Scraping {month}-{self.year} ...")
            try:
                r = requests.get(url)
                r.raise_for_status()
                soup = BeautifulSoup(r.text, "html.parser")

                table = soup.find("table", class_="medias mensuales numspan")
                if not table:
                    logging.warning(f"No table found for {month}-{self.year}")
                    continue

                for tr in table.find_all("tr")[1:]:
                    cols = [td.get_text(strip=True) for td in tr.find_all("td")]

                    if cols and cols[0].isdigit():
                        # Ensure row has exactly 15 columns
                        if len(cols) < 15:
                            cols += [''] * (15 - len(cols))
                        elif len(cols) > 15:
                            cols = cols[:15]

                        cols[0] = int(cols[0])  # Day
                        cols.append(int(month))
                        cols.append(self.year)

                        all_data.append(cols)

                time.sleep(1)  # polite delay

            except requests.HTTPError as http_err:
                logging.error(f"HTTP error {month}-{self.year}: {http_err}")
            except Exception as e:
                logging.error(f"Error {month}-{self.year}: {e}")

        if all_data:
            columns = [
                "Day", "T", "TM", "Tm", "SLP", "H", "PP",
                "VV", "V", "VM", "VG", "RA", "SN", "TS", "FG",
                "Month", "Year"
            ]
            df = pd.DataFrame(all_data, columns=columns)
            numeric_cols = ["T", "TM", "Tm", "SLP", "H", "PP", "VV", "V", "VM", "VG"]
            for col in numeric_cols:
                df[col] = pd.to_numeric(df[col], errors='coerce')
            logging.info(f"{self.year} scraped successfully, {len(df)} rows.")
            return df
        else:
            logging.warning(f"No data scraped for {self.year}.")
            return pd.DataFrame()
