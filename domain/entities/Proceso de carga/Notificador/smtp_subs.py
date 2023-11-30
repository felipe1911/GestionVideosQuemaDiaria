from subscriber import Subscriber

class SMTP_subs:
    def __init__(self, id_subscriber, user) -> None:
        self.id_subscriber = id_subscriber
        self.user = user

    def __repr__(self) -> str:
        return (self.user.name)

    def __str__(self) -> str:
        return (self.user.name)

        
    def update(self):
        print(f'Correo electrónico enviado a {self.user.email}')
