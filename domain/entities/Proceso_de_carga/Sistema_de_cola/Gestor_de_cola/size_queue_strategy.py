from .strategy_queue import StrategyQueue

class SizeOrderStrategy(StrategyQueue):
    def order(self,videos):
        return sorted(videos, key=lambda video: len(video.url))