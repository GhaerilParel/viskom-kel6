import cv2
import numpy as np

def prepare_image(image_path):
    # Membaca gambar menggunakan OpenCV
    img = cv2.imread(image_path)
    img = cv2.cvtColor(img, cv2.COLOR_BGR2RGB)  # Mengubah ke RGB
    return img
