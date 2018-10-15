# coding utf-8
from telegram import InlineQueryResultArticle, InputTextMessageContent, InlineQueryResultLocation, InlineQueryResult
from telegram.ext import CommandHandler, Updater, MessageHandler, Filters, InlineQueryHandler
from telegram.ext.dispatcher import run_async
from functools import wraps
from sys import argv
import logging
import sys
import modules.bicizgz
from modules.bicizgz.bici import bici

def start(bot, update):
    bot.send_message(update.message.chat_id, text="espero que te guste")

def token():
    #lee el token de fichero
    API1 = ''
    with open('./token.txt', 'rU') as f:
        API1 = f.readline()
        API1 = API1.rstrip('\n')
        f.close()
    logging.info(f'API1 -> {API1}')
    return API1

@run_async
def trabaja(bot, update):
    logging.info("trabaja(bot, update)")
    logging.info(f'update.inline_query.query -> {update.inline_query.query}')
    results = list()
    logging.info(f'update.inline_query.location.longitude -> {update.inline_query.location.longitude}')
    logging.info(f'update.inline_query.location.latitude -> {update.inline_query.location.latitude}')
    if not update.inline_query.query:
        results.append(InlineQueryResultArticle(id="3",title="comando vacio escribe bici o bus o tranvía",input_message_content=InputTextMessageContent('escribe bici o bus o tranvia',parse_mode="HTML"), ))
        bot.answerInlineQuery(update.inline_query.id, results, cache_time=0)
        return
    elif (update.inline_query.query == 'bici'):
        '''
        loc0 = InlineQueryResultLocation(1,latitude=41.120689, longitude=1.1810739, title='bicis=1 huecos=3 {calle}')
        loc2 = InlineQueryResultLocation(2,latitude=43.4618219, longitude=-3.8112334, title='bicis=2 huecos=1 {calle}')
        #result = Bici.paradascercanas(update.inline_query.location.longitude, update.inline_query.location.latitude, nparadas)        
        results.append(loc0)
        results.append(loc2)
        #loc01 = InlineQueryResultArticle(id="3",title="Parada 1",input_message_content=InputTextMessageContent('bicis={nbicis} huecos={nhuecos} calle {calle}',parse_mode="HTML"), url="https://www.google.com/maps/place/La+Canonja,+Tarragona/@41.1201774,1.181502")
        #loc02 = InlineQueryResultArticle(id="4", title="Parada 2", input_message_content=InputTextMessageContent("bicis={nbicis} huecos={nhuecos} calle {calle}",parse_mode="HTML"), url='https://www.google.com/maps/place/Santander,+Cantabria/@43.4623256,-3.8100945')
        #results.append(loc01)
        #results.append(loc02)
        bot.answerInlineQuery(update.inline_query.id, results, cache_time=0) 
        logging.info(f'update.inline_query.location.longitude -> {update.inline_query.location.longitude}')
        logging.info(f'update.inline_query.location.latitude -> {update.inline_query.location.latitude}')
        '''
        MiBici = bici()
        bot.answerInlineQuery(update.inline_query.id, MiBici.obtenlistaDistanciaUsuario(float(0),str(update.inline_query.location.latitude),str(update.inline_query.location.longitude)), cache_time=0) 
        return
    elif (update.inline_query.query == 'bicis'):
        '''
        loc0 = InlineQueryResultLocation(1,latitude=41.120689, longitude=1.1810739, title='bicis=1 huecos=3 {calle}')
        loc2 = InlineQueryResultLocation(2,latitude=43.4618219, longitude=-3.8112334, title='bicis=2 huecos=1 {calle}')
        #result = Bici.paradascercanas(update.inline_query.location.longitude, update.inline_query.location.latitude, nparadas)        
        results.append(loc0)
        results.append(loc2)
        #loc01 = InlineQueryResultArticle(id="3",title="Parada 1",input_message_content=InputTextMessageContent('bicis={nbicis} huecos={nhuecos} calle {calle}',parse_mode="HTML"), url="https://www.google.com/maps/place/La+Canonja,+Tarragona/@41.1201774,1.181502")
        #loc02 = InlineQueryResultArticle(id="4", title="Parada 2", input_message_content=InputTextMessageContent("bicis={nbicis} huecos={nhuecos} calle {calle}",parse_mode="HTML"), url='https://www.google.com/maps/place/Santander,+Cantabria/@43.4623256,-3.8100945')
        #results.append(loc01)
        #results.append(loc02)
        bot.answerInlineQuery(update.inline_query.id, results, cache_time=0) 
        logging.info(f'update.inline_query.location.longitude -> {update.inline_query.location.longitude}')
        logging.info(f'update.inline_query.location.latitude -> {update.inline_query.location.latitude}')
        '''
        MiBici = bici()
        bot.answerInlineQuery(update.inline_query.id, MiBici.obtenlistaDistanciaUsuario2(float(0),str(update.inline_query.location.latitude),str(update.inline_query.location.longitude)), cache_time=0) 
        return
    elif (update.inline_query.query == 'bus'):
        loc0 = InlineQueryResultLocation(1,latitude=41.120689, longitude=1.1810739, title='bicis=1 huecos=3 {calle}')
        loc2 = InlineQueryResultLocation(2,latitude=43.4618219, longitude=-3.8112334, title='bicis=2 huecos=1 {calle}')
        #result = Bici.paradascercanas(update.inline_query.location.longitude, update.inline_query.location.latitude, nparadas)        
        results.append(loc0)
        results.append(loc2)
        #loc01 = InlineQueryResultArticle(id="3",title="Parada 1",input_message_content=InputTextMessageContent('bicis={nbicis} huecos={nhuecos} calle {calle}',parse_mode="HTML"), url="https://www.google.com/maps/place/La+Canonja,+Tarragona/@41.1201774,1.181502")
        #loc02 = InlineQueryResultArticle(id="4", title="Parada 2", input_message_content=InputTextMessageContent("bicis={nbicis} huecos={nhuecos} calle {calle}",parse_mode="HTML"), url='https://www.google.com/maps/place/Santander,+Cantabria/@43.4623256,-3.8100945')
        #results.append(loc01)
        #results.append(loc02)
        bot.answerInlineQuery(update.inline_query.id, results, cache_time=0) 
        return
    elif (update.inline_query.query == 'tranvia'):
        loc0 = InlineQueryResultLocation(1,latitude=41.120689, longitude=1.1810739, title='bicis=1 huecos=3 {calle}')
        loc2 = InlineQueryResultLocation(2,latitude=43.4618219, longitude=-3.8112334, title='bicis=2 huecos=1 {calle}')
        #result = Bici.paradascercanas(update.inline_query.location.longitude, update.inline_query.location.latitude, nparadas)        
        results.append(loc0)
        results.append(loc2)
        #loc01 = InlineQueryResultArticle(id="3",title="Parada 1",input_message_content=InputTextMessageContent('bicis={nbicis} huecos={nhuecos} calle {calle}',parse_mode="HTML"), url="https://www.google.com/maps/place/La+Canonja,+Tarragona/@41.1201774,1.181502")
        #loc02 = InlineQueryResultArticle(id="4", title="Parada 2", input_message_content=InputTextMessageContent("bicis={nbicis} huecos={nhuecos} calle {calle}",parse_mode="HTML"), url='https://www.google.com/maps/place/Santander,+Cantabria/@43.4623256,-3.8100945')
        #results.append(loc01)
        #results.append(loc02)
        bot.answerInlineQuery(update.inline_query.id, results, cache_time=0) 
        return
    else:
        results.append(InlineQueryResultArticle(id="3",title="comando no soportado",input_message_content=InputTextMessageContent('escribe bici o bus o tranvia',parse_mode="HTML"), ))
        bot.answerInlineQuery(update.inline_query.id, results, cache_time=0)
        return

def main(args):
    logging.basicConfig(format='%(asctime)s - %(levelname)s - %(message)s', level=logging.INFO)
    API1 = token()
    updater = Updater(API1, workers=10)
    dispatcher = updater.dispatcher
    dispatcher.add_handler(InlineQueryHandler(trabaja))
    updater.start_polling(clean=True)
    updater.idle()


if __name__ == '__main__':
    main(argv)