import os
import logging
from logging.handlers import RotatingFileHandler
from datetime import datetime
from pathlib import Path

# ==================================================
# Base Paths
# ==================================================

BASE_DIR = Path(__file__).resolve().parents[2]

LOG_DIR = BASE_DIR / "logs"

LOG_DIR.mkdir(exist_ok=True)

# ==================================================
# Log File
# ==================================================

LOG_FILE = LOG_DIR / f"{datetime.now().strftime('%Y-%m-%d')}.log"

# ==================================================
# Logger
# ==================================================

logger = logging.getLogger("autofix_ai")

logger.setLevel(logging.INFO)

# Prevent duplicate handlers during reloads
if logger.hasHandlers():
    logger.handlers.clear()

# ==================================================
# Formatter
# ==================================================

LOG_FORMAT = (
    "[%(asctime)s] "
    "[%(levelname)s] "
    "[%(name)s] "
    "%(filename)s:%(lineno)d "
    "- %(message)s"
)

formatter = logging.Formatter(LOG_FORMAT)

# ==================================================
# Console Handler
# ==================================================

console_handler = logging.StreamHandler()

console_handler.setLevel(logging.INFO)

console_handler.setFormatter(formatter)

# ==================================================
# File Handler
# ==================================================

file_handler = RotatingFileHandler(
    filename=LOG_FILE,
    maxBytes=5 * 1024 * 1024,  # 5 MB
    backupCount=5,
    encoding="utf-8"
)

file_handler.setLevel(logging.INFO)

file_handler.setFormatter(formatter)

# ==================================================
# Register Handlers
# ==================================================

logger.addHandler(console_handler)

logger.addHandler(file_handler)

logger.propagate = False

# ==================================================
# Startup Log
# ==================================================

logger.info("Logger initialized successfully.")