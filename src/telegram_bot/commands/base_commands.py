from telegram import Update
from telegram.ext import CallbackContext


# simple example
def command_start(update: Update, context: CallbackContext):
    update.message.reply_text('Hello!')
