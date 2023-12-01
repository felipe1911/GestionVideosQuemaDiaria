from .strategy_error import StrategyError

class BannedUserStrategyError(StrategyError):
    def get_error(self):
        return 2