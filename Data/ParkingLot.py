from Data.States_refs import SearchState
from Data.Ticket_handle import CalcutateTicket
from random import randint

class Slot:
    def __init__(self) -> None:
        self.__free = True
        self.__plaque = None
        self.__state = None
        self.__entry = None
        self.__exit = None
    
    def AddCar(self, plaque):
        self.__free = False
        self.__plaque = plaque
        self.__state = SearchState(plaque[:3])

    def RemoveCar(self):
        self.__free = True
        self.__plaque = None
        self.__state = None

    def EntryTime(self, time):
        self.__entry = time

    def ExitTime(self, time):
        self.__exit = time

    def State(self):
        return self.__state
    
    def IsFree(self):
        return self.__free

    def Info(self):
        if self.__free:
            return " Livre "
        else:
            return self.__plaque

class ParkingLot:
    def __init__(self, m, n) -> None:
        self.__lot = [[Slot() for i in range(m)] for j in range(n)]
    
    def Place(self, plaque):
        y = randint(0,len(self.__lot)-1)
        x = randint(0,len(self.__lot[0])-1)
        this_slot = self.__lot[y][x]
        if this_slot.IsFree():
            this_slot.AddCar(plaque)
            return x, y
        else:
            self.Place(plaque)

    def Show(self):
        for line in self.__lot:
            show_line = []
            for slot in line:
                show_line.append(slot.Info())
            print(' | '.join(show_line))

    def IsFull(self):
        for line in self.__lot:
            for slot in line:
                if slot.IsFree():
                    return False
        return True