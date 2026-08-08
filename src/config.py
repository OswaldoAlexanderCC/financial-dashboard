BASE_URL = "https://api.coingecko.com/api/v3/coins/markets"


TABLE_NAME = "crypto_market"

DEFAULT_CURRENCY = "usd"

DEFAULT_PER_PAGE = 100

DEFAULT_PAGE = 1

DEFAULT_ORDER = "market_cap_desc"

TIMEOUT = 10  # seconds

# BigQuery
PROJECT_ID = "linen-badge-504816-r6"

DATASET_ID = "crypto_data"

BQ_TABLE = f"{DATASET_ID}.{TABLE_NAME}"