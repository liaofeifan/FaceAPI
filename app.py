import face_recognition
import json
from flask import Flask
from flask import request
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

        img = face_recognition.load_image_file(img_file)
        encoding = face_recognition.face_encodings(img)

        if len(encoding) != 1:
            api_msg["msg"] = "no human face or multi human faces in the image"
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

        source_img = face_recognition.load_image_file(source_img_file)
        source_encoding = face_recognition.face_encodings(source_img)

        # detect if there is only one face in source image
        if len(source_encoding) != 1:
            api_msg["msg"] = "no human face or multi human faces in source image"

            return json.dumps(api_msg)
        else:
            source_encoding = source_encoding[0]

        # get source face encodings list
        source_encodings = [
            source_encoding
        ]

        img = face_recognition.load_image_file(img_file)
        encoding = face_recognition.face_encodings(img)

        # detect if there is only one face in source image
        if len(encoding) != 1:
            api_msg["status"] = -1
            api_msg["msg"] = "no human face or multi human faces in target image"
        else:
            encoding = encoding[0]

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
