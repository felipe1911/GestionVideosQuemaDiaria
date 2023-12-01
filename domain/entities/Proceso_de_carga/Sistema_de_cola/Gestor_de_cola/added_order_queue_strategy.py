from .strategy_queue import StrategyQueue

class AddedOrderQueueStrategy(StrategyQueue):
    def order(self,videos:list):
        return videos