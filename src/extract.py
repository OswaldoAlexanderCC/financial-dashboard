import requests
import pandas as pd
import logging
 
from config import (
    BASE_URL,
    DEFAULT_CURRENCY,
    DEFAULT_PER_PAGE,
    DEFAULT_PAGE,
    DEFAULT_ORDER,
    TIMEOUT,
)


def extract_market_data():

    params = {
        "vs_currency": DEFAULT_CURRENCY,
        "per_page": DEFAULT_PER_PAGE,
        "page": DEFAULT_PAGE,
        "order": DEFAULT_ORDER,
    }
    logging.info("Starting market data extraction...")
    try:
        response = requests.get(BASE_URL, params=params, timeout=TIMEOUT)
        response.raise_for_status()

        data = response.json()
        df = pd.DataFrame(data)
        logging.info(f"Retrieved {len(df)} records.")
        return df
        
    except requests.RequestException as e:
        logging.error(f"Error fetching market data: {e}")
        return pd.DataFrame()