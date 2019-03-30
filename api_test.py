import requests
from PIL import Image

import requests
import base64
from PIL import Image

# choose self-defined post method
method = 4

if method == 1:
    # Detection - File method

    url = 'http://127.0.0.1:5000/api/face_detection'
    files = {'img': open('/home/fivesheep/文档/链盾项目/face_recognition/examples/biden.jpg', 'rb')}
    r = requests.post(url, files=files)
    print(r.text)

elif method == 2:
    # Detection - Base64 method

    url = 'http://127.0.0.1:5000/api/face_detection'
    encoded_image = base64.b64encode(open('/home/fivesheep/文档/链盾项目/face_recognition/examples/biden.jpg', 'rb').read())
    img_str = bytes.decode(encoded_image)
    r = requests.post(url, json={'img': img_str})
    print(r.text)

elif method == 3:
    # Comparison - File method

    url = 'http://127.0.0.1:5000/api/face_comparison'
    files = {'source_img': open('/home/fivesheep/文档/链盾项目/face_recognition/examples/biden.jpg', 'rb'), 'img': open('/home/fivesheep/文档/链盾项目/face_recognition/examples/biden.jpg', 'rb')}
    r = requests.post(url,files=files)
    print(r.text)

elif method == 4:
    # Comparison - Base64 method

    url = 'http://127.0.0.1:5000/api/face_comparison'
    # get source image base64 string
    encoded_source_img = base64.b64encode(open('/home/fivesheep/文档/链盾项目/face_recognition/examples/biden.jpg', 'rb').read())
    source_img_str = bytes.decode(encoded_source_img)

    # get image base64 string
    encoded_img = base64.b64encode(
        open('/home/fivesheep/文档/链盾项目/face_recognition/examples/biden.jpg', 'rb').read())
    img_str = bytes.decode(encoded_img)

    r = requests.post(url, json={'img': img_str, 'source_img': source_img_str})
    print(r.text)
