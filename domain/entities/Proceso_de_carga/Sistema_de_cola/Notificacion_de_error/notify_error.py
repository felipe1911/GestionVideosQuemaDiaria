def notify_error(error_id,video):
    if error_id == 0:
        print(video.title,': No presenta errores ni excepciones')
    elif error_id == 1:
        print(video.title,': No puede subir este video porque el tamaño es demasiado grande para la carga')
    elif error_id == 2:
        print(video.title, ': No puede subir este video porque usted está restringido')
    elif error_id == 3:
        print(video.title, ': No puede subir este video porque tiene una duración mayor a 45 minutos')