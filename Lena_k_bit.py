import cv2
import numpy as np
from sklearn.metrics import mean_squared_error


def k_grey_level_quantized_image(picture, level, height, width):
    image = np.empty((height, width), dtype=np.uint8)
    grey_levels = []
    step = int(255 / (level - 1))
    for i in range(0, 256, step):
        grey_levels.append(i)
    for y in range(height):
        for x in range(width):
            index = int((picture[y][x] / 256) * level)
            image[y][x] = grey_levels[index]
    return image


if __name__ == "__main__":
    picture = cv2.imread('./images/Lena.bmp', cv2.IMREAD_GRAYSCALE)
    height, width = picture.shape
    cv2.imshow('Original Lena', picture)
    bits = [1, 2, 4, 6]
    for bit in bits:
        level = 2 ** bit
        image = k_grey_level_quantized_image(picture, level, height, width)
        mean_square_error = mean_squared_error(image, picture)
        cv2.imshow('Lena Quantized ' + str(bit) + ' bit', image)
        print('Mean square error 256 - ' + str(bit) + ' bit pictures: ' + str(mean_square_error))
        cv2.imwrite('./images/LenaQuantized' + str(bit) + ' bit.bmp', image)
    cv2.waitKey(0)
