from publisher import Publisher

from course import Course
from user import User

user_instance = User(
    id=1,
    name='John Doe',
    email='john.doe@example.com',
    phone_number='123-456-7890',
    goals=['Fitness', 'Learning', 'Productivity']
)

course_instance = Course(
    title='Python Programming',
    description='Learn Python from scratch to advanced topics.',
    instructor='Dr. Coding Guru',
    tags=['Programming', 'Python', 'Coding'],
    videos=['Introduction', 'Basic Syntax', 'Functions'],
    comments=['Great course!', 'Looking forward to more videos.']
)



publisher_instance = Publisher(course_instance)
publisher_instance.subscribe(user_instance,'email')
publisher_instance.subscribe(user_instance,'sms')

publisher_instance.notify_users()
