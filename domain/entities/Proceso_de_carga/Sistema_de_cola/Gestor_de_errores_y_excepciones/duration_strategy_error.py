from .strategy_error import StrategyError

class DurationStrategyError(StrategyError):
    def get_error(self):
        return 3