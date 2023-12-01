from contenido import Contenido
from factory_subscriber import FactorySubscriber
from add_subscriber import add_subscriber_to_publisher

class Publisher:
    def __init__(self, course):
        self.subscribers = []
        self.course = course


    def subscribe(self, user_new_susbscriber, type_subscriber) -> None:
        new_susbscriber = FactorySubscriber.create_subscriber(self,user_new_susbscriber,type_subscriber)
        id_new_subscriber = new_susbscriber.id_subscriber
        add_subscriber_to_publisher(self,id_new_subscriber,new_susbscriber)

    def notify_users(self):
        print(self.subscribers)
        for subscriber_pair in self.subscribers:
            subscriber = subscriber_pair[1]
            subscriber.update()