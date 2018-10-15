import sys
from modules.bicizgz import conexion
import modules.bicizgz.listaparada
from modules.bicizgz.posicionUsuario import obtenerlistaPosicionUsuario
import pandas as pd
from telegram import InlineQueryResultArticle, InlineQueryResultLocation, InputTextMessageContent
import logging

class bici:

    def __init__(self):
        #print('init')
        pass
    
    def obtenlistaParadas(self):
        return conexion.obtenlistaParadas()

    def obtenlistaDistanciaUsuario(self, idUsuario='0', LatitudeUsuario='0', LongitudeUsuario='0'):
        listaparadas = pd.read_csv('modules/bicizgz/paradas.csv', sep=',',header=0)
        listakm = obtenerlistaPosicionUsuario(listaparadas, idUsuario, LatitudeUsuario, LongitudeUsuario)
        listaresult = []

        for index, fila in listakm.iterrows():
           #------------------------------------------------------------------------------------------------------# 
           #COLUMNAS DEL DATAFRAME DEL CALCULO DE DISTANCIAS                                                      #
           #[Distancia, UsuarioID, ParadaID, LatitudeUsuario, LongitudeUsuario, LatitudeParada, LongitudeParada]  #
           #------------------------------------------------------------------------------------------------------# 
           #COLUMNAS DEL DATAFRAME OBTENIDOS DEL SERVIDOR                                                         #
           #[StationID, DisctrictCode, AddressGmapsLatitude, AddressGmapsLongitude, StationAvailableBikes   \     #
           # StationFreeSlot, AddressZipCode, AddressStreet1, AddressNumber, NearbyStationList,             \     #
           # StationStatusCode, StationName]                                                                      #
           #------------------------------------------------------------------------------------------------------# 
           #DATOS A RETORNAR EN UNA LISTA                                                                         #
           #[2,latitude=43.4618219, longitude=-3.8112334, title='bicis=2 huecos=1 {calle}']                       #
           #------------------------------------------------------------------------------------------------------#
            filtro = listaparadas[listaparadas['StationID'] == fila['ParadaID']]
            listaresult.append(InlineQueryResultLocation((filtro['StationID']).values,    \
                            float(filtro['AddressGmapsLatitude']),    \
                            float(filtro['AddressGmapsLongitude']),    \
                            title=f"{filtro['StationAvailableBikes'].values} bicis {filtro['StationFreeSlot'].values} huecos {filtro['AddressStreet1'].values}".replace('[','').replace(']','')))
            if len(listaresult) == 6:
                logging.info('6 estaciones enviadas')
                break
        return listaresult

    def obtenlistaDistanciaUsuario2(self, idUsuario='0', LatitudeUsuario='0', LongitudeUsuario='0'):
        listaparadas = pd.read_csv('modules/bicizgz/paradas.csv', sep=',',header=0)
        listakm = obtenerlistaPosicionUsuario(listaparadas, idUsuario, LatitudeUsuario, LongitudeUsuario)
        listaresult = []
        ApiKey='LEE EL API KEY DE TRELLO'
        for index, fila in listakm.iterrows():
           #------------------------------------------------------------------------------------------------------# 
           #COLUMNAS DEL DATAFRAME DEL CALCULO DE DISTANCIAS                                                      #
           #[Distancia, UsuarioID, ParadaID, LatitudeUsuario, LongitudeUsuario, LatitudeParada, LongitudeParada]  #
           #------------------------------------------------------------------------------------------------------# 
           #COLUMNAS DEL DATAFRAME OBTENIDOS DEL SERVIDOR                                                         #
           #[StationID, DisctrictCode, AddressGmapsLatitude, AddressGmapsLongitude, StationAvailableBikes   \     #
           # StationFreeSlot, AddressZipCode, AddressStreet1, AddressNumber, NearbyStationList,             \     #
           # StationStatusCode, StationName]                                                                      #
           #------------------------------------------------------------------------------------------------------# 
           #DATOS A RETORNAR EN UNA LISTA                                                                         #
           #[2,latitude=43.4618219, longitude=-3.8112334, title='bicis=2 huecos=1 {calle}']                       #
           #------------------------------------------------------------------------------------------------------#
            filtro = listaparadas[listaparadas['StationID'] == fila['ParadaID']]
            thumb=f"https://maps.googleapis.com/maps/api/staticmap?center={filtro['AddressGmapsLatitude'].values},{filtro['AddressGmapsLongitude'].values}&zoom=20&size=600x400&key={ApiKey}".replace('[','').replace(']','')
            logging.info(f'url -> {thumb}')
            add = InlineQueryResultArticle((filtro['StationID']).values,    \
                                            title=f"{filtro['StationAvailableBikes'].values}b/{filtro['StationFreeSlot'].values}h {filtro['AddressStreet1'].values}".replace('[','').replace(']',''),    \
                                            input_message_content=InputTextMessageContent(f"{filtro['StationAvailableBikes'].values} bicis {filtro['StationFreeSlot'].values} huecos \n\r{filtro['AddressStreet1'].values}\r\nhttps://www.google.com/maps/@{float(filtro['AddressGmapsLatitude'])},{float(filtro['AddressGmapsLongitude'])},20z ".replace('[','').replace(']',''),parse_mode="HTML"),    \
                                            thumb_url=thumb,thumb_width=600,thumb_height=400)
            listaresult.append(add)
            if len(listaresult) == 6:
                logging.info('6 estaciones enviadas')
                break
        return listaresult

def main():
    c = bici()
    print(c.obtenlistaParadas())

    lp = pd.read_csv('paradas.csv', sep=',',header=0)
    print(f'{c.obtenlistaDistanciaUsuario( "1234567", "41.6218009", "-0.9523861")}')

    del c

if __name__ == '__main__':
    main()