import cv2
import numpy as np
from utils.visual import get_global_images


def key_pressed(key: str):
    return cv2.waitKey(1) & 0xFF == ord(key)


def show_image(img: np.array):
    cv2.imshow('1', img)


def show_all_images():
    images = get_global_images()
    for i, img in enumerate(images):
        cv2.imshow(str(i), img)


def close_all_images():
    images = get_global_images()
    for i, img in enumerate(images):
        cv2.destroyWindow(str(i))
