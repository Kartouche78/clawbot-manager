import os
import telebot
from anthropic import Anthropic

# On récupère les clés via les variables d'environnement
TELEGRAM_TOKEN = "8599622285:AAFBlOVFlC056GaBmfQDx13cZjcUixJ8wcg"
CLAUDE_KEY = os.environ.get("CLAUDE_KEY")

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = Anthropic(api_key=CLAUDE_KEY)

@bot.message_handler(func=lambda message: True)
def chat_with_claude(message):
    response = client.messages.create(
        model="claude-3-haiku-20240307",
        max_tokens=1000,
        messages=[{"role": "user", "content": message.text}]
    )
    bot.reply_to(message, response.content[0].text)

bot.polling()