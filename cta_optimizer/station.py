from cta_optimizer.location import Location

class Station:
    def __init__(self, name: str, location: Location):
        self.__validate_name(name)
        self.__validate_location(location)

        self.name = name
        self.location = location

        self.adjacent_stations = set()

    def add_adjacent_station(self, station: "Station"):
        self.__validate_station(station)
        self.adjacent_stations.add(station)

    def remove_adjacent_station(self, station: "Station"):
        self.__validate_station(station)
        self.adjacent_stations.remove(station)

    def get_adjacent_stations(self):
        return self.adjacent_stations

    def get_name(self):
        return self.name

    def get_location(self):
        return self.location

    def __str__(self):
        return f"Station: {self.name} ({self.location})"

    def __eq__(self, other):
        if not isinstance(other, Station):
            return False

        return self.name == other.name and self.location == other.location

    def __hash__(self):
        return hash((self.name, self.location))

    @staticmethod
    def __validate_name(name: str):
        if name is None:
            raise ValueError("Name cannot be None")

        if not isinstance(name, str):
            raise ValueError("Name must be a string")

        if len(name) == 0:
            raise ValueError("Name cannot be empty")

    @staticmethod
    def __validate_location(location: Location):
        if location is None:
            raise ValueError("Location cannot be None")

        if not isinstance(location, Location):
            raise ValueError("Location must be a Location object")

    def __validate_station(self, station: "Station"):
        if station is None:
            raise ValueError("Station cannot be None")

        if not isinstance(station, Station):
            raise ValueError("Station must be a Station object")

        if station == self:
            raise ValueError("Station cannot be adjacent to itself")