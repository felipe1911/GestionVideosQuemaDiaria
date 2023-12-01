from subscriber import Subscriber

class WS_subs:
    def __init__(self, id_subscriber, user) -> None:
        self.id_subscriber = id_subscriber
        self.user = user

    def __repr__(self) -> str:
        return (self.user.name)

    def __str__(self) -> str:
        return (self.user.name)

    def update(self):
        print(f'Notificación Web enviada a {self.user.name}')
