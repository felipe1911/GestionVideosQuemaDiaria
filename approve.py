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
            subscribers = []
            
            for video in course['videos']:
                subscribers.extend(video.get('subscribers', []))

                print(f"    Video: {video['title']} of {course['title']}:\n")
                print(f"      Likes: {video.get('likes', 0)}")

                comments = video.get('comments', [])
                print(f"      Number of comments: {len(comments)}")
                print("      Comments:")
                for comment in comments:
                    print(f"        {comment['user']}: {comment['comment']}")
                print("\n")
                

            print(f"  Number of Subscribers: {len(set(subscribers))}")
            print("  List of Subscribers:")
            for subscriber in set(subscribers):
                print(f"      {subscriber}")

class Moderator:
    def __init__(self, id: int, name: str, email: str) -> None:
        self.id = id
        self.name = name
        self.email = email

    def check_and_approve_videos(self, json_data):
        instructors = json_data.get('instructors', [])

        for instructor_data in instructors:
            courses = instructor_data.get('courses', [])

            for course_data in courses:
                videos = course_data.get('videos', [])

                for video_data in videos:
                    title = video_data.get('title', '')
                    approved = video_data.get('approved', False)

                    if not approved:  # Only prompt for approval if the video is not approved
                        print(f"\nVideo: {title}\nApproved: {approved}")

                        decision = input("Do you approve this video? (yes/no): ").lower()

                        if decision == 'yes':
                            video_data['approved'] = True
                            print(f"{title} approved!\n")
                        elif decision == 'no':
                            video_data['approved'] = False
                            print(f"{title} disapproved.\n")
                        else:
                            print("Invalid input. Please enter 'yes' or 'no'.\n")


        # Update the JSON file with the modified data
        with open('database_data.json', 'w') as database_data:
            json.dump(json_data, database_data, indent=2)


if __name__ == "__main__":
    # Read data from redis_data.json
    with open("redis_data.json", "r") as redis_file:
        redis_data = json.load(redis_file)

    # Read data from database_data.json
    with open("database_data.json", "r") as database_file:
        database_data = json.load(database_file)

    moderator = Moderator(id=1, name="John", email="john@example.com")
    moderator.check_and_approve_videos(database_data)


