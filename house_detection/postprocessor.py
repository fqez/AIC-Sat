# -*- coding: utf-8 -*-
import numpy as np
import cv2

class Postprocessor():

    """postprocess and analyze network output
    """

    def _recompose_image(self, images):
        """recomponse network output as a only image
        
        Parameters
        ----------
        images : numpy array
            arry of image's parts
        
        Returns
        -------
        numpy array
            image in grayscale
        """

        n, h, w = images.shape

        img = np.zeros((h*2, w*2),dtype=np.uint8)

        img[:int(w), :int(h)] = images[0]
        img[:int(w), int(h):] = images[1]

        img[int(w):, :int(h)] = images[2]
        img[int(w):, int(h):] = images[3]

        return img

    def _rescalate_houses_dims(self, houses, f):
        """Rescale bounding boxes using the factor d
        
        Parameters
        ----------
        houses : numpy array
            bounding boxes of houses (x,y,h,w)
        f : float
            factor to scale
        
        Returns
        -------
        numpy array
            bounding boxes of houses (x,y,h,w)
        """

        houses_res = houses/f

        return houses_res.astype(np.int)

    def _find_houses(self, image):
        """localize houses in the image
        
        Parameters
        ----------
        image : numpy array
            grayscale image
        
        Returns
        -------
        numpy array
            bounding boxes of houses (x,y,h,w)
        """

        cnts = cv2.findContours(image, cv2.RETR_EXTERNAL, cv2.CHAIN_APPROX_SIMPLE)[-2]

        rects = []
        for c in cnts:
            rects.append(cv2.boundingRect(c))

        return np.array(rects, dtype=np.int)


    def process(self, images, factor):
        """postprocess network output
        
        Parameters
        ----------
        images : numpy array
            arry of image's parts
        factor : float
            factor to scale
        
        Returns
        -------
        numpy array
            bounding boxes of houses (x,y,h,w)
        """

        image = self._recompose_image(images)

        houses = self._find_houses(image)

        return self._rescalate_houses_dims(houses, factor)

    def mark_houses(self, img, houses):
        """draw bounding boxes in a copy of the image
        
        Parameters
        ----------
        img : numpy array
            image to put the boundong boxes
        houses : numpy array
            bounding boxes of houses (x,y,h,w)
        
        Returns
        -------
        numpy array
            image with bounding boxes
        """""
        img_cp = img.copy()

        for x,y,h,w in houses:
            cv2.rectangle(img_cp,(x,y),(x+w,y+h),(0,255,0),1)

        return img_cp

