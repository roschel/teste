from typing import Union

from model.property import Property

properties = {
    0: Property(name="Initial", position=0, rent=0, value=100),
    1: Property(name="Leblon", position=1, rent=50, value=100),
    2: Property(name="Av. Presidente Vargas", position=2, rent=75, value=125),
    3: Property(name="Av.Nossa S. de Copacabana", position=3, rent=150, value=200),
    4: Property(name="Av. Brigadeiro Faria Lima", position=4, rent=180, value=300),
    5: Property(name="Av. Rebouças", position=5, rent=400, value=600),
    6: Property(name="Av. 9 de Julho", position=6, rent=400, value=600),
    7: Property(name="Av. Europa", position=7, rent=800, value=1000),
    8: Property(name="Rua Augusta", position=8, rent=90, value=120),
    9: Property(name="Av. Pacaembú", position=9, rent=750, value=900),
    10: Property(name="Interlagos", position=10, rent=600, value=700),
    11: Property(name="Morumbi", position=11, rent=550, value=750),
    12: Property(name="Flamengo", position=12, rent=400, value=900),
    13: Property(name="Botafogo", position=13, rent=350, value=730),
    14: Property(name="Av. Brasil", position=14, rent=250, value=840),
    15: Property(name="Av. Paulista", position=15, rent=1000, value=1100),
    16: Property(name="Jardim Europa", position=16, rent=780, value=900),
    17: Property(name="Copacabana", position=17, rent=2000, value=3000),
    18: Property(name="Av.Vieira Souto", position=18, rent=50, value=100),
    19: Property(name="Av. Atlântica", position=19, rent=890, value=1500),
    20: Property(name="Ipanema", position=20, rent=570, value=1200)
}


class Board:
    def __init__(self, position=0):
        self.position = position
        self.currently_position = 0

    def play_round(self, dices) -> Union[Property, int]:
        self.currently_position = self.position + dices if self.position else dices
        if self.currently_position >= 20:
            self.currently_position -= 20
        return properties[self.currently_position]
