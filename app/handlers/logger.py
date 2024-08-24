from loguru import logger
from pathlib import Path

DIR = Path(__file__).absolute().parent.parent

logger.add(
    f"{DIR}/logs/app.log",
    format="[{time}] [{level}] [{file.name}:{line}]  {message}",
    level="DEBUG",
    compression="zip",
)
