# coding utf-8
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters
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
    telegram.ForceReply(force_reply=True, selective=False)
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

def echo_text(bot, update):
    logging.info(f'update.message.text -> {update.message.text} \nupdate.message.chat_id -> {update.message.chat_id} \nupdate.message.from_user ->  {update.message.from_user}')
    bot.send_message(update.message.chat_id, f'update.message.text -> {update.message.text} \nupdate.message.chat_id -> {update.message.chat_id} \nupdate.message.from_user ->  {update.message.from_user}')

def echo_location(bot, update):
    logging.info(f'update.message.location -> {update.message.location} \nupdate.message.chat_id -> {update.message.chat_id} \nupdate.message.from_user ->  {update.message.from_user}')
    MapaLoingitud = update.message.location.longitude
    MapaLatitud = update.message.location.latitude
    bot.send_message(update.message.chat_id, f'MapaLoingitud -> {MapaLoingitud} \nMapaLatitud -> {MapaLatitud}')
    bot.send_message(update.message.chat_id, f'update.message.location -> {update.message.location} \nupdate.message.chat_id -> {update.message.chat_id} \nupdate.message.from_user ->  {update.message.from_user}')

def main(args):
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    API1 = token()
    updater = Updater(API1)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(MessageHandler(Filters.text,echo_text))
    dispatcher.add_handler(MessageHandler(Filters.location,echo_location))
    dispatcher.add_handler(CommandHandler('test',test,pass_args = False))
    updater.start_polling(clean=True)
    updater.idle()


if __name__ == '__main__':
    main(argv)