![Python](https://img.shields.io/badge/Python-3.x-blue)
![GitHub Repo Size](https://img.shields.io/github/repo-size/RR-1902/crypto-tracker-automation)



# crypto-tracker-automation
Automated cryptocurrency price tracker using Python and Selenium to scrape real-time market data from CoinMarketCap and export it to CSV.
# Cryptocurrency Price Tracker using Selenium

An automated cryptocurrency market data scraper built with Python and Selenium.  
This project extracts real-time price information from CoinMarketCap, including coin name, current price, 24-hour percentage change, and market capitalization, and stores the data in a structured CSV format for analysis.

---

## 🚀 Features

- Scrapes top cryptocurrencies from CoinMarketCap
- Handles JavaScript-rendered and virtualized tables
- Extracts:
  - Cryptocurrency Name
  - Current Price
  - 24-hour Change (%)
  - Market Capitalization
  - Timestamp (UTC)
- Exports data to CSV using Pandas
- Robust and flexible scraping logic (not dependent on fragile class names)

---

## 🛠️ Technology Stack

- Python 3.x
- Selenium WebDriver
- Google Chrome & ChromeDriver
- WebDriver Manager
- Pandas
- CoinMarketCap (data source)

---

## ⚙️ How It Works

1. Launches a Chrome browser using Selenium
2. Opens CoinMarketCap
3. Waits for dynamic content to load
4. Scrolls to load lazy-rendered data
5. Extracts required market metrics using meaning-based filtering
6. Saves the data into a CSV file

---

## 📊 Sample Output

| Name | Price | 24h Change | Market Cap | Timestamp |
|-----|-------|------------|------------|-----------|
| Bitcoin | $43,210.12 | +1.24% | $845,123,456,789 | 2025-xx-xx |

---

## ▶️ How to Run

```bash
pip install selenium webdriver-manager pandas
python main.py
