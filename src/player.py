# Write a class to hold player information, e.g. what room they are in
# currently.

class Player:
    def __init__(self, name, current_room, inventory=None):
        self.name = name
        self.current_room = current_room
        self.inventory = inventory
    
    def _str_(self):
        return f"{self.name} is in the {self.current_room.name}"
        