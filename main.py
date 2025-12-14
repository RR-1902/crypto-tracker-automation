import pandas as pd
from datetime import datetime, timezone
from selenium import webdriver
from selenium.webdriver.chrome.service import Service
from selenium.webdriver.common.by import By
from selenium.webdriver.chrome.options import Options
from selenium.webdriver.support.ui import WebDriverWait
from selenium.webdriver.support import expected_conditions as EC
from webdriver_manager.chrome import ChromeDriverManager

URL = "https://coinmarketcap.com/"
CSV_FILE = "crypto_data.csv"

def get_driver(headless=True):
    options = Options()
    if headless:
        options.add_argument("--headless=new")
    options.add_argument("--disable-gpu")
    options.add_argument("--no-sandbox")
    options.add_argument("--window-size=1920,1080")
    return webdriver.Chrome(
        service=Service(ChromeDriverManager().install()),
        options=options
    )

def scrape_top_10():
    driver = get_driver(True)
    driver.get(URL)

    WebDriverWait(driver, 15).until(
        EC.presence_of_element_located((By.XPATH, "//tbody/tr"))
    )

    driver.execute_script("window.scrollTo(0, document.body.scrollHeight)")
    WebDriverWait(driver, 5).until(
        EC.presence_of_element_located((By.XPATH, "//span[contains(text(),'$')]"))
    )

    rows = driver.find_elements(By.XPATH, "//tbody/tr")[:10]
    data = []

    for row in rows:
        texts = [t.strip() for t in row.text.split("\n") if t.strip()]

        name = ""
        price = ""
        change_24h = ""
        market_cap = ""

        for t in texts:
            if not t.startswith("$") and not t.endswith("%") and not t.isdigit() and len(t) > 3:
                name = t
                break

        dollar_values = [t for t in texts if t.startswith("$")]
        percent_values = [t for t in texts if t.endswith("%")]

        if len(dollar_values) > 0:
            price = dollar_values[0]
        if len(dollar_values) > 1:
            market_cap = dollar_values[1]
        if len(percent_values) > 0:
            change_24h = percent_values[0]

        data.append([
            name,
            price,
            change_24h,
            market_cap,
            datetime.now(timezone.utc).strftime("%Y-%m-%d %H:%M:%S")
        ])

    driver.quit()

    return pd.DataFrame(
        data,
        columns=["Name", "Price", "24h Change", "Market Cap", "Timestamp"]
    )

def save_csv(df):
    try:
        old_df = pd.read_csv(CSV_FILE)
        df = pd.concat([old_df, df], ignore_index=True)
    except FileNotFoundError:
        pass
    df.to_csv(CSV_FILE, index=False)

if __name__ == "__main__":
    df = scrape_top_10()
    print(df)
    if not df.empty:
        save_csv(df)
