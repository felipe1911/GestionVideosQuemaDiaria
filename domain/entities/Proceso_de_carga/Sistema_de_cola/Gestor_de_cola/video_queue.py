from .added_order_queue_strategy import AddedOrderQueueStrategy
from .size_queue_strategy import SizeOrderStrategy
from .duration_order_queue_strategy import DurationOrderStrategy
class VideoQueue:
    def __init__(self, videos):
        self.videos = videos
        self.orderStrategy = None

    def setOrderStrategy(self):
        if len(self.videos) <= 2:
            self.orderStrategy = AddedOrderQueueStrategy()
        elif 2 < len(self.videos) < 5:
            self.orderStrategy = SizeOrderStrategy()
        elif len(self.videos) == 5:
            self.orderStrategy = DurationOrderStrategy()

    def getOrder(self):
        return self.orderStrategy.order(self.videos)
