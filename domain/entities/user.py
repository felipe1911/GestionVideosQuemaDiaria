class User:
  def __init__(self,id:int, name:str,email:str, phone_number:int, goals) -> None:
    self.id = id
    self.name = name
    self.email = email
    self.goals = goals or []
    self.phone_number = phone_number
    self.subscriptions = []