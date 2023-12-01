import json 

class LoadDataCommand:
    def __init__(self, json_file):
        self.json_file = json_file

    def execute(self):
        with open(self.json_file, 'r') as file:
            data = json.load(file)
        print(f"Data fetched from {self.json_file}.")
        return data
    
class UpdateJsonCommand:
    def __init__(self, file_path, new_data):
        self.file_path = file_path
        self.new_data = new_data

    def execute(self):
        with open(self.file_path, "w") as file:
            json.dump(self.new_data, file, indent=2)
        print(f"{self.file_path} file updated.")

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
        course_tags = self.course["tags"]
        common_tags = set(user_goals) & set(course_tags)
        similarity_score = len(common_tags) / len(set(user_goals)) * 100

        if similarity_score > 0:
            print(f"Similarity being calculated for user {user_id} and course {course_id}...")
            self.similarity_results.append({
                "user_id": user_id,
                "course_id": course_id,
                "similarity_score": similarity_score,
                "common_tags": common_tags
            })

class CheckAndApproveVideosCommand:
    def __init__(self, json_data):
        self.json_data = json_data

    def execute(self):
        instructors = self.json_data.get('instructors', [])

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

        update_command = UpdateJsonCommand('../data/database_data.json', self.json_data)
        update_command.execute()

class PrintStatsCommand:
    def __init__(self, instructor_data):
        self.instructor_data = instructor_data

    def execute(self):
        self.instructor_data = self.instructor_data["instructors"]
        for ins in self.instructor_data:
            StatsPrinter.print_stats(ins)

class StatsPrinter:
    @staticmethod
    def print_stats(instructor_data):
        print("------------------------------------------------------------------\n")
        print(f"Stats {instructor_data['name']}:\n")

        for course in instructor_data['courses']:
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

