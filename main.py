import telebot

# Ton Token officiel pour @Kartouche-bot
TOKEN = '8599622285:AAFBlOVFlC056GaBmfQDx13cZjcUixJ8wcg'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    # Un petit message personnalisé pour marquer le coup
    bot.reply_to(message, "Salut Kartouche ! K-Bot est officiellement en vie sur ton serveur karakartal ! 🚀")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    # Le bot te renvoie ce que tu écris
    bot.reply_to(message, f"Tu as dit : {message.text}")

print("K-Bot est prêt à discuter sur Telegram...")
bot.infinity_polling()