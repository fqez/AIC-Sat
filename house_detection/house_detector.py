# -*- coding: utf-8 -*-

from .postprocessor import Postprocessor
from .preprocessor import Preprocessor
from .network import Network

class House_detector():
    """House detector using keras network

    Attributes
    ----------
    _pre : Preprocessor
        Function to preprocess images
    _net : Network
        neural network
    _post: Postprocessor
        Function to postprocess images

    """

    def __init__(self, network):
        """inicialize house detector
        
        Parameters
        ----------
        network : str  
            path to network file
        
        """

        self._pre = Preprocessor()
        self._post = Postprocessor()
        self._net = Network(network, 0.3)

    def detect (self, images):
        """Detector of houses in images
        
        Parameters
        ----------
        images : numpy array
            array of images
        
        Returns
        -------
        list
            list of detections (n_houses, bounding_boxes, image with bounding boxes)
        """
        detections = []

        for i in images:
            f, imgs = self._pre.process(i)
            det = self._net.predict(imgs)
            houses = self._post.process(det, f)
            img = self._post.mark_houses(i, houses)

            detections.append((len(houses), houses, img))

        return detections


