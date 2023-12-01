from .strategy_error import StrategyError

class SizeStrategyError(StrategyError):
    def get_error(self):
        return 1