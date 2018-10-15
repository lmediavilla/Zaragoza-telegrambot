import conexion
import listaparada
import posicionUsuario
import pandas as pd

class bici:

    def __init__(self):
        #print('init')
        pass
    
    def obtenlistaParadas(self):
        return conexion.obtenlistaParadas()

    def obtenlistaDistanciaUsuario(self, listaparadas, idUsuario='0', LatitudeUsuario='0', LongitudeUsuario='0'):
        listakm = posicionUsuario.obtenerlistaPosicionUsuario(listaparadas, idUsuario, LatitudeUsuario, LongitudeUsuario)
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
           listaresult.append([
                                str(filtro['StationID']),
                                str(filtro['AddressGmapsLatitude']),
                                str(filtro['AddressGmapsLongitude']),
                                str(filtro['StationAvailableBikes']) + " " + \
                                str(filtro['StationFreeSlot']) + " {" + str(filtro['AddressStreet1']) +"}"
                              ])

        return listaresult
          
          
        


def main():
    c = bici()
    print(c.obtenlistaParadas())

    lp = pd.read_csv('paradas.csv', sep=',',header=0)
    print(f'{c.obtenlistaDistanciaUsuario( lp, "1234567", "41.6218009", "-0.9523861")}')

    del c

if __name__ == '__main__':
    main()