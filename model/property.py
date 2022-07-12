from model.player import Player


class Property:
    def __init__(self, name, rent, value, position):
        self.name = name
        self.rent = rent
        self.value = value
        self.position = position
        self.owner: Player = None

    def include_owner(self, owner: Player):
        self.owner = owner

    def check_if_owned(self) -> Player:
        return self.owner

    def __str__(self):
        return f'{self.name} - {self.position}'
