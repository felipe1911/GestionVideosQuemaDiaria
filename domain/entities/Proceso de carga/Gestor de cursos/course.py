class Course:
    def _init_(self, title, description, goals, instructor, tags = None, videos=[], comments=[]):
        self.title = title
        self.description = description
        self.goals = goals
        self.tags = tags
        self.instructor = instructor
        self.comments = comments
        self.videos = videos