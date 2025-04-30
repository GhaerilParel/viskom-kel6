# Menggunakan base image Python 3.10
FROM python:3.10

# Set environment variable untuk memastikan pip tidak menulis bytecode .pyc ke file
ENV PYTHONDONTWRITEBYTECODE 1

# Set environment variable untuk memastikan buffer stdout/stderr dikelola secara langsung
ENV PYTHONUNBUFFERED 1

# Memperbarui pip, setuptools, wheel ke versi terbaru
RUN pip install --upgrade pip setuptools wheel

# Install build tools yang diperlukan seperti build-essential dan python3-dev
RUN apt-get update && apt-get install -y build-essential python3-dev

# Menyiapkan direktori kerja di dalam container
WORKDIR /app

# Menyalin file requirements.txt ke dalam container
COPY requirements.txt /app/

# Membuat virtual environment di dalam container
RUN python -m venv /opt/venv

# Mengaktifkan virtualenv dan menginstal dependensi dari requirements.txt
RUN . /opt/venv/bin/activate && pip install -r /app/requirements.txt

# Menyalin semua file dari proyek lokal ke dalam container
COPY . /app/

# Menetapkan direktori kerja di dalam container
WORKDIR /app

# Menentukan perintah untuk menjalankan aplikasi Flask menggunakan Gunicorn
CMD ["/opt/venv/bin/gunicorn", "app:app"]

# Expose port 8000 untuk aplikasi web
EXPOSE 8000
