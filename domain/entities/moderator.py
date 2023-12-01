from .Aprobar_videos.check_and_approve_videos_command import CheckAndApproveVideosCommand

class Moderator:
  def _init_(self, id:int, name:str, email:str) -> None:
    self.id = id
    self.name = name
    self.email = email

    
  def check_and_approve_videos(self, json_data):
    check_approve_command = CheckAndApproveVideosCommand(json_data)
    check_approve_command.execute()