import random
from typing import Type

from abstractions.behavior import Behavior


class Player:
    def __init__(self, id, behavior: Type[Behavior], balance=300):
        self.id = id
        self.behavior = behavior()
        self.balance = balance
        self.last_dices = 0
        self._currently_position = 0
        self.playing = True
        self.properties = []

    @property
    def currently_position(self):
        return self._currently_position

    @currently_position.setter
    def currently_position(self, value):
        self._currently_position += value
        if self._currently_position >= 20:
            self._currently_position -= 20

    def __str__(self):
        return f'{self.id} - R${self.balance} - Playing: {self.playing}'

    def roll_dices(self) -> int:
        self.last_dices = random.randint(1, 6)
        return self.last_dices

    def pay_rent(self, rent):
        self.balance -= rent

    def receive_rent(self, rent):
        self.balance += rent

    def _buy(self, property):
        if self.behavior.action() == 'impulsive':
            self.balance -= property.value
            property.include_owner(self)
            self.properties.append(property)
        if self.behavior.action() == 'aleatory':
            if random.randint(0, 1):
                self.balance -= property.value
                property.include_owner(self)
                self.properties.append(property)
        if self.behavior.action() == 'demanding':
            if property.rent > 50:
                self.balance -= property.value
                property.include_owner(self)
                self.properties.append(property)
        if self.behavior.action() == 'prudent':
            if self.balance - property.value >= 80:
                self.balance -= property.value
                property.include_owner(self)
                self.properties.append(property)

    def buy_or_pay(self, property):
        if not self.playing:
            return
        if not property.position:
            self.balance += property.value
            return

        if self.currently_position > 20:
            self.balance += 100

        if not property.check_if_owned():
            if self.is_possible_to_buy(property.value):
                self._buy(property)
        else:
            self.balance -= property.rent
            property.owner.balance += property.rent

        self.check_if_it_is_over_for_this_player()

    def check_if_it_is_over_for_this_player(self):
        if self.balance < 0:
            self.playing = False
            for property in self.properties:
                property.owner = None

    def is_possible_to_buy(self, value) -> bool:
        currently_cash = self.balance
        return (currently_cash - value) > 0
