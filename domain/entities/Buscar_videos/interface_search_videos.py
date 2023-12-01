from .search_by_description import search_by_description
from .search_by_tags import search_by_tags

def interface_search_videos(user):
    print('\nBienvenido al portal de búsqueda\n')
    while True:
        selected_query_option = input('\n1. Búsqueda por descripción \n2. Búsqueda por etiquetas \n3. Salir \n  ¿Qué desea hacer?: ')
        if selected_query_option == '1':
            query_description = input('\nIngrese su búsqueda: ')
            search_by_description(query_description)
        if selected_query_option == '2':
            query_tags = input('\nIngrese las etiquetas (separadas por comas sin espacios): ').split(',')
            search_by_tags(query_tags)
        if selected_query_option ==  '3':
            break

        

