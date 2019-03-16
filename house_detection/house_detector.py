# -*- coding: utf-8 -*-

from .postprocessor import Postprocessor
from .preprocessor import Preprocessor
from .network import Network

class House_detector():

    def __init__(self, network):

        self._pre = Preprocessor()
        self._post = Postprocessor()
        self._net = Network(network, 0.3)

    def detect (self, images):
        detections = []

        for i in images:
            f, imgs = self._pre.process(i)
            det = self._net.predict(imgs)
            houses = self._post.process(det, f)
            print(len(houses))
            img = self._post.mark_houses(i, houses)

            detections.append((len(houses), houses, img))

        return detections


