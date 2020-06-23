from selenium import webdriver
import time
from start.Utils import read_txt_name, screen_img, create_file

# driver = webdriver.Chrome()
videoListPath = './video.txt'
save_img_path = '/Users/fiona/Desktop/image'
# read urlList from video.txt
urlList = read_txt_name(videoListPath)

for url in urlList:
    video_id = url[31:43]
    print(video_id)
    newDir = img_name = save_img_path + "/" + video_id + "/"
    create_file(newDir)
    screen_img(url, newDir)

