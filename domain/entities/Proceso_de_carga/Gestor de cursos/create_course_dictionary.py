def create_course_dictionary(course):
    course_dictionary = {
        "title": course.title,
        "description": course.description,
        "id instructor": course.instructor.id,
        "tags": course.tags,
        "videos": course.videos,
        "comments": course.comments
    }

    return course_dictionary