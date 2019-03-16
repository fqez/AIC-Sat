# -*- coding: utf-8 -*-
import unittest
import cv2
import numpy as np

from house_detection.utils import imgs_are_equal

from house_detection.house_detector import House_detector

class Testhouse_detector (unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(Testhouse_detector, self).__init__(*args, **kwargs)
        self.dect = House_detector("model/aerial_model.h5")

    def test_detect(self):
        img = cv2.imread("tests/data/austin35_1500.tif")
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        res = self.dect.detect([rgb_img])

        res_0 = res[0]

        houses_1500 = np.load("tests/data/austin35_houses_1500.npy")

        img_marks = cv2.imread("tests/data/austin35_1500_marks.tif")

        print (res_0[0], len(houses_1500))

        self.assertTrue(np.array_equal(img_marks, res_0[2]))
        self.assertTrue(np.array_equal(houses_1500, res_0[1]))
        self.assertTrue(np.array_equal(len(houses_1500), res_0[0]))


if __name__ == '__main__':
    unittest.main()