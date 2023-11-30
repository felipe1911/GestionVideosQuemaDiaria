class Course:
    def _init_(self, title, description, instructor, tags , videos=[], comments=[]):
        self.title = title
        self.description = description
        self.instructor = instructor
        self.tags = tags
        self.comments = comments
        self.videos = videos