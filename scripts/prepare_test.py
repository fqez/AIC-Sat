import cv2
from house_detection.network import Network
from house_detection.postprocessor import Postprocessor
from house_detection.preprocessor import Preprocessor
import numpy as np

def main():
    pre = Preprocessor()
    post = Postprocessor()
    net = Network("model/aerial_model.h5")
    img = cv2.imread("tests/data/austin35_1500.tif")
    
    img_gray = pre._rgb2gray(img)
    cv2.imwrite("tests/data/austin35_1500_gray.tif", img_gray)
    np.save("tests/data/austin35_1500_gray.npy", img_gray)


    factor, img_res = pre._resize_img(img_gray)
    cv2.imwrite("tests/data/austin35_1024.tif", img_res)
    np.save("tests/data/austin35_1024.npy", img_res)
    
    arr_img = pre._crop_image(img_res, 2)
    cv2.imwrite("tests/data/austin35_1024_1.tif", arr_img[0])
    np.save("tests/data/austin35_1024_1.npy", arr_img[0])
    cv2.imwrite("tests/data/austin35_1024_2.tif", arr_img[1])
    np.save("tests/data/austin35_1024_2.npy", arr_img[1])
    cv2.imwrite("tests/data/austin35_1024_3.tif", arr_img[2])
    np.save("tests/data/austin35_1024_3.npy", arr_img[2])
    cv2.imwrite("tests/data/austin35_1024_4.tif", arr_img[3])
    np.save("tests/data/austin35_1024_4.npy", arr_img[3])

    predicted = net.predict(arr_img)

    cv2.imwrite("tests/data/austin35_pred_1.tif", predicted[0])
    np.save("tests/data/austin35_pred_1.npy", predicted[0])
    cv2.imwrite("tests/data/austin35_pred_2.tif", predicted[1])
    np.save("tests/data/austin35_pred_2.npy", predicted[1])
    cv2.imwrite("tests/data/austin35_pred_3.tif", predicted[2])
    np.save("tests/data/austin35_pred_3.npy", predicted[2])
    cv2.imwrite("tests/data/austin35_pred_4.tif", predicted[3])
    np.save("tests/data/austin35_pred_4.npy", predicted[3])

    img_rec = post._recompose_image(predicted)
    cv2.imwrite("tests/data/austin35_1024_bw.tif", img_rec)
    np.save("tests/data/austin35_1024_bw.npy", img_rec)
    
    houses = post._find_houses(img_rec)
    np.save("tests/data/austin35_houses_1024.npy", houses)

    houses_1500= post._rescalate_houses_dims(houses, factor)
    np.save("tests/data/austin35_houses_1500.npy", houses_1500)

    img2 = post.mark_houses(img, houses_1500)
    cv2.imwrite("tests/data/austin35_1500_marks.tif", img2)
    np.save("tests/data/austin35_1500_marks.npy", img2)

if __name__ == "__main__":
    main()