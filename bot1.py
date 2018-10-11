# coding utf-8
from telegram.ext import CommandHandler, Updater
import telegram
from functools import wraps
from sys import argv
import logging



def test(bot, update):
    bot.send_chat_action(update.message.chat_id, action=telegram.ChatAction.TYPING)
    location_keyboard = telegram.KeyboardButton(text="enviame la posicion", request_location=True)
    custom_keyboard = [[ location_keyboard]]
    reply_markup = telegram.ReplyKeyboardMarkup(custom_keyboard)
    bot.send_message(update.message.chat_id, text="me compartes la hubicación?", reply_markup=reply_markup)
    logging.info(f'update.message.chat_id -> {update.message.chat_id} update.message.from_user ->  {update.message.from_user}')

def start(bot, update):
    bot.send_chat_action(update.message.chat_id, action=telegram.ChatAction.TYPING)
    bot.send_message(update.message.chat_id, text="soporto /test")

def token():
    #lee el token de fichero
    API1 = ''
    with open('./token.txt', 'rU') as f:
        API1 = f.readline()
        API1 = API1.rstrip('\n')
        f.close()
    logging.info(f'API1 -> {API1}')
    return API1


#https://python-telegram-bot.readthedocs.io/en/stable/telegram.ext.conversationhandler.html  por aqui voy
def main(args):
    logging.basicConfig(format='%(asctime)s - %(name)s - %(levelname)s - %(message)s', level=logging.INFO)
    '''arranque bot'''
    API1 = token()
    with open('./token.txt', 'rU') as f:
        API1 = f.readline()
        API1 = API1.rstrip('\n')
        f.close()
    logging.info(f'API1 -> {API1}')
    updater = Updater(API1)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(CommandHandler('test',test,pass_args = False))
    updater.start_polling(clean=True)
    updater.idle()


if __name__ == '__main__':
    main(argv)