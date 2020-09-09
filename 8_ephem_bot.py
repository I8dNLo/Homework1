"""
Домашнее задание №1

Использование библиотек: ephem

* Установите модуль ephem
* Добавьте в бота команду /planet, которая будет принимать на вход 
  название планеты на английском, например /planet Mars
* В функции-обработчике команды из update.message.text получите 
  название планеты (подсказка: используйте .split())
* При помощи условного оператора if и ephem.constellation научите 
  бота отвечать, в каком созвездии сегодня находится планета.

"""

import logging
from telegram.ext import Updater, CommandHandler, MessageHandler, Filters
import settings
import ephem
from datetime import datetime


logging.basicConfig(filename='bot.log', level=logging.INFO)

PROXY = {
    'proxy_url': settings.PROXY_URL,
    'urllib3_proxy_kwargs': {'username': settings.PROXY_USERNAME, 'password' : settings.PROXY_PASSWORD},
}

def greet_user(update, context):
    print('Вызван /start')
    update.message.reply_text('Здравствуй, пользователь')

def get_date(update, context):
    print('Вызван date')
    dt_now = datetime.now()
    update.message.reply_text(dt_now.strftime('%d.%m.%Y'))

def get_planet(update, context):
    print("вызвана функция определения местоположения планеты")
    dt_now = datetime.now()
    planet = ephem.Mars(dt_now.strftime('%d/%m/%Y'))
    constellation = ephem.constellation(planet)
    update.message.reply_text(constellation)


def talk_to_me(update, context):
    text = update.message.text
    print(text)
    update.message.reply_text(text)

def main():
    mybot = Updater(settings.API_KEY, use_context=True, request_kwargs=PROXY)

    dp = mybot.dispatcher
    dp.add_handler(CommandHandler('start', greet_user))
    dp.add_handler(CommandHandler('planet', get_planet))
    dp.add_handler(CommandHandler('date', get_date))

   # dp.add_handler(MessageHandler('date', get_date))
    dp.add_handler(MessageHandler(Filters.text, talk_to_me))

    logging.info('Бот стартовал')

    mybot.start_polling()
    mybot.idle()

if __name__ == '__main__':
    main()
