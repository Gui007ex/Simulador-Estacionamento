from os import system as sys
from Data.ParkingLot import ParkingLot

my_lot = ParkingLot(4,4)

while True:
    option = input()
    my_lot.Place(option)
    sys('cls')
    my_lot.Show()
