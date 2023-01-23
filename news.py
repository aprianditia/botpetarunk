import requests
import json
from telegram.ext import Updater, CommandHandler

# Function to get current crypto price from Indodax
def get_price(crypto):
    url = "https://indodax.com/api/{}/ticker".format(crypto)
    response = requests.get(url)
    data = json.loads(response.text)
    return data["ticker"]["last"]

# Function to check for price change and send notification
def check_price(update, context):
    crypto = "BTC"  # Example for Bitcoin
    current_price = get_price(crypto)
    if current_price > previous_price + (previous_price * 0.3):
        message = "ALERT: {} price has increased by 30%! Current price: {}".format(crypto, current_price)
    elif current_price < previous_price - (previous_price * 0.3):
        message = "ALERT: {} price has decreased by 30%! Current price: {}".format(crypto, current_price)
    else:
        message = "No drastic change in {} price".format(crypto)
    context.bot.send_message(chat_id=update.message.chat_id, text=message)

# Telegram bot setup
updater = Updater(token="YOUR_BOT_TOKEN", use_context=True)
dispatcher = updater.dispatcher

# Command handler for /checkprice command
dispatcher.add_handler(CommandHandler("checkprice", check_price))

# Start polling
updater.start_polling()
