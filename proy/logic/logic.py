import sys

sys.path.append('C:\\Users\\lunag\\OneDrive - Universidad del rosario\\2023-2-DESKTOP-7JL5SLU\\arqui\\proy')

from commands.commands import *
from strategy.strategy import *

class Instructor:
    def __init__(self, id: int, name: str, email: str, phone_number: int) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.courses = []

    class Course:
        def __init__(self, id, title, description, tags):
            self.id = id
            self.title = title
            self.description = description
            self.tags = tags
            self.videos = []
            self.subscribers = []  # Track users subscribed to the course

        class Video:
            def __init__(self, id, title, tags, author, url, duration, comments=None, likes=None):
                self.id = id
                self.title = title
                self.tags = tags
                self.author = author
                self.url = url
                self.duration = duration
                self.comments = comments or []
                self.likes = likes or 0
                self.approved = False

    def print_stats(self):
        stats_command = StatsCommand(self)
        stats_command.execute()

class Moderator:
    def __init__(self, id: int, name: str, email: str) -> None:
        self.id = id
        self.name = name
        self.email = email

    def check_and_approve_videos(self, json_data):

        check_approve_command = CheckAndApproveVideosCommand(json_data)
        check_approve_command.execute()

class User:
    def __init__(self, id: int, name: str, email: str, phone_number: int, goals=None) -> None:
        self.id = id
        self.name = name
        self.email = email
        self.phone_number = phone_number
        self.subscriptions = []
        self.goals = goals or []

class RecommendCourses:
    def __init__(self, data):
        self.data = data
        self.similarity_results = []

    def find_recommendations(self):
        for user in self.data["users"]:
            for instructor in self.data["instructors"]:
                for course in instructor["courses"]:
                    course_id = course["id"]
                    if course_id not in user["subscriptions"]:
                        CalculateSimilarityCommand(user, instructor, course, self.similarity_results).execute()

        self.similarity_results.sort(key=lambda x: x["similarity_score"], reverse=True)

class DisplayRecommendations:
    def __init__(self, recommendations):
        self.recommendations = recommendations

    def display(self):
        for result in self.recommendations:
            print(f"User: {result['user_id']}, Course: {result['course_id']}, Similarity Score: {result['similarity_score']} %")
            print(f"Common Tags: {', '.join(result['common_tags'])}")
            print("\n")


if __name__ == "__main__":
    db_data = LoadDataCommand('../data/database_data.json').execute()
    redis_data = LoadDataCommand('../data/redis_data.json').execute()

    strategy = DataLoadStrategy()
    instructor_data = strategy.load_data()

    printStatsCommand = PrintStatsCommand(instructor_data)
    printStatsCommand.execute()

    moderator = Moderator(id=1, name="John", email="john@example.com")
    moderator.check_and_approve_videos(db_data)

    recommendation_engine = RecommendCourses(db_data)
    recommendation_engine.find_recommendations()

    display_engine = DisplayRecommendations(recommendation_engine.similarity_results)
    display_engine.display()


    