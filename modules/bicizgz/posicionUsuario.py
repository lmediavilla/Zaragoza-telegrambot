import math as m
import pandas as df

def obtenerlistaPosicionUsuario(listaparadas, idUsuario, LatitudeUsuario, LongitudeUsuario):
    
        data = df.DataFrame(columns=('Distancia', 'UsuarioID', 'ParadaID', 'LatitudeUsuario', \
                                     'LongitudeUsuario', 'LatitudeParada', 'LongitudeParada'))

        for index, fila in listaparadas.iterrows():
            
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


def calcula_distancia(strLatitudeOrigen='0', strLongitudeOrigen='0',    \
                          strLatitudeDestino='0', strLongitudeDestino='0'):

        RADIO_TIERRA = 6371

        try:
            LatitudeOrigen=float(strLatitudeOrigen.replace(',','.'))
            LongitudeOrigen=float(strLongitudeOrigen.replace(',','.'))
        except:
            LatitudeOrigen=float(strLatitudeOrigen)
            LongitudeOrigen=float(strLongitudeOrigen)
        try:
            LatitudeDestino=float(strLatitudeDestino.replace(',','.'))
            LongitudeDestino=float(strLongitudeDestino.replace(',','.'))
        except:
            LatitudeDestino=float(strLatitudeDestino)
            LongitudeDestino=float(strLongitudeDestino)
   
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
    pass

if __name__ == '__main__':
    main()