from add_video_set import add_video_set
from video import Video

video1 =  Video(1,'video1', ['A','B','C'], 'Luna', 'url1', 1)
video2 =  Video(2,'video2', ['D','E','F'], 'Ana', 'url12', 2)
video3 =  Video(3,'video3', ['G','H','I'], 'Felipe', 'url123', 3)
video4 =  Video(4,'video4', ['J','K','L'], 'Luna', 'url1234', 4)
video5 =  Video(5,'video5', ['M','N','O'], 'Felipe', 'url12345', 5)

set1 = [video4,video1]
set2 = [video1, video3, video5]
set3 = [video5,video4,video3,video2,video1]

add_video_set(set1)
add_video_set(set2)
add_video_set(set3)