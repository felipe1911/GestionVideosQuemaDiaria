from .strategy_error import StrategyError

class NoErrorStrategyError(StrategyError):
    def get_error(self):
        return 0