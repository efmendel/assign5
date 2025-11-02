import re
class Location:
    def __init__(self, city: str, state: str, country: str):
        self.city = city
        self.state = state
        self.country = country
        
    def valid_location(self) -> bool:
        pattern = r"^(?P<city>[a-zA-Z]+), (?P<state>[A-Z]{2}), (?P<country>[A-Z]{2})$"
        location_string = f"{self.city}, {self.state}, {self.country}"
        return re.match(pattern, location_string) is not None