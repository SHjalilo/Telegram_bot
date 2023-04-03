#import os
import telebot
from telebot import types
#BOT_TOKEN = os.environ.get('BOT_TOKEN')
bot = telebot.TeleBot('BOT_TOKEN')
#----
@bot.message_handler(commands=['start', 'hello'])
def send_welcome(message):
    bot.reply_to(message, "How are you doing ?")
#----------------------------------------------------------
#@bot.message_handler(func=lambda msg: True)
#def echo_all(message):
#    bot.reply_to(message, message.text)
def option_func(message):
    if message.text in "options":
        return True
    
@bot.message_handler(func=option_func)
def options(message):
    markup=types.ReplyKeyboardMarkup(row_width=2)
    itembtn1=types.KeyboardButton('option 01')
    itembtn2=types.KeyboardButton('option 02')
    itembtn3=types.KeyboardButton('option 03')
    markup.add(itembtn1 , itembtn2 , itembtn3)
    bot.send_message(message.chat.id, "Choose an option :",reply_markup=markup)


def main():
    bot.infinity_polling()

if __name__=="__main__":
    main()
