import telebot

bot = telebot.TeleBot("6049737817:AAH0NdLsq6th8feFw7HRvJFvCLOHFnAi0fY")

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, "How are you doing?")

@bot.message_handler(func=lambda m: True)
def echo_all(message):
	bot.reply_to(message, message.text)

bot.infinity_polling()

