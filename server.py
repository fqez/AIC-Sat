
from flask import Flask, jsonify, request, abort, render_template
import cv2

from house_detection.house_detector import House_detector
import tensorflow as tf
from image_utils import *
import argparse

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
    images = [b64_to_img(i) for i in b64_images]

    cv2.imwrite("test.png", images[0])
    #print(b64_images[0])

    with graph.as_default():
        detections = dect.detect(images)
        result = []

        for d in detections:
            
            a={"total": d[0], "detections":d[1].tolist(), "image": img_to_b64(d[2])}
            result.append(a)
        
        return jsonify({'result': result}), 201

@app.route('/')
def index():
    """Handler for index
        
        Returns
        -------
        html client for API
        """
    return render_template("index.html", url=request.url)


def main(args):
    """main function
        
        Parameters
        ----------
        args : dict
            arguments
        """

    host = args["host"]
    port = args["port"]
    debug = args["debug"]

    app.run(host=host,port=port, debug=debug)

if __name__ == '__main__':
    ap = argparse.ArgumentParser()
    ap.add_argument("-s", "--host", required=False, default = "127.0.0.1", help="host (default: 127.0.0.1)")
    ap.add_argument("-p", "--port", required=False, type=int, default = 5000, help="port (default: 5000)")
    ap.add_argument("-d", "--debug", required=False, action="store_true", default=False, help="Activate debug mode")

    args = vars(ap.parse_args())

    main(args)