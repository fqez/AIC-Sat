
from flask import Flask, jsonify, request, abort, render_template
import cv2
import numpy as np
import base64

from house_detection.house_detector import House_detector
import tensorflow as tf

app = Flask(__name__)

dect = House_detector() # Detector
graph = tf.get_default_graph() # Necessary to use predict in threads



"""
=================
API DOCUMENTATION
=================
------------------------------------------------------------------------------------------------------------------------------------------------------------
| FUNCTION  |METHOD|T IN|               FORMAT IN                   |T OUT|                                   FORMAT OUT                                   |
------------------------------------------------------------------------------------------------------------------------------------------------------------
|/api/detect| POST |json|{"images":[img1(base64), img2(base64),...]}|json |{result:[{total:n_houses(int), detections:[detections], image: img(base64)},..]}|
------------------------------------------------------------------------------------------------------------------------------------------------------------

"""

def b64_to_img(b64):
    """Conversor from base64 to opencv image
        
        Parameters
        ----------
        b64 : string
            image in base64
        
        Returns
        -------
        opencv image (numpy array)
        """
    base64_file = b64.partition(",")[-1]
    print(base64_file[:50])
    #while(len(b64)%4 !=0):
    #    base64_file += "="
    #print(base64_file[:50])
    jpg_img = base64.b64decode(base64_file)
    return cv2.imdecode(np.frombuffer(jpg_img,dtype=np.int8),1)

def img_to_b64 (img):
    """Conversor from opencv image to base64
        
        Parameters
        ----------
        img : numpy array
            opencv image
        
        Returns
        -------
        image in base64 (string, UTF-8)
        """
    png_encoded_img = cv2.imencode('.jpg', img)
    return base64.b64encode(png_encoded_img[1]).decode('UTF-8')

@app.route('/api/detect', methods=['POST'])
def detect():
    """Handler for detect method of API
        
        Returns
        -------
        json with result of detections
        """

    if not request.json or not 'images' in request.json:
        abort(400)

    
    b64_images = request.get_json()['images']
    print("00000")
    images = [b64_to_img(i) for i in b64_images]
    print("00001")

    cv2.imwrite("test.png", images[0])
    print("00003")
    #print(b64_images[0])

    with graph.as_default():
        detections = dect.detect(images)
        print("1")
        result = []

        for d in detections:
            
            a={"total": d[0], "detections":d[1].tolist(), "image": img_to_b64(d[2])}
            result.append(a)
        
        print("2")
        return jsonify({'result': result}), 201

@app.route('/')
def index():
    """Handler for index
        
        Returns
        -------
        html client for API
        """
    return render_template("index.html", url=request.url)

if __name__ == '__main__':
    
    app.run(debug=True)