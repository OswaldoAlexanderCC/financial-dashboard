import logging
import pandas_gbq

from config import PROJECT_ID, BQ_TABLE


def load_market_data(df):

    logging.info("Loading data into BigQuery...")

    pandas_gbq.to_gbq(
        dataframe=df,
        destination_table=BQ_TABLE,
        project_id=PROJECT_ID,
        if_exists="replace"
    )

    logging.info(f"Loaded {len(df)} records into '{BQ_TABLE}'.")
    logging.info("Load completed.")