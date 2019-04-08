import cv2
import base64
import numpy as np


def imgs_are_equal(img1, img2):
    """Compare 2 images
        
        Parameters
        ----------
        img1 : opencv Color Image
            first image to compare

        img2 : opencv Color Image
            second image to compare
        
        Returns
        -------
        Boolean
        """
    if img1.shape == img2.shape:
        difference = cv2.subtract(img1, img2)
        if len(difference.shape) > 2:
            b, g, r = cv2.split(difference)
            return cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0
        else :
            return cv2.countNonZero(difference) == 0
    return False

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
    if "," in b64:
        base64_file = b64.partition(",")[-1]
    else: 
        base64_file = b64

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
