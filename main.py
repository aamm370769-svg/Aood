from telegram import Update
from telegram.ext import Updater, MessageHandler, Filters, CallbackContext
from transformers import pipeline

# نموذج AI مجاني
generator = pipeline('text-generation', model='gpt2')

def handle_message(update: Update, context: CallbackContext):
    user_msg = update.message.text
    response = generator(user_msg, max_length=100)[0]['generated_text']
    update.message.reply_text(response)

# التوكن الخاص بك
TELEGRAM_TOKEN = "8341866245:AAHcqf99oEyVct8sUKONnOj1cIsc1ya7a-I"

updater = Updater(TELEGRAM_TOKEN, use_context=True)
updater.dispatcher.add_handler(MessageHandler(Filters.text & ~Filters.command, handle_message))
updater.start_polling()
updater.idle()
