import json

# function to add to JSON
def write_json(new_data, filename, indent):
    with open(filename,'r+') as file:
          # First we load existing data into a dict.
        file_data = json.load(file)
        # Join new_data with file_data inside emp_details
        file_data.append(new_data)
        # Sets file's current position at offset.
        file.seek(0)
        # convert back to json.
        json.dump(file_data, file, indent=indent)

def p2p(videos,course):
    for video in videos:
        print("\n Nodo 1 agregando metadata a la SAN")
        metadata = {
            "id": video.id,
            "title": video.title,
            "tags": video.tags,
            "author": video.author.name,
            "duration": video.duration,
            "comments": video.comments,
            "likes": video.likes,
            "approved": video.approved
        }
        write_json(metadata,'domain\san\san.json',8)

        print("\n Nodo 2 agregando data a la base de datos")
        data = {
            "id": video.id,
            "title": video.title,
            "tags": video.tags,
            "author": video.author.name,
            "url": video.url,
            "duration": video.duration,
            "comments": video.comments,
            "likes": video.likes,
            "approved": video.approved
        }
        write_json(data,'domain\database\database_videos.json',9)

        print("\n Nodo 3 actualizando datos del curso")

        print("\n Nodo 4 integrando sistema P2P")

        print("\n Carga completada")
        print("")