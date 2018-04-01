#!/usr/bin/python

import requests
import telegram
from telegram.ext import Updater
from telegram.ext import CommandHandler

api = 'https://api.blinktrade.com/api/v1/BRL/ticker?crypto_currency=BTC'

json_data = requests.get(api).json()

ultimas_compra = json_data['last']
alta = json_data['high']
baixa = json_data['low']
volume = json_data['vol']

bot = telegram.Bot(token='389931006:AAHPLmleKkPQ_VOf_eLVCu_GMXbhNxSyuD4')
updater = Updater(token='389931006:AAHPLmleKkPQ_VOf_eLVCu_GMXbhNxSyuD4')
dispatcher = updater.dispatcher

def start(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Digite /preco para ver o preço do Bitcoin na Foxbit')

def preco(bot, update):
    bot.send_message(chat_id=update.message.chat_id, text='Preço: R$ {}\n'.format(ultimas_compra) + 
        'Alta: R$ {}\n'.format(alta) +
        'Baixa: R$ {}\n'.format(baixa) +
        'Volume: ฿ {}\n'.format(volume))

start_handler = CommandHandler('start', start)
dispatcher.add_handler(start_handler)

preco_handler = CommandHandler('preco', preco)
dispatcher.add_handler(preco_handler)

updater.start_polling()