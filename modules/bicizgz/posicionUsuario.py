import math as m
import pandas as df
import googlemaps as ggmp
from datetime import datetime
import logging

def obtenerlistaPosicionUsuario(listaparadas, idUsuario, LatitudeUsuario, LongitudeUsuario):
    
        data = df.DataFrame(columns=('Distancia', 'UsuarioID', 'ParadaID', 'LatitudeUsuario', \
                                     'LongitudeUsuario', 'LatitudeParada', 'LongitudeParada'))

        for index, fila in listaparadas.iterrows():
            
            if fila['StationStatusCode']=='OPN':
                    data.loc[len(data)]=[  
                                    calcula_distancia(LatitudeUsuario, LongitudeUsuario, \
                                                    fila['AddressGmapsLatitude'], fila['AddressGmapsLongitude']),
                                    idUsuario,
                                    fila['StationID'],
                                    fila['AddressGmapsLatitude'], 
                                    fila['AddressGmapsLongitude'],
                                    LatitudeUsuario, 
                                    LongitudeUsuario
                                    
                    ]  
            
        return data.sort_values(by=['Distancia'], ascending=[True])


def acomodador(strLatitude='0', strLongitude='0'):
    
    try:
            Latitude=float(strLatitude.replace(',','.'))
            Longitude=float(strLongitude.replace(',','.'))
    except:
            Latitude=float(strLatitude)
            Longitude=float(strLongitude)
    
    return Latitude, Longitude


def token():
    #lee el token de fichero
    tGM = ''
    print("TKn1", tGM)
    with open('./token.txt', 'rU') as f:
        tGM = f.readline()
        tGM = tGM.rstrip('\n')
        f.close()
    logging.info(f'tGM -> {tGM}')
    print("TKn", tGM)
    return tGM


def calcula_tiempodistancia(strLatitudeOrigen='0', strLongitudeOrigen='0',    \
                            strLatitudeDestino='0', strLongitudeDestino='0'):
    now = datetime.now()
    token()
    """
    gmaps = ggmp.Client(key=token())
    directions_result = gmaps.directions(str(acomodador(strLatitudeOrigen, strLongitudeOrigen)),
                                         str(acomodador(strLatitudeDestino, strLongitudeDestino)),
                                          mode="walking",
                                          departure_time=now)
"""
    print ("RESULTADO  ", directions_result)                                      
    return directions_result

def calcula_distancia(strLatitudeOrigen='0', strLongitudeOrigen='0',    \
                      strLatitudeDestino='0', strLongitudeDestino='0'):

        RADIO_TIERRA = 6371

        LatitudeOrigen, LongitudeOrigen = acomodador(strLatitudeOrigen, strLongitudeOrigen)
        LatitudeDestino, LongitudeDestino = acomodador(strLatitudeDestino, strLongitudeDestino) 
   
        Distancia_Km = RADIO_TIERRA * m.acos(
                                             m.cos(m.radians(90-LatitudeOrigen)) * m.cos(m.radians(90-LatitudeDestino)) + 
                                             m.sin(m.radians(90-LatitudeOrigen)) * m.sin(m.radians(90-LatitudeDestino)) *
                                             m.cos(m.radians(LongitudeOrigen-LongitudeDestino))
                                            )

        return round(Distancia_Km, 7)


def main():
    """
    km=calcula_distancia("41,644029", "-0,897865",  "41,6496477", "-0,8883027")
    print('Distancia: ', km) #Distancia:  1.010759
    """
    calcula_tiempodistancia("41,644029", "-0,897865",  "41,6496477", "-0,8883027")
    pass

if __name__ == '__main__':
    main()