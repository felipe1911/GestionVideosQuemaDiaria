def create_course_dictionary(course):
    course_dictionary = {
        "title": course.title,
        "description": course.description,
        "instructor": course.instructor,
        "tags": course.tags,
        "videos": course.videos,
        "comments": course.comments
    }

    return course_dictionary