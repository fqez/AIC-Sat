# -*- coding: utf-8 -*-
import unittest
import cv2
import numpy as np

from house_detection.preprocessor import Preprocessor

class TestPreprocessor (unittest.TestCase):
    def __init__(self, *args, **kwargs):
        super(TestPreprocessor, self).__init__(*args, **kwargs)
        self.proc = Preprocessor()

    def test_img2gray(self):
        
        img = cv2.imread("tests/data/austin35_1500.tif")
        rgb_img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)
        gray_img = self.proc._rgb2gray(rgb_img)

        #cv2.imwrite("tests/data/austin35_1500_gray.tif", gray_img)
        img2 = cv2.imread("tests/data/austin35_1500_gray.tif",cv2.IMREAD_GRAYSCALE)
        self.assertTrue(np.array_equal(img2, gray_img))

        

    def test_crop_image(self):

        img = cv2.imread("tests/data/austin35_1024.tif",cv2.IMREAD_GRAYSCALE)

        im1 = cv2.imread("tests/data/austin35_1024_1.tif", cv2.IMREAD_GRAYSCALE)
        im2 = cv2.imread("tests/data/austin35_1024_2.tif", cv2.IMREAD_GRAYSCALE)
        im3 = cv2.imread("tests/data/austin35_1024_3.tif", cv2.IMREAD_GRAYSCALE)
        im4 = cv2.imread("tests/data/austin35_1024_4.tif", cv2.IMREAD_GRAYSCALE)

        im_arr = [im1, im2, im3, im4]

        arr_img = self.proc._crop_image(img, 2)

        #cv2.imwrite("tests/data/austin35_1024_1.tif", arr_img[0])
        #cv2.imwrite("tests/data/austin35_1024_2.tif", arr_img[1])
        #cv2.imwrite("tests/data/austin35_1024_3.tif", arr_img[2])
        #cv2.imwrite("tests/data/austin35_1024_4.tif", arr_img[3])

        for i in range(len(im_arr)):
            self.assertTrue(np.array_equal(np.asarray(im_arr[i]), np.asarray(arr_img[i])))
        

    def test_resize_img(self):
        img = cv2.imread("tests/data/austin35_1500_gray.tif",cv2.IMREAD_GRAYSCALE)
        img2 = cv2.imread("tests/data/austin35_1024.tif",cv2.IMREAD_GRAYSCALE)
        f = 1024./1500.
        fc, img_res = self.proc._resize_img(img)
        #cv2.imwrite("tests/data/austin35_1024.tif", img_res)
        self.assertTrue(np.array_equal(img2, img_res))
        self.assertEqual(fc, f)

        
        
    def test_process(self):
        img = cv2.imread("tests/data/austin35_1500.tif",cv2.IMREAD_GRAYSCALE)

        im1 = cv2.imread("tests/data/austin35_1024_1.tif", cv2.IMREAD_GRAYSCALE)
        im2 = cv2.imread("tests/data/austin35_1024_2.tif", cv2.IMREAD_GRAYSCALE)
        im3 = cv2.imread("tests/data/austin35_1024_3.tif", cv2.IMREAD_GRAYSCALE)
        im4 = cv2.imread("tests/data/austin35_1024_4.tif", cv2.IMREAD_GRAYSCALE)

        im_arr = np.array([im1, im2, im3, im4])
        f = 1024./1500.
        fc, arr_img = self.proc.process(img)
        self.assertEqual(fc, f)
        for i in range(len(im_arr)):
            self.assertTrue(np.array_equal(im_arr[i], arr_img[i]))


if __name__ == '__main__':
    unittest.main()