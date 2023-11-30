def get_id_new_subscriber(publisher):
    max_id = max(t[0] for t in publisher.subscribers) if publisher.subscribers else 0
    new_id = max_id + 1

    return new_id