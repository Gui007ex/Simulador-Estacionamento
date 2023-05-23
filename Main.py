from os import system as sys
from Data.ParkingLot import ParkingLot
import Data.Verifier as Verifier

commands = '''
Processar entrada de carro (E)
Processar saída de carro (S)

-----> '''

my_lot = ParkingLot(4,4)

active = True
while active:
    sys('cls')
    my_lot.Show()
    action = input(commands).upper()
    match action:
        case 'E':
            pass
