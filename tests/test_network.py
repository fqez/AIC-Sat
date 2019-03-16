# -*- coding: utf-8 -*-
import unittest
import cv2
import numpy as np

from house_detection.network import Network

class TestNetwork (unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestNetwork, self).__init__(*args, **kwargs)
        self.net = Network("model/aerial_model.h5")



    def test_predict(self):

        im1 = cv2.imread("tests/data/austin35_1024_1.tif", cv2.IMREAD_GRAYSCALE)
        im2 = cv2.imread("tests/data/austin35_1024_2.tif", cv2.IMREAD_GRAYSCALE)
        im3 = cv2.imread("tests/data/austin35_1024_3.tif", cv2.IMREAD_GRAYSCALE)
        im4 = cv2.imread("tests/data/austin35_1024_4.tif", cv2.IMREAD_GRAYSCALE)

        im_arr = np.array([im1, im2, im3, im4])

        prediction = self.net.predict(im_arr)
        res1 = cv2.imread("tests/data/austin35_pred_1.tif", cv2.IMREAD_GRAYSCALE)
        res2 = cv2.imread("tests/data/austin35_pred_2.tif", cv2.IMREAD_GRAYSCALE)
        res3 = cv2.imread("tests/data/austin35_pred_3.tif", cv2.IMREAD_GRAYSCALE)
        res4 = cv2.imread("tests/data/austin35_pred_4.tif",  cv2.IMREAD_GRAYSCALE)

        res_arr = np.array([res1, res2, res3, res4])

        for i in range(len(res_arr)):
            self.assertTrue(np.array_equal(res_arr[i], prediction[i]))




if __name__ == '__main__':
    unittest.main()
        