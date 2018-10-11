import math as m

RADIO_TIERRA = 6371

class posicionUsuario():

    
    def __init__(self):
        pass

    def calcula_distancia(self, strLatitudeOrigen='0', strLongitudeOrigen='0',    \
                                strLatitudeDestino='0', strLongitudeDestino='0'):
        
        LatitudeOrigen=float(strLatitudeOrigen.replace(',','.'))
        LongitudeOrigen=float(strLongitudeOrigen.replace(',','.'))
        LatitudeDestino=float(strLatitudeDestino.replace(',','.'))
        LongitudeDestino=float(strLongitudeDestino.replace(',','.'))
   
        Distancia_Km = RADIO_TIERRA * m.acos(
                                             m.cos(m.radians(90-LatitudeOrigen)) * m.cos(m.radians(90-LatitudeDestino)) + 
                                             m.sin(m.radians(90-LatitudeOrigen)) * m.sin(m.radians(90-LatitudeDestino)) *
                                             m.cos(m.radians(LongitudeOrigen-LongitudeDestino))
                                            )

        return round(Distancia_Km, 7)


def main():
    
    pu = posicionUsuario()
    km=pu.calcula_distancia("41,644029", "-0,897865",  "41,6496477", "-0,8883027")
    print('Distancia: ', km) #Distancia:  1.010759

if __name__ == '__main__':
    main()