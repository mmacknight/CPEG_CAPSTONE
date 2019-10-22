import cv2
import numpy as np

def applyCustomColorMap(im_gray) :

    lut = np.zeros((256, 1, 3), dtype=np.uint8)

    lut[:, 0, 0] = [i for i in range(200)] + [0 for i in range(56)]

    lut[:, 0, 1] = [i for i in range(200) ] +[0 for i in range(56)]


    lut[:, 0, 2] = [i for i in range(200)] +[0 for i in range(56)]


    im_color = cv2.LUT(im_gray, lut)

    return im_color;


if __name__  == '__main__' :

    im = cv2.imread("kirk.jpg",cv2.IMREAD_COLOR);
    # im = cv2.cvtColor(im, cv2.COLOR_GRAY2BGR);
    im_color = applyCustomColorMap(im);

    cv2.imwrite('/tmp/colormap_algae.jpg', im_color)
    cv2.imshow("Pseudo Colored Image", im_color);
    cv2.waitKey(0);
