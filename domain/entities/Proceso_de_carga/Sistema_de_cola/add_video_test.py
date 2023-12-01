from add_video_set import add_video_set
from video import Video
from instructor import Instructor

instructor1 = Instructor(1, 'Ana','ana@gmail.com', '123456789')
banned_instructor = Instructor(2, 'Luna', 'luna@gmail.com','19083291',True)

video1 =  Video(1,'video1', ['A','B','C'], instructor1, 'url1', 1)
video2 =  Video(2,'video2', ['D','E','F'], instructor1, 'url12', 2)
video3 =  Video(3,'video3', ['G','H','I'], instructor1, 'url123', 3)
video4 =  Video(4,'video4', ['J','K','L'], instructor1, '123456789012345678901234567890123456789012345678901234567891234567890', 4)
video5 =  Video(5,'video5', ['M','N','O'], instructor1, 'url12345', 3000)

video6 =  Video(1,'video1', ['A','B','C'], banned_instructor, 'url1', 1)
video7 =  Video(2,'video2', ['D','E','F'], banned_instructor, 'url12', 2)

set1 = [video6,video7]
set2 = [video5,video4,video3,video2,video1]

add_video_set(set1,banned_instructor)
add_video_set(set2,instructor1)