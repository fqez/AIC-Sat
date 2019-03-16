# -*- coding: utf-8 -*-

from keras.models import load_model
import numpy as np
import matplotlib.pyplot as plt

class Network:
    """Class that contains the keras network

    Attributes
    ----------
    model : keras model
        Network model
    threshold : float
        Threshold to binarizing images (the default is 0.3)

    """
    
    def __init__(self, model_path, threshold = 0.3):
        """init function
        
        Parameters
        ----------
        model_path : str
            path to network model
        threshold : float, optional
            threshold to binarizing images (the default is 0.3)
        
        """
        self.model = load_model(model_path)
        self.threshold = threshold

    def predict(self, imgs, verbose = 0):
        """Pass images by Network
        
        Parameters
        ----------
        imgs : np array
            images to be predicted
        verbose : int, optional
            set verbose mode in model predict (the default is 0)
        
        Returns
        -------
        np.array
            binarized results of prediccton
        """

        X_test = imgs.reshape(*imgs.shape,1)
        X_test = X_test.astype('float32')
        X_test/= 255

        prediction = self.model.predict(X_test, verbose=verbose)
        prediction[prediction > self.threshold] = 1
        prediction[prediction <= self.threshold] = 0

        prediction = prediction.reshape(*imgs.shape)

        return prediction.astype(np.uint8)* 255