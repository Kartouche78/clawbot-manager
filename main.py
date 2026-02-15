import telebot
from anthropic import Anthropic

# Remplace par tes vraies clés
TELEGRAM_TOKEN = "8599622285:AAFBlOVFlC056GaBmfQDx13cZjcUixJ8wcg"
CLAUDE_KEY = "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"

bot = telebot.TeleBot(TELEGRAM_TOKEN)
client = Anthropic(api_key=CLAUDE_KEY)

@bot.message_handler(func=lambda message: True)
def chat_with_claude(message):
    # On envoie la question à l'IA Claude
    response = client.messages.create(
        model="claude-3-haiku-20240307", # La version rapide et pas chère
        max_tokens=1000,
        messages=[{"role": "user", "content": message.text}]
    )
    # On renvoie la réponse de l'IA sur Telegram
    bot.reply_to(message, response.content[0].text)

print("K-Bot IA est prêt sur le serveur !")
bot.polling()