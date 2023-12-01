class Course:
    def __init__(self, title, description, instructor, tags , videos=[], comments=[]):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.subcribers = []
        self.tags = tags
        self.comments = comments
        self.videos = videos