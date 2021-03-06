class Parada:
    #datos que proporciona el json
    StationID = ''
    DisctrictCode = ''
    AddressGmapsLatitude = ''
    AddressGmapsLongitude = ''
    StationAvailableBikes = ''
    StationFreeSlot = ''
    AddressZipCode = ''
    AddressStreet1 = ''
    AddressNumber = ''
    NearbyStationList = ''
    StationStatusCode = ''
    StationName = ''
    def __init__(self, StationID, DisctrictCode, AddressGmapsLatitude, AddressGmapsLongitude,   \
                StationAvailableBikes, StationFreeSlot, AddressZipCode, AddressStreet1,         \
                 AddressNumber, NearbyStationList, StationStatusCode, StationName):

        #constructor del objeto
        self.StationID = StationID
        self.DisctrictCode = DisctrictCode
        self.AddressGmapsLatitude = str(round(float(AddressGmapsLatitude), 7))
        self.AddressGmapsLongitude =  str(round(float(AddressGmapsLongitude), 7))
        self.StationAvailableBikes = StationAvailableBikes
        self.StationFreeSlot = StationFreeSlot
        self.AddressZipCode = AddressZipCode
        self.AddressStreet1 = AddressStreet1
        self.AddressNumber = AddressNumber
        self.NearbyStationList = NearbyStationList
        self.StationStatusCode = StationStatusCode
        self.StationName = StationName
    def __repr__(self):
        #ésto define como se imprime el objeto
        s = f'\nStationID -> {self.StationID}                           \
              \nDisctrictCode -> {self.DisctrictCode}                   \
              \nAddressGmapsLatitude -> {self.AddressGmapsLatitude}     \
              \nAddressGmapsLongitude -> {self.AddressGmapsLongitude}   \
              \nStationAvailableBikes -> {self.StationAvailableBikes}   \
              \nStationFreeSlot -> {self.StationFreeSlot}               \
              \nAddressZipCode -> {self.AddressZipCode}                 \
              \nAddressStreet1 -> {self.AddressStreet1}                 \
              \nAddressNumber -> {self.AddressNumber}                   \
              \nNearbyStationList -> {self.NearbyStationList}           \
              \nStationStatusCode -> {self.StationStatusCode}           \
              \nStationName -> {self.StationName}                       \
              \n'
        return s

def main():
    pass

if __name__ == '__main__':
    main()
