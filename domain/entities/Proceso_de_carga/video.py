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

    def __str__(self) -> str:
        return self.name
    
    