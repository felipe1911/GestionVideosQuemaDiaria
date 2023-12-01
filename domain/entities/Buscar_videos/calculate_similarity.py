class CalculateSimilarityCommand:
    def __init__(self, user, instructor, course, similarity_results):
        self.user = user
        self.instructor = instructor
        self.course = course
        self.similarity_results = similarity_results

    def execute(self):

        user_id = self.user.id
        user_name = self.user.name
        user_goals = self.user.goals
        course_title = self.course['title']
        course_tags = self.course["tags"]
        common_tags = set(user_goals) & set(course_tags)
        similarity_score = len(common_tags) / len(set(user_goals)) * 100

        if similarity_score > 0:
            print(f"Similitud siendo calculada para {user_name} and curso {course_title}...")
            self.similarity_results.append({
                'title': course_title,
                "similarity_score": similarity_score,
                "common_tags": common_tags
            })