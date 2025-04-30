# Menggunakan base image Python 3.10
FROM python:3.10

# Memperbarui pip, setuptools, dan wheel
RUN pip install --upgrade pip setuptools wheel

# Instalasi build tools yang diperlukan seperti build-essential dan python3-dev
RUN apt-get update && apt-get install -y build-essential python3-dev

# Menyiapkan direktori kerja di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt /app/

# Membuat virtual environment di dalam container
RUN python -m venv /opt/venv

# Memperbarui pip di virtual environment dan menginstal dependensi
RUN /opt/venv/bin/pip install --upgrade pip
RUN /opt/venv/bin/pip install -r /app/requirements.txt

# Menyalin seluruh aplikasi dari proyek lokal ke dalam container
COPY . /app/

# Menetapkan direktori kerja di dalam container
WORKDIR /app

# Menentukan perintah untuk menjalankan aplikasi menggunakan Gunicorn
CMD ["/opt/venv/bin/gunicorn", "app:app"]

# Expose port 8000 untuk aplikasi web
EXPOSE 8000
