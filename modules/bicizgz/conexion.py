import requests
from json import loads
from parada import Parada

def obtenlistaParadas():
    #devolvemos json en bruto
    URL = 'https://www.bizizaragoza.com/sites/default/files/stations/station_list.json'
    response = loads(requests.get(URL, timeout=3).text)
    #print(response)
    listaParadas = []
    for element in response:
        print(element['StationID'])
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
        del P
    return listaParadas


def main():
    print(obtenlistaParadas())
if __name__ == '__main__':
    main()