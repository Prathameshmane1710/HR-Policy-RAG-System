import logging
import os
from datetime import datetime

LOGS_DIR = "logs"
date_dir_name = datetime.now().strftime("%d %B %Y")
test_log_name = os.path.join(LOGS_DIR,date_dir_name)
os.makedirs(test_log_name,exist_ok=True)


_run_started_at = datetime.now().strftime("%Y%m%d_%H%M%S")
RUN_LOG_FILE = os.path.join(test_log_name,f"run_{_run_started_at}.log")

logging.basicConfig(
    level=logging.INFO,
    format="%(asctime)s | %(levelname)s | %(name)s | %(message)s",
    handlers=[
        logging.FileHandler(RUN_LOG_FILE,encoding="utf8"),
        logging.StreamHandler(),
    ],
)

def get_logger(name: str) -> logging.Logger:
    return logging.getLogger(name)