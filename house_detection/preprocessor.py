# -*- coding: utf-8 -*-
import cv2
import numpy as np

class Preprocessor:
    """Prepare images to be used by network
    """
    def process(self, img,n_img=2):
        """Function to preprocess images

        Arguments:
            img {opencv img} -- image to be processed
            n_img {int} -- number of part by side  (default: {2})

        Returns:
            tuple -- (resize_factor(float),array of opencv images(np.array))
        """        
        img_gray = self._rgb2gray(img)
        factor, img_res = self._resize_img(img_gray)
        arr_img = self._crop_image(img_res, n_img)
        return (factor, arr_img)

    def _crop_image(self, img, n_img):
        """crop image
        
        Arguments:
            img {opencv img} -- image to be divide
            n_img {int} -- number of part by side
        
        Returns:
            np.array -- array of opencv images
        """
        h,w = img.shape
        h_w_size = int(h/n_img)
        w_w_size = int(w/n_img)

        
        array_img = np.zeros((n_img*n_img, h_w_size, w_w_size),dtype=np.uint8)
        #for i in range(0, n_img*n_img):
            #print(i*h_w_size,(i+1)*h_w_size, i*w_w_size,(i+1)*w_w_size)
            #array_img[i]=img[i*h_w_size:(i+1)*h_w_size, i*w_w_size:(i+1)*w_w_size]

        array_img[0] = img[:int(w/2), :int(h/2)]
        array_img[1] = img[:int(w/2), int(h/2):]

        array_img[2] = img[int(w/2):, :int(h/2)]
        array_img[3] = img[int(w/2):, int(h/2):]

        return array_img

    def _rgb2gray(self, img):
        """convert RGB images to gray scale
        
        Arguments:
            img {opencv img} -- RGB image to convert
        
        Returns:
            opencv img --  grayscale image 
        """
        if len(img.shape) > 2:
            return cv2.cvtColor(img, cv2.COLOR_RGB2GRAY)
        return img

    def _resize_img(self, img):
        """[summary]
        
        Arguments:
            img {opencv img} -- image to be resized (grayscale)
        
        Returns:
            tuple -- (resize_factor(float), img(opencv img))
        """
        resized_image = cv2.resize(img, (1024, 1024))
        hi,_ = img.shape
        hr,_ = resized_image.shape 
        return (float(hr)/float(hi), resized_image)






