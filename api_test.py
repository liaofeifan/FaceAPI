import requests
from PIL import Image

import requests
url = 'http://127.0.0.1:5000/api/face_comparison'
# source_img = Image.open('/Users/FiveSheep/项目/链盾/dataset/face_recognition/asian/multi/000/000_2.bmp')
# img = Image.open('/Users/FiveSheep/项目/链盾/dataset/face_recognition/asian/multi/000/000_1.bmp')
files={'source_img': open('./img/000_0.bmp', 'rb'), 'img': open('./img/001_0.bmp', 'rb')}

r=requests.post(url,files=files)

print(r.text)

# url = 'http://127.0.0.1:5000/api/face_detection'
# # source_img = Image.open('/Users/FiveSheep/项目/链盾/dataset/face_recognition/asian/multi/000/000_2.bmp')
# # img = Image.open('/Users/FiveSheep/项目/链盾/dataset/face_recognition/asian/multi/000/000_1.bmp')
# files = {'img': open('/media/fivesheep/TransFer/CASIA-FaceV5/CASIA-FaceV5/000/000_1.bmp', 'rb')}
#
# r = requests.post(url,files=files)
#
# print(r.text)
