from .calculate_similarity import CalculateSimilarityCommand

class RecommendCourses:
    def __init__(self, user, data):
        self.data = data
        self.similarity_results = []
        self.user = user

    def find_recommendations(self):
        for course in self.data:
            instructor = course['id instructor']
            
            CalculateSimilarityCommand(self.user, instructor, course, self.similarity_results).execute()

        self.similarity_results.sort(key=lambda x: x["similarity_score"], reverse=True)