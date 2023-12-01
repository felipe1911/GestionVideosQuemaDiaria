from .no_error_strategy import NoErrorStrategyError
from .size_strategy_error import SizeStrategyError
from .banned_user_strategy_error import BannedUserStrategyError
from .duration_strategy_error import DurationStrategyError

class VideoError:
    def __init__(self, video, instructor):
        self.video = video
        self.instructor = instructor
        self.errorStrategy = None

    def setErrorStrategy(self):
        if self.instructor.banned == True:
            self.errorStrategy = BannedUserStrategyError()
        elif len(self.video.url) > 40:
            self.errorStrategy = SizeStrategyError()
        elif self.video.duration > 2700:
            self.errorStrategy = DurationStrategyError()
        else:
            self.errorStrategy = NoErrorStrategyError()

    def getErrorId(self):
        return self.errorStrategy.get_error()