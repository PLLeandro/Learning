class Room:
    def __init__(self, id:str, floor:int, seats:int):
        self.id=id
        self.floor=floor
        self.seats=seats
        self.area=seats*2
    
    def getId(self)->str:
        return self.id
    def getFloor(self)->int:
        return self.floor
    def getSeats(self)->int:
        return self.seats
    def get_area(self)->int:
        return self.area
    
class Bulding:
    def __init__(self, name:str, address:str, floors:range):
        self.name=name
        self.address=address
        self.floors=floors
        self.rooms=[]

    def getFloors(self)->range:
        return self.floors
    def getRooms(self)->list:
        return self.rooms
    def addRoom(self, room: Room) ->None:
        if room.getFloor() in self.floors:
            self.rooms.append(room)
    def aera(self)->int:
        return sum(room.get_area()for room in self.rooms)