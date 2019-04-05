import cv2
import base64
import json
import http.client
# Cargamos una imagen, luego va a base64, a un mapa y a un JSON
img = cv2.imread('tests/data/austin35_1500.tif')
png_encoded_img = cv2.imencode('.jpg', img)
base64_encoded_img = base64.b64encode(png_encoded_img[1])
message = {'images': [base64_encoded_img.decode('UTF-8')]}
json_message = json.dumps(message)
# Creamos conexión, cabecera y enviamos el mensaje con un POST
headers = {'Content-type': 'application/json'}
connection = http.client.HTTPConnection('127.0.0.1',port=5000)

connection.request('POST',
'/api/detect', json_message, headers)
# Esperamos la respuesta y la pintamos por pantalla
resp = connection.getresponse()
print(resp.read().decode())