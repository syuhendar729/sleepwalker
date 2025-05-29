from abc import ABC, abstractmethod

class Obstacle(ABC):
    def __init__(self, x, y):
        self.x = x
        self.y = y

    @abstractmethod
    def draw(self, screen):
        pass

    @abstractmethod
    def interact(self, player):
        pass
