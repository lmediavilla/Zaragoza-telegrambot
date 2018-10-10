import requests
from json import loads
from parada import Parada
import pandas as pd

def cleanCsv():
    #limpiar Csv una vez redescubro las paradas
    df = pd.read_csv('paradas.csv', sep=',',header=0)
    #print(f'len(df) -> {len(df)}')
    i = 0
    for i in range(0,len(df)):
        df = df[df['StationID'] == i]
        print(f'borrado {i}')
    df.to_csv('paradas.csv',sep=',',encoding='utf-8',index=False) 
    

def obtenlistaParadas():
    #devolvemos json en bruto
    URL = 'https://www.bizizaragoza.com/sites/default/files/stations/station_list.json'
    response = loads(requests.get(URL, timeout=3).text)
    listaParadas = []
    cleanCsv()
    df = pd.read_csv('paradas.csv', sep=',',header=0)
    for element in response:
        P = Parada( element['StationID'], 
                    element['DisctrictCode'],
                    element['AddressGmapsLatitude'],
                    element['AddressGmapsLongitude'],
                    element['StationAvailableBikes'], 
                    element['StationFreeSlot'], 
                    element['AddressZipCode'], 
                    element['AddressStreet1'], 
                    element['AddressNumber'],
                    element['NearbyStationList'], 
                    element['StationStatusCode'], 
                    element['StationName']
                  )
        listaParadas.append(P)
        df.loc[len(df)]=[P.StationID,P.DisctrictCode,P.AddressGmapsLatitude,P.AddressGmapsLongitude,P.StationAvailableBikes,P.StationFreeSlot,P.AddressZipCode,P.AddressStreet1,P.AddressNumber,P.NearbyStationList,P.StationStatusCode,P.StationName]
        #esto es un poco cutre, escribir el fichero n veces
        df.to_csv('paradas.csv',sep=',',encoding='utf-8',index=False)   
        del P
    return listaParadas


def main():
    print(obtenlistaParadas())
if __name__ == '__main__':
    main()