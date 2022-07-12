from abc import ABC, abstractmethod


class Behavior(ABC):

    @abstractmethod
    def action(self):
        pass
