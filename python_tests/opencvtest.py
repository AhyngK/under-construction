import cv2
import os

videoname = 'Coldplay - Viva la Vida (Lyrics)'
filepath = 'C:\\Users\\SSAFY\\Desktop\\lyrics_video\\Coldplay - Viva la Vida (Lyrics).mp4'
video = cv2.VideoCapture(filepath)

if not video.isOpened():
    print("Error: opening video stream or file:",filepath)
    exit(0)

length = int(video.get(cv2.CAP_PROP_FRAME_COUNT))
width = int(video.get(cv2.CAP_PROP_FRAME_WIDTH))
height = int(video.get(cv2.CAP_PROP_FRAME_HEIGHT))
fps = 60

frame_interval = int(fps * 0.2)

save_path = 'C:\\Users\\SSAFY\\Desktop\\frames'

try:
    if not os.path.exists(save_path+'\\'+videoname):
        os.makedirs(save_path+'\\'+videoname)
except OSError:
    print("Error: Creation of the directory")

count = 0
frame_count = 0
while True:
    ret, image = video.read()
    if not ret:
        break
    if frame_count % frame_interval == 0:
        cv2.imwrite(os.path.join(save_path, videoname, f"frame{count}.jpg"), image)
        count += 1
    frame_count += 1

video.release()
print("Done: Frame Extraction Complete")

