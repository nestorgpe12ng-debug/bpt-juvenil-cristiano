import os
import telebot
from openai import OpenAI

TOKEN = os.environ.get("8295031670:AAHJuV-Op_EXkDHCwhE_FMtZWLNcLlnMrEs")
OPENAI_KEY = os.environ.get("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")

bot = telebot.TeleBot(TOKEN)
client = OpenAI(api_key=OPENAI_KEY)

PERSONALIDAD = """
Eres un bot juvenil cristiano.
Hablas de manera amigable.
No usas groserías.
Das consejos bíblicos prácticos.
Eres positivo, motivador y breve.
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
