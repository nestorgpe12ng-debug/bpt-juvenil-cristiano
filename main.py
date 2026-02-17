from flask import Flask
from telebot import TeleBot
import os
import openai

app = Flask(__name__)

TOKEN = os.environ.get("TOKEN")
OPENAI_KEY = os.environ.get("OPENAI_KEY")

bot = TeleBot(TOKEN)
openai.api_key = OPENAI_KEY

PERSONALIDAD = """
Eres un bot juvenil cristiano. Hablas de manera amigable, positiva y breve. No usas groserías. Das consejos bíblicos prácticos basados en la Reina Valera 1960. Eres motivador, claro y cercano. Usa versículos y palabras inspiradoras.
"""

@bot.message_handler(func=lambda message: True)
def responder(message):
    if '@' in message.text or message.chat.type == 'private':
        respuesta = openai.ChatCompletion.create(
            model="gpt-4o",
            messages=[
                {"role": "system", "content": PERSONALIDAD},
                {"role": "user", "content": message.text}
            ],
            parameters={
                "max_tokens": 300,
                "temperature": 0.7,
            }
        )
        respuesta_texto = respuesta.choices[0].message.content
        bot.reply_to(message, respuesta_texto)

if __name__ == '__main__':
    bot.polling()
