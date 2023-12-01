class CalculateSimilarityCommand:
    def __init__(self, user, instructor, course, similarity_results):
        self.user = user
        self.instructor = instructor
        self.course = course
        self.similarity_results = similarity_results

    def execute(self):

        user_id = self.user["id"]
        
        user_goals = self.user["goals"]
        course_id = self.course["id"]
        course_title = self.course['title']
        course_tags = self.course["tags"]
        common_tags = set(user_goals) & set(course_tags)
        similarity_score = len(common_tags) / len(set(user_goals)) * 100

        if similarity_score > 0:
            print(f"Similitud siendo calculada para {user_id} and curso {course_title}...")
            self.similarity_results.append({
                "course_id": course_id,
                'course_title': course_title,
                "similarity_score": similarity_score,
                "common_tags": common_tags
            })