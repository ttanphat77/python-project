import argparse
import cv2
import random
from flask import Blueprint, request
import numpy
import base64

cat_detector_bp = Blueprint('cat_detector', __name__)


@cat_detector_bp.route('/detect/', methods=['POST'])
def detect_cat():
    img = cv2.imdecode(numpy.fromstring(request.files['file'].read(), numpy.uint8), cv2.IMREAD_UNCHANGED)
    gray_img = cv2.cvtColor(img, cv2.COLOR_BGR2GRAY)

    detector = cv2.CascadeClassifier('visionary.net_cat_cascade_web_LBP.xml')

    rects = detector.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=7, minSize=(50, 50))

    for (i, (x, y, w, h)) in enumerate(rects):
        color = random_color()
        cv2.rectangle(img, (x, y), (x + w, y + h), color, 2)
        # cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2)

    retval, buffer_img = cv2.imencode('.jpg', img)
    data = base64.b64encode(buffer_img)
    return data


def random_color():
    rgbl = [255, 0, 0]
    random.shuffle(rgbl)
    return tuple(rgbl)

# ap = argparse.ArgumentParser()
# ap.add_argument("-i", "--image", required=True, help="path to the input image")
# ap.add_argument("-c", "--cascade",
#                 default="visionary.net_cat_cascade_web_LBP.xml",
#                 help="part to cat Detector haar cascade")

# args = vars(ap.parse_args())

# load image and grayscale
# image = cv2.imread(args["image"])
# gray_img = cv2.cvtColor(image, cv2.COLOR_BGR2GRAY)

# load haar cascade
# detector = cv2.CascadeClassifier(args["cascade"])

# detect cat face
# rects = detector.detectMultiScale(gray_img, scaleFactor=1.1, minNeighbors=7, minSize=(50, 50))

# draw bounding box
# for (i, (x, y, w, h)) in enumerate(rects):
#     color = random_color()
#     cv2.rectangle(image, (x, y), (x + w, y + h), color, 2)
# cv2.putText(image, "Cat #{}".format(i + 1), (x, y - 10), cv2.FONT_HERSHEY_SIMPLEX, 0.55, color, 2)
