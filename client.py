import cv2
import json
import http.client
import argparse
import sys
from glob import glob

from image_utils import *

def read_images(folder):
    """loads images from folder
        
        Parameters
        ----------
        folder : string
            path of folder images
        
        Returns
        -------
        list of opencv images
        """
    images = []
    for infile in glob(folder + "/*"):
        image = cv2.imread(infile)

        images.append(image)
    return images

def send_images(server, port, b64_images):
    """sends Base 64 image list
        
        Parameters
        ----------
        server : string
            server's url

        port : int
            server's port

        bs64_images:
            list of images in b64 format
        
        Returns
        -------
        Response of http request
        """
    message = {'images': b64_images}
    json_message = json.dumps(message)

    headers = {'Content-type': 'application/json'}
    connection = http.client.HTTPConnection(server,port=port)
    connection.request('POST','/api/detect', json_message, headers)

    return connection.getresponse()


def main(args):
    """main function
        
        Parameters
        ----------
        args : dict
            arguments
        """

    server = args["server"]
    port = args["port"]
    dirin = args["in"]
    out = args["out"]

    # Read and encode images
    images = read_images(dirin)
    b64_images = [img_to_b64(i) for i in images]

    # send images
    resp = send_images(server, port, b64_images)

    # decode and save response
    response = json.loads(resp.read().decode())

    with open(out , 'w') as f:
        json.dump(response["result"], f)



if __name__ == '__main__' :

    ap = argparse.ArgumentParser()
    ap.add_argument("-i", "--in", required=True, help="folder with in images")
    ap.add_argument("-o", "--out", required=True, help="output json file")
    ap.add_argument("-s", "--server", required=False, default = "localhost", help="server's url (default: localhost)")
    ap.add_argument("-p", "--port", required=False, type=int, default=5000, help="server's port (default: 5000)")
    args = vars(ap.parse_args())
    main(args)

