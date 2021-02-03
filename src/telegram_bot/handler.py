from django.conf import settings

from telegram import Bot
from telegram.ext import Dispatcher, CommandHandler
from .commands import base_commands


def setup():
    telegram_bot = Bot(settings.TELEGRAM_BOT_TOKEN)
    if settings.TELEGRAM_BOT_WEBHOOK_ENABLED:
        telegram_bot.set_webhook(settings.TELEGRAM_BOT_WEBHOOK_URL)

    telegram_dispatcher = Dispatcher(telegram_bot, None, workers=6)

    # register your handlers here
    command_start = CommandHandler('start', base_commands.command_start)
    telegram_dispatcher.add_handler(command_start)

    return telegram_bot, telegram_dispatcher


bot, dispatcher = setup()
