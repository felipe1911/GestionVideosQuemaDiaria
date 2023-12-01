from .upload_manager import UploadManager

def get_videos_info_to_send_to_P2P(videos, error_list):
    videos_info = []
    for i in range(len(error_list)):
        manager = UploadManager(videos[i],error_list[i])
        manager.setUploadStrategy()
        if manager.executeUpload != None:
            videos_info.append(manager.executeUpload())
    return videos_info