from aiogram import Dispatcher
from aiogram.types import ErrorEvent

from .logger import logger

from .user import help, start


def setup_handlers(dp: Dispatcher) -> None:
    @dp.error()
    async def _error(event: ErrorEvent):
        logger.exception(event.exception)

    dp.include_routers(start, help)
  
