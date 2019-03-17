# -*- coding: utf-8 -*-
import unittest
import cv2
import numpy as np

from house_detection.postprocessor import Postprocessor

class TestPostprocessor (unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPostprocessor, self).__init__(*args, **kwargs)
        self.proc = Postprocessor()

    def test_recompose_image(self):
        img1 = cv2.imread("tests/data/austin35_pred_1.tif", cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread("tests/data/austin35_pred_2.tif", cv2.IMREAD_GRAYSCALE)
        img3 = cv2.imread("tests/data/austin35_pred_3.tif", cv2.IMREAD_GRAYSCALE)
        img4 = cv2.imread("tests/data/austin35_pred_4.tif",  cv2.IMREAD_GRAYSCALE)

        img_arr = np.array([img1, img2, img3, img4])

        img_res = self.proc._recompose_image(img_arr)

        img = cv2.imread("tests/data/austin35_1024_bw.tif", cv2.IMREAD_GRAYSCALE)

        self.assertTrue(np.array_equal(img_res, img))

    def test_find_houses(self):

        img = cv2.imread("tests/data/austin35_1024_bw.tif", cv2.IMREAD_GRAYSCALE)

        houses = self.proc._find_houses(img)
        houses_save = np.load("tests/data/austin35_houses_1024.npy")
        self.assertTrue(np.array_equal(houses, houses_save))

    def test_rescalate_houses_dims(self):

        houses_1024 = np.load("tests/data/austin35_houses_1024.npy")

        houses = self.proc._rescalate_houses_dims(houses_1024, 1024./1500.)
        houses_1500 = np.load("tests/data/austin35_houses_1500.npy")
        
        self.assertTrue(np.array_equal(houses, houses_1500))


    def test_process(self):
        img1 = cv2.imread("tests/data/austin35_pred_1.tif", cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread("tests/data/austin35_pred_2.tif", cv2.IMREAD_GRAYSCALE)
        img3 = cv2.imread("tests/data/austin35_pred_3.tif", cv2.IMREAD_GRAYSCALE)
        img4 = cv2.imread("tests/data/austin35_pred_4.tif",  cv2.IMREAD_GRAYSCALE)

        img_arr = np.array([img1, img2, img3, img4])

        houses = self.proc.process(img_arr, 1024./1500.)

        houses_1500 = np.load("tests/data/austin35_houses_1500.npy")

        self.assertTrue(np.array_equal(houses, houses_1500))


    def test_mark_houses(self):

        img = cv2.imread("tests/data/austin35_1500.tif")

        houses_1500 = np.load("tests/data/austin35_houses_1500.npy")

        img_mark =  self.proc.mark_houses(img, houses_1500)


        img2 = cv2.imread("tests/data/austin35_1500_marks.tif")

        self.assertTrue(np.array_equal(img_mark, img2))


        




if __name__ == '__main__':
    unittest.main()