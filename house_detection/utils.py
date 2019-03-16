import cv2



def imgs_are_equal(img1, img2):
    if img1.shape == img2.shape:
        difference = cv2.subtract(img1, img2)
        if len(difference.shape) > 2:
            b, g, r = cv2.split(difference)
            return cv2.countNonZero(b) == 0 and cv2.countNonZero(g) == 0 and cv2.countNonZero(r) == 0
        else :
            return cv2.countNonZero(difference) == 0
    return False



if __name__ == "__main__":
    img = cv2.imread("austin35_1500.tif",cv2.IMREAD_GRAYSCALE)
    cv2.imwrite("austin35_1500_gray.tif", img)
    #mg = cv2.imread("g.png")
    #print(imgs_are_equal(img, mg))