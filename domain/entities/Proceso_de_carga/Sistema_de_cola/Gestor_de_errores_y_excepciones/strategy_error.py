from abc import ABC, abstractmethod

class StrategyError(ABC):
    @abstractmethod
    def get_error():
        pass