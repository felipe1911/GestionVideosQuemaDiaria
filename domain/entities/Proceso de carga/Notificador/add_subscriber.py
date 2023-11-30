


def add_subscriber_to_publisher(publisher,id_subscriber,subscriber):
    publisher.subscribers.append((id_subscriber,subscriber))

    print(f'Usuario {subscriber.user.name} suscrito a {publisher.course.title}')