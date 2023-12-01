import json
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
        print("------------------------------------------------------------------\n")
        print(f"Stats {self['name']}:\n")
        
        for course in self['courses']:
            print("\n")
            print(f"  Course: {course['title']}:\n")
            print(f"    Number of Subscribers: {len(course['subscribers'])}")
            print("    Subscribers:")
            for subscriber in course['subscribers']:
                print(f"      {subscriber}")
            print("\n")
            
            for video in course['videos']:

                if video['approved']:
                    print(f"    Video: {video['title']} of {course['title']}:\n")
                    print(f"      Likes: {video.get('likes', 0)}")

                    comments = video.get('comments', [])
                    print(f"      Number of comments: {len(comments)}")
                    print("      Comments:")
                    for comment in comments:
                        print(f"        {comment['user']}: {comment['comment']}")
                    print("\n")
                else:
                    print(f"    Video: {video['title']} of {course['title']}:\n")
                    print(f"      Video is not approved yet.")
                    print("\n")
                    

def update_redis(redis_data, database_data):
        if redis_data != database_data:
            with open("redis_data.json", "w") as redis_file:
                json.dump(database_data, redis_file, indent=2)
            print("redis_data.json updated.")

if __name__ == "__main__":
    # Read data from redis_data.json
    with open("redis_data.json", "r") as redis_file:
        redis_data = json.load(redis_file)

    # Read data from database_data.json
    with open("database_data.json", "r") as database_file:
        database_data = json.load(database_file)

    update_redis(redis_data, database_data)

    with open("redis_data.json", "r") as redis_file:
                redis_data = json.load(redis_file)

    for instructor in redis_data['instructors']:
        Instructor.print_stats(instructor)


