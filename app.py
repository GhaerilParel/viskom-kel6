from flask import Flask, request, render_template
import os
from model import predict_image  # Fungsi dari model.py untuk prediksi
from utils import prepare_image  # Fungsi dari utils.py untuk memproses gambar

app = Flask(__name__)

# Direktori upload gambar
UPLOAD_FOLDER = 'static/images/'
app.config['UPLOAD_FOLDER'] = UPLOAD_FOLDER

# Memastikan folder 'static/images/' ada
if not os.path.exists(app.config['UPLOAD_FOLDER']):
    os.makedirs(app.config['UPLOAD_FOLDER'])

# Daftar kelas pakaian berdasarkan hasil training (kelas yang Anda tampilkan)
class_names = [
    "Backpacks", "Belts", "Briefs", "Coat", "Cutoffs", 
    "Flip Flops", "Formal Shoes", "Handbags", "Heels", 
    "Hoodie", "Jeans", "Kurtas", "Sandals", "Shirts", 
    "Socks", "Sports Shoes", "Sunglasses", "Tshirts", 
    "Wallets", "Watches"
]

@app.route('/')
def index():
    return render_template('index.html')

@app.route('/predict', methods=['POST'])
def predict():
    if 'image' not in request.files:
        print("No file uploaded")  # Debugging
        return {'error': 'No file uploaded'}, 400

    file = request.files['image']
    if file.filename == '':
        print("No selected file")  # Debugging
        return {'error': 'No selected file'}, 400

    print(f"File received: {file.filename}")  # Debugging
    
    # Menyimpan file yang diupload
    file_path = os.path.join(app.config['UPLOAD_FOLDER'], file.filename)
    file.save(file_path)

    # Memproses gambar dan prediksi
    img = prepare_image(file_path)  # Fungsi untuk memproses gambar
    predictions = predict_image(file_path)  # Fungsi untuk melakukan prediksi

    # Ambil hasil prediksi (angka kelas yang diprediksi)
    predicted_class_index = predictions.argmax(axis=-1)  # Mengambil indeks kelas dengan probabilitas tertinggi
    
    # Mempetakan hasil prediksi ke nama kelas berdasarkan indeks
    predicted_class_name = class_names[predicted_class_index[0]]

    # Mengembalikan hasil prediksi dalam format JSON
    return {'prediction': predicted_class_name}


# ...existing code...

    
if __name__ == "__main__":
    app.run(host="0.0.0.0", port=5000)  # port bebas, Render override nanti
