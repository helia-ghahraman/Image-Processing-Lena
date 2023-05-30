import cv2
import numpy as np


def darker_lighter(picture, change, height, width):
    image = np.empty((height, width), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            new = picture[y][x] + change
            if new > 255:
                new = 255
            elif new < 0:
                new = 0
            image[y][x] = new
    return image


def change_contrast(picture, change, height, width):
    image = np.empty((height, width), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            new = picture[y][x] * change
            if new > 255:
                new = 255
            elif new < 0:
                new = 0
            image[y][x] = int(new)
    return image

def invert(picture, height, width):
    image = np.empty((height, width), dtype=np.uint8)
    for y in range(height):
        for x in range(width):
            image[y][x] = 255 - picture[y][x]
    return image


if __name__ == "__main__":
    picture = cv2.imread('./images/Lena.bmp', cv2.IMREAD_GRAYSCALE)
    height, width = picture.shape
    image = darker_lighter(picture, 100, height, width)
    cv2.imwrite('./images/LenaLighter.bmp', image)
    image = darker_lighter(picture, -100, height, width)
    cv2.imwrite('./images/LenaDarker.bmp', image)
    image = change_contrast(picture, 2, height, width)
    cv2.imwrite('./images/higherContrast.bmp', image)
    image = change_contrast(picture, 0.5, height, width)
    cv2.imwrite('./images/lowerContrast.bmp', image)
    image = invert(picture, height, width)
    cv2.imwrite('./images/inverted.bmp', image)
