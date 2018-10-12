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
        return posicionUsuario.obtenerlistaPosicionUsuario(listaparadas, idUsuario, LatitudeUsuario, LongitudeUsuario)
          
          
        


def main():
    c = bici()
    print(c.obtenlistaParadas())

    lp = pd.read_csv('paradas.csv', sep=',',header=0)
    print(c.obtenlistaDistanciaUsuario( lp, "1234567", "41.6218009", "-0.9523861",))

    del c

if __name__ == '__main__':
    main()