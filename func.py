from PIL import Image
import face_recognition
import numpy as np


def load_image(im, mode='RGB'):
    if mode:
        im = im.convert(mode)
    return np.array(im)


def get_rotated_encoding(im, degree=0):
    encoding = None
    if not degree:
        im = load_image(im)
        encoding = face_recognition.face_encodings(im)
    elif degree == 90:
        im = im.transpose(Image.ROTATE_90)
        im = load_image(im)
        encoding = face_recognition.face_encodings(im)
    elif degree == 180:
        im = im.transpose(Image.ROTATE_180)
        im = load_image(im)
        encoding = face_recognition.face_encodings(im)
    elif degree == 270:
        im = im.transpose(Image.ROTATE_270)
        im = load_image(im)
        encoding = face_recognition.face_encodings(im)
    return encoding


def get_face(img_file):
    im = Image.open(img_file)
    length = im.size[0]
    width = im.size[1]

    if length <= width:
        # normal or upside-down portrait
        encoding = get_rotated_encoding(im)
        if not len(encoding):
            encoding = get_rotated_encoding(im, 180)
        return encoding
    else:
        # rotated portrait
        # rotate 90 or 270
        encoding = get_rotated_encoding(im, 90)
        if not len(encoding):
            encoding = get_rotated_encoding(im, 270)
        return encoding
