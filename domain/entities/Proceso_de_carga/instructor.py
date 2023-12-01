class Instructor:
  def __init__(self, id:int, name:str,email:str, phone_number:int, banned:bool = False) -> None:
    self.id = id
    self.name = name
    self.email = email
    self.phone_number = phone_number
    self.courses = []
    self.banned = banned