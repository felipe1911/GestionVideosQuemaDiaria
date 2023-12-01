from abc import ABC, abstractmethod

class Subscriber(ABC):
  def __init__(self,id_subscriber, user):
    pass
  
  @abstractmethod
  def update():
    pass
