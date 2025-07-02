# This is an init file for the package
import logging
import time
import sys
import os

logging_str='%(asctime)s - %(name)s - %(levelname)s - %(message)s'
logging.basicConfig(stream=sys.stdout, level=logging.INFO, format=logging_str)
logger = logging.getLogger(__name__)

log_dir = "logging"

log_file= f"{log_dir}/running_log.log"

os.makedirs(log_dir, exist_ok=True)

logging.basicConfig(
    filename=log_file,
    level=logging.INFO,
    format=logging_str,
    filemode='a',
    handlers=[
        logging.FileHandler(log_file),
        logging.StreamHandler(sys.stdout)
    ]
)

logger=logging.getLogger(__name__)