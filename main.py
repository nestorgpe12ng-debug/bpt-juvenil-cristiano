import os
import telebot
from openai import OpenAI

TOKEN = os.environ.get("TOKEN")
OPENAI_KEY = os.environ.get("OPENAI_KEY")

bot = telebot.TeleBot(TOKEN)
client = OpenAI(api_key=OPENAI_KEY)

PERSONALIDAD = """
Eres un bot juvenil cristiano.
Hablas de manera amigable.
No usas groserías.
Das consejos bíblicos prácticos.
Eres positivo, motivador y breve.
Usar base Biblica 1960
"""

@bot.message_handler(func=lambda message: True)
def responder(message):
    if "@TuBot" in message.text:
        respuesta = client.chat.completions.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": PERSONALIDAD},
                {"role": "user", "content": message.text}
            ]
        )
        bot.reply_to(message, respuesta.choices[0].message.content)

bot.polling()
