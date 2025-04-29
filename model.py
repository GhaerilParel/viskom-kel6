import tensorflow as tf
from tensorflow.keras.preprocessing import image
import numpy as np

# Memuat model yang sudah dilatih (InceptionV3 dalam hal ini)
model = tf.keras.models.load_model('model/benar_model_inceptionv3.h5')

def predict_image(image_path):
    # Memuat dan memproses gambar sesuai input model
    img = image.load_img(image_path, target_size=(224, 224))  # Gambar diubah ukurannya menjadi (224, 224)
    img_array = image.img_to_array(img)  # Mengubah gambar menjadi array
    img_array = np.expand_dims(img_array, axis=0)  # Menambahkan batch dimension
    img_array /= 255.0  # Normalisasi gambar

    # Melakukan prediksi dengan model
    predictions = model.predict(img_array)
    return predictions
