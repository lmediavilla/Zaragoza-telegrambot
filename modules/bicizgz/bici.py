import conexion
import listaparada
import posicionUsuario

class bici:

    def __init__(self):
        #print('init')
        pass
    
    def obtenlistaParadas(self):
        return conexion.obtenlistaParadas()




def main():
    c = bici()
    print(c.obtenlistaParadas())
    #conexion()
    del c

if __name__ == '__main__':
    main()