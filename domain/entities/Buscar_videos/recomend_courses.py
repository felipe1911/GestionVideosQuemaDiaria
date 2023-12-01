from .calculate_similarity import CalculateSimilarityCommand

class RecommendCourses:
    def __init__(self, user):
        self.similarity_results = []
        self.user = user

    def find_recommendations(self, user):
        for course in self.data:
            instructor = course['instructor']
            CalculateSimilarityCommand(user, instructor, course, self.similarity_results).execute()

        self.similarity_results.sort(key=lambda x: x["similarity_score"], reverse=True)