from Data.States_refs import SearchState
from Data.Ticket_handle import CalculateTicket
from random import randint

class Slot:
    def __init__(self) -> None:
        self.__free = True
        self.__plaque = None
        self.__state = None
        self.__entry = None
    
    def AddCar(self, plaque, time):
        self.__free = False
        self.__plaque = plaque
        self.__state = SearchState(plaque[:3])
        self.__entry = time

    def RemoveCar(self, time):
        price = CalculateTicket(self.__entry, time)
        self.__free = True
        self.__plaque = None
        self.__state = None
        self.__entry = None
        return price

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
    
    def Place(self, plaque, time):
        y = randint(0,len(self.__lot)-1)
        x = randint(0,len(self.__lot[0])-1)
        this_slot = self.__lot[y][x]
        if this_slot.IsFree():
            this_slot.AddCar(plaque, time)
            return x, y
        else:
            self.Place(plaque)

    def Exit(self, plaque, time):
        for line in self.__lot:
            for slot in line:
                if plaque == slot.Info():
                    return slot.RemoveCar(time)
        return None

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