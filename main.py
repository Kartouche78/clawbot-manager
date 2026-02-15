import telebot

# Remplace 'TON_TOKEN_ICI' par le code que BotFather t'a donné
TOKEN = 'TON_TOKEN_ICI'
bot = telebot.TeleBot(TOKEN)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "Salut Kartouche ! K-Bot est en ligne sur ton serveur karakartal !")

@bot.message_handler(func=lambda message: True)
def echo_all(message):
    bot.reply_to(message, f"Tu as dit : {message.text}")

print("K-Bot est prêt à discuter...")
bot.infinity_polling()