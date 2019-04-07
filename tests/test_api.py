import unittest
import json

import server
import cv2
import base64

BASE_URL = 'http://127.0.0.1:5000/'
DETECT_URL= '{}/api/detect'.format(BASE_URL)



class TestApi(unittest.TestCase):

    def setUp(self):
        self.app = server.app.test_client()
        self.app.testing = True

    def test_get_index(self):
        response = self.app.get(BASE_URL)
        self.assertEqual(response.status_code, 200)

    def test_detect(self):
        img = cv2.imread('tests/data/austin35_1500.tif')
        png_encoded_img = cv2.imencode('.jpg', img)
        base64_encoded_img = base64.b64encode(png_encoded_img[1])
        message = {'images': [base64_encoded_img.decode('UTF-8')]}



        response = self.app.post(DETECT_URL, 
                                data=json.dumps(message),
                                content_type='application/json')
        data = json.loads(response.get_data())
        self.assertEqual(response.status_code, 201)
        self.assertEqual(data['result'][0]['total'], 1377)

    def test_bad_method(self):
        response = self.app.get(DETECT_URL)
        self.assertEqual(response.status_code, 405)
    
    def test_bad_data(self):
        response = self.app.post(DETECT_URL, 
                                data=json.dumps("hola"),
                                content_type='application/json')
        self.assertEqual(response.status_code, 400)

        response = self.app.post(DETECT_URL)
        self.assertEqual(response.status_code, 400)