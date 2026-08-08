from extract import extract_market_data
from transform import transform_market_data
from load import load_market_data
import logging

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s"
)

def main():

    logging.info("ETL process started.")

    df = extract_market_data()
    df = transform_market_data(df)
    load_market_data(df)

    logging.info("ETL process completed successfully.")

if __name__ == "__main__":
    main()