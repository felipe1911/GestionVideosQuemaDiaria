from upload_facade import upload_facade
from instructor import Instructor
from course import Course

instructor1 = Instructor(1, 'Ana','ana@gmail.com', '123456789')

course1 = Course('Baja la panza', 'Curso para bajar la panza', instructor1, ['panza'])
course2 = Course('Aumenta la nalga', 'Curso para aumentar la nalga', instructor1, ['nalga'])

instructor1.courses.append(course1)
instructor1.courses.append(course2)
upload_facade(instructor1)