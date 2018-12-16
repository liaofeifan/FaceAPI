import face_recognition
import json
from flask import Flask
from flask import request

# self-written functions
from func import get_face

app = Flask(__name__)

# api activity test


@app.route('/', methods=['GET'])
def hello():
    return "Halo, the API is alive!"

@app.route('/face', methods=['GET'])
def face():
    return "Halo, this is face api!"

# verify if there is any human face in the picture
# params
# <img>: image to verify


@app.route('/api/face_detection', methods=['POST'])
def face_detect():
    #initialize api message
    api_msg = {
        "status": -1,
        "data": {},
        "msg": ""
    }
    if request.method == 'POST':
        # get image file in request data
        img_file = request.files['img']

        face = get_face(img_file)

        if len(face) != 1:
            api_msg["msg"] = "No human face or multi human faces in the image"
        else:
            api_msg["status"] = 0
            api_msg["data"] = {"result": 1}
            api_msg["msg"] = "1 human face detected"

        return json.dumps(api_msg)

#

# verify if persons provided are the same one
# params
# <source_img>: face image stored in the block chain
# <img>: current face image to verify


@app.route('/api/face_comparison', methods=['POST'])
def face_compare():
    # initialize api message
    api_msg = {
        "status": -1,
        "data": {},
        "msg": ""
    }
    if request.method == 'POST':
        source_img_file = request.files['source_img']
        img_file = request.files['img']

        source_face = get_face(source_img_file)

        # detect if there is only one face in source image
        if len(source_face) != 1:
            api_msg["msg"] = "No human face or multi human faces in source image"
            return json.dumps(api_msg)
        else:
            source_face = source_face[0]

        # get source face encodings list
        source_encodings = [
            source_face
        ]

        face = get_face(img_file)

        # detect if there is only one face in source image
        if len(face) != 1:
            api_msg["status"] = -1
            api_msg["msg"] = "no human face or multi human faces in target image"
            return json.dumps(api_msg)
        else:
            encoding = face[0]

        # compute the face distance between source & target face
        face_distances = face_recognition.face_distance(source_encodings, encoding)

        # set the tolerance to 0.4 and test if the verification passes

        is_passed = False
        for i, face_distance in enumerate(face_distances):
            if face_distance <= 0.4:
                is_passed = True

        # set the api message

        if is_passed:
            api_msg["status"] = 0
            api_msg["data"] = {"result": 1}
            api_msg["msg"] = "face verification passed"
        else:
            api_msg["status"] = 0
            api_msg["data"] = {"result": 0}
            api_msg["msg"] = "face verification failed"

        return json.dumps(api_msg)


if __name__ == '__main__':
    app.run()
