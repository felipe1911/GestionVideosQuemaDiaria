from .update_json_command import UpdateJsonCommand

class CheckAndApproveVideosCommand:
        
    def __init__(self, json_data):
        self.json_data = json_data

    def execute(self):
        for course_data in self.json_data:
            print(course_data)
            videos = course_data.get('videos', [])
            for video_data in videos:
                title = video_data['title']
                approved = video_data.get('approved', False)
                
                if not approved:
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
        update_command = UpdateJsonCommand('domain\database\database_courses.json', self.json_data)
        update_command.execute()