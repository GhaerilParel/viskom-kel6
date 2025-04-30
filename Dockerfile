# Menggunakan image Python yang sesuai
FROM python:3.10

# Memperbarui pip, setuptools, dan wheel
RUN pip install --upgrade pip setuptools wheel

# Instalasi build tools jika diperlukan
RUN apt-get update && apt-get install -y build-essential python3-dev

# Menyalin file requirements.txt
COPY requirements.txt /app/

# Menginstal dependensi dari requirements.txt
RUN python -m venv /opt/venv
RUN . /opt/venv/bin/activate && pip install -r /app/requirements.txt

# Menyalin seluruh aplikasi ke container
COPY . /app/

# Menetapkan direktori kerja
WORKDIR /app

# Perintah untuk menjalankan aplikasi
CMD ["python", "app.py"]