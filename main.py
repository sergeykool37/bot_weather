#Botweather234

import os
import telebot
from weather_api import print_temp
token_bot=os.getenv('TokenBot')
bot=telebot.TeleBot(token_bot)

@bot.message_handler(commands=['start', 'help'])
def send_welcome(message):
    bot.reply_to(message, f'Я бот. Приятно познакомиться, {message.from_user.first_name}')

@bot.message_handler(content_types=['text'])
def get_text_messages(message):
    response=message.text.lower()
    if  response== 'привет':
        bot.send_message(message.from_user.id, 'Привет!')
    else:
        weather=print_temp(response)
        bot.send_message(message.from_user.id, weather)



# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    bot.polling(none_stop=True)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
