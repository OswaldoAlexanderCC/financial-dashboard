import pandas as pd
import logging


def transform_market_data(df):
    logging.info("Starting data transformation...")
    columns = [
        "id",
        "symbol",
        "name",
        "current_price",
        "market_cap",
        "market_cap_rank",
        "total_volume",
        "price_change_percentage_24h"
    ]
    logging.info(f"Selected {len(columns)} columns.")
    df=df[columns]
    logging.info("Transformation completed.")
    return df