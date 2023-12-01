from .strategy_queue import StrategyQueue

class DurationOrderStrategy(StrategyQueue):
    def order(self,videos):
        return sorted(videos, key=lambda video: video.duration)