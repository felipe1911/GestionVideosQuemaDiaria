from abc import ABC, abstractmethod

class StrategyQueue(ABC):
    @abstractmethod
    def order():
        pass