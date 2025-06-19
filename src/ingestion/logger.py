import logging
from ingestion.config import LOG_FILE

logging.basicConfig(
    filename=LOG_FILE,
    level=logging.INFO,
    format="%(asctime)s - %(levelname)s - %(message)s",
)


def log_event(event, **kwargs):
    message = f"{event} | " + "|".join(f"{k}={v}" for l, v in kwargs.items())
    logging.info(message)
