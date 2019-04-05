
from flask import Flask, jsonify, request, abort
import cv2
import numpy as np
import base64

from house_detection.house_detector import House_detector
import tensorflow as tf

app = Flask(__name__)

dect = House_detector("model/aerial_model.h5")
graph = tf.get_default_graph()


def b64_to_img(b64):
    jpg_img = base64.b64decode(b64)
    return cv2.imdecode(np.frombuffer(jpg_img,dtype=np.int8),1)

def img_to_b64 (img):
    png_encoded_img = cv2.imencode('.jpg', img)
    return base64.b64encode(png_encoded_img[1]).decode('UTF-8')

@app.route('/api/detect', methods=['POST'])
def detect():
    if not request.json or not 'images' in request.json:
        abort(400)

    
    b64_images = request.get_json()['images']
    images = [b64_to_img(i) for i in b64_images]

    with graph.as_default():
        detections = dect.detect(images)
        result = []

        for d in detections:
            a={"total": d[0], "detections":d[1].tolist(), "image": img_to_b64(d[2])}
            result.append(a)
        

        return jsonify({'result': result}), 201

@app.route('/')
def index():
    return "Hello, World!"

if __name__ == '__main__':
    app.run(debug=True)