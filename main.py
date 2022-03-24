import telebot
import requests
from datetime import datetime
from auth_data import bot_token

def get_data():
   req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
   response = req.json()
   sell_price = response['btc_usd']['sell']
   print(f"{datetime.now().strftime('%m-%d-%Y %H:%M')}\nSell BTC price: {sell_price}")

def telegram_bot(token):
   bot = telebot.TeleBot(token)

   @bot.message_handler(commands=["start"])
   def start_message(message):
      bot.send_message(message.chat.id, "Hi! Write price to see BTC price")

   @bot.message_handler(content_types=["text"])
   def send_price(message):
      if message.text.lower() =="price":
         try:
            req = requests.get("https://yobit.net/api/3/ticker/btc_usd")
            response = req.json()
            sell_price = response['btc_usd']['sell']
            bot.send_message(
               message.chat.id,
               f"{datetime.now().strftime('%m-%d-%Y %H:%M')}\nSell BTC price: {sell_price}"
            )
         except Exception as ex:
            print(ex)
            bot.send_message (
               message.chat.id,
               "We don't know what is this"
            )
      else:
         bot.send_message(
            message.chat.id,
            "What is this?!"
         )

   bot.polling()

if __name__ == '__main__':
   # get_data()
   telegram_bot(bot_token)