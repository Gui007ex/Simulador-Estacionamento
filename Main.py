from os import system as sys
from Data.ParkingLot import ParkingLot
import Data.Verifier as Verifier
from Data.States_refs import SearchState
from Data.Ticket_handle import Format

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
            if my_lot.IsFull():
                input('\nEstacionamento cheio...')
            else:
                placa = input('\nPlaca: ').upper()
                horario = input('Horário (entrada): ')
                if Verifier.isPlaque(placa) and Verifier.isHour(horario):
                    x, y = my_lot.Place(placa, horario)
                    sys('cls')
                    my_lot.Show()
                    input(f'\nCarro alocado ({y+1},{x+1})\n\nHorário de entrada: {horario}\nPlaca: {placa}\nEstado: {SearchState(placa)}\n\n...')
                else:
                    input('\nPlaca e(ou) Horário inválido(s)...')
        case 'S':
            if my_lot.isEmpty():
                input('\nEstacionamento vazio...')
            else:
                placa = input('\nPlaca: ').upper()
                horario = input('Horário de saída: ')
                if Verifier.isPlaque(placa) and Verifier.isHour(horario):
                    ticket, time = my_lot.Exit(placa, horario)
                    if ticket == None:
                        input('\nPlaca não encontrada...')
                    else:
                        sys('cls')
                        my_lot.Show()
                        input(f'\nCarro removido\n\nEntrada e Saída: {time}/{horario}\nTempo de permanência: {Format(time,horario)}\nValor do ticket: R${ticket},00\n\n...')
                else:
                    input('\nPlaca e(ou) Horário inválido(s)...')