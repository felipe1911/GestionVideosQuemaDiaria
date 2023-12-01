def get_courses_by_instructor(json_data, id_instructor):
    print(id_instructor)
    matching_courses = []
    for course_data in json_data:
        if course_data['id instructor'] == id_instructor:
            matching_courses.append(course_data)

    return matching_courses
