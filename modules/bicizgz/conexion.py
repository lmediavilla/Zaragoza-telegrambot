import requests
from json import loads
from modules.bicizgz.parada import Parada
import pandas as pd
import logging

def cleanCsv():
    #limpiar Csv una vez redescubro las paradas
    df = pd.read_csv('paradas.csv', sep=',',header=0)
    i = 0
    for i in range(0,len(df)):
        df = df[df['StationID'] == i]
        logging.info(f'borrado {i}')
    df.to_csv('paradas.csv',sep=',',encoding='utf-8',index=False) 
    
def csvToList():
    df = pd.read_csv('paradas.csv', sep=',',header=0)
    return  df.values.tolist()

def listToCsv(lista):
    df = pd.DataFrame(lista, columns=['StationID',"DisctrictCode","AddressGmapsLatitude","AddressGmapsLongitude","StationAvailableBikes","StationFreeSlot","AddressZipCode","AddressStreet1","AddressNumber","NearbyStationList","StationStatusCode","StationName"])
    df.to_csv('paradas2.csv',sep=',',encoding='utf-8',index=False) 
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
        df.loc[len(df)]=[
                            P.StationID,                \
                            P.DisctrictCode,            \
                            P.AddressGmapsLatitude,     \
                            P.AddressGmapsLongitude,    \
                            P.StationAvailableBikes,    \
                            P.StationFreeSlot,          \
                            P.AddressZipCode,           \
                            P.AddressStreet1,           \
                            P.AddressNumber,            \
                            P.NearbyStationList,        \
                            P.StationStatusCode,        \
                            P.StationName               \
                        ]
        del P
    df.to_csv('paradas.csv',sep=',',encoding='utf-8',index=False)  
    return listaParadas


def main():
    #print(obtenlistaParadas())
    listToCsv(csvToList())
if __name__ == '__main__':
    main()