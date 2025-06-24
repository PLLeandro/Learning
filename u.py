class Room:
    def __init__(self, id: str, floor: int, seats: int):
        self._id = id
        self._floor = floor
        self._seats = seats
        self._area = seats *2

    def get_id(self) -> str:
        return self._id

    def get_floor(self) -> int:
        return self._floor

    def get_seats(self) -> int:
        return self._seats

    def get_area(self) -> int:
        return self._area


class Building:
    def __init__(self, name: str, address: str, floors: range):
        self._name = name
        self._address = address
        self._floors = floors  # Deve essere un oggetto di tipo range
        self._rooms = []

    def get_floors(self) -> range:
        return self._floors

    def get_rooms(self) -> list:
        return self._rooms

    def add_room(self, room: Room) -> None:
        if room.get_floor() in self._floors:
            self._rooms.append(room)
        else:
            print(f"Impossibile aggiungere l'aula {room.get_id()}: piano {room.get_floor()} fuori dall'intervallo {self._floors}.")







def area(self.get_area) -> int:
        return sum(room.get_area() for room in self._rooms)
