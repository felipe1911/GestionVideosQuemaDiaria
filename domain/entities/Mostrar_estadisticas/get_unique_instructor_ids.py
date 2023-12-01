def get_unique_instructor_ids(json_data):
    unique_ids = set()
    for course_data in json_data:
        unique_ids.add(course_data.get('id instructor'))
        for video_data in course_data.get('videos', []):
            unique_ids.add(video_data.get('id instructor'))

    return list(unique_ids)
