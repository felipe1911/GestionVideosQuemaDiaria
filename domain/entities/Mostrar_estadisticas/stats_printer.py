from .get_courses_by_instructor import get_courses_by_instructor
from .get_unique_instructor_ids import get_unique_instructor_ids

class StatsPrinter:
    @staticmethod
    def print_stats(instructor_id,course_data):
        print("------------------------------------------------------------------\n")

        specific_course_data = get_courses_by_instructor(course_data, instructor_id)

        for course in specific_course_data:
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