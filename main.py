from flask import Flask
from telebot import TeleBot
import os

app = Flask(__name__)

TOKEN = os.environ.get("TOKEN")
bot = TeleBot(TOKEN)

@bot.message_handler(func=lambda message: True)
def echo(message):
    bot.reply_to(message, "¡Hola! Estoy vivo. Tu bot funciona.")

if __name__ == "__main__":
    bot.polling()

