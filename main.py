from flask import Flask, request
import telebot
import os
import openai

TOKEN = os.environ.get("TOKEN")
OPENAI_KEY = os.environ.get("OPENAI_KEY")

bot = telebot.TeleBot(TOKEN)
openai.api_key = OPENAI_KEY

PERSONALIDAD = """
Eres un bot juvenil cristiano. Hablas de forma amigable, cercana y motivadora.
No usas groserías. Das consejos prácticos basados en la Biblia Reina Valera 1960.
Cuando cites un versículo, indica el libro, capítulo y versículo.
Mantén respuestas claras y edificantes.
"""

@app.route(f"/{TOKEN}", methods=["POST"])
def webhook():
    json_str = request.get_data().decode("UTF-8")
    update = telebot.types.Update.de_json(json_str)
    bot.process_new_updates([update])
    return "OK", 200

@bot.message_handler(func=lambda message: True)
def responder(message):
    try:
        respuesta = openai.ChatCompletion.create(
            model="gpt-4o-mini",
            messages=[
                {"role": "system", "content": PERSONALIDAD},
                {"role": "user", "content": message.text}
            ],
            max_tokens=300,
            temperature=0.7,
        )

        texto = respuesta.choices[0].message.content
        bot.reply_to(message, texto)

    except Exception as e:
        bot.reply_to(message, "Hubo un pequeño error, pero todo estará bien 🙌")
