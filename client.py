import cv2
import base64
import json
import http.client
import numpy as np


img = cv2.imread('tests/data/austin35_1500.tif')
png_encoded_img = cv2.imencode('.jpg', img)
base64_encoded_img = base64.b64encode(png_encoded_img[1])
message = {'images': [base64_encoded_img.decode('UTF-8')]}
json_message = json.dumps(message)

# Sending message
headers = {'Content-type': 'application/json'}
connection = http.client.HTTPConnection('127.0.0.1',port=5000)
connection.request('POST',
'/api/detect', json_message, headers)

# Decoding and save files
resp = connection.getresponse()
response = json.loads(resp.read().decode())


jpg_img = base64.b64decode(response["result"][0]["image"])
cv2.imwrite("resp.jpg", cv2.imdecode(np.frombuffer(jpg_img,dtype=np.int8),1))



