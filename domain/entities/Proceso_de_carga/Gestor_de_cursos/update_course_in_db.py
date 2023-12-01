import json

def update_course_in_db(original_course,modified_course):
    title_to_find = original_course.title
    print(title_to_find)
    with open('domain\database\database_courses.json', 'r') as file:
        data = json.load(file)

    for course in data:
        if course.get("title") == title_to_find:
            # Update the fields
            course["title"] = modified_course.title
            course["description"] = modified_course.description
            course["tags"] = modified_course.tags

            # Rewrite the JSON file
            with open('domain\database\database_courses.json', 'w') as file:
                json.dump(data, file, indent=2)
            
            print(f"Curso con el titulo '{title_to_find}' actualizado correctamente.")
            return

    print(f"Curso con el titulo  '{title_to_find}' no fue encontrado")