# ZAMART
[Link Adaptable]( https://zamart.adaptable.app/main)

Naufal Aulia - 2206082455 - PBP E

## Implementasi _checklist_ dari awal sampai akhir
1. __Membuat sebuah proyek Django baru__
    1. Membuat direktori baru bernama ZaMart
    2. Membuat _virtual environment_ baru dengan menjalankan perintah berikut di dalam _terminal shell_ direktori
        * Mac
        ```bash
        python3 -m venv env
        ```
    3. Setelah itu, aktifkan _virtual environment_ dengan menjalankan kode berikut.
        * Mac
        ```bash
        source env/bin/activate
        ```
    4. Membuat berkas `requirements.txt` di dalam direktori yang sama dan tambahkan beberapa _dependencies_ yang diperlukan dalam proyek ini.
    5. Memasang _dependencies_ dengan menjalankan perintah berikut dan pastikan _virtual environment_ sedang berjalan.
        ```bash
        pip install -r requirements.txt
        ```
    6. Membuat proyek Django bernama ZaMart dengan perintah berikut.
        ```bash
        django-admin startproject ZaMart .
        ```
    7. Tambahkan `*` pada `ALLOWED_HOST` di `setings.py` untuk mengizinkan akses dari semua host, yang akan memungkinkan aplikasi diakses secara luas. 
        ```python
        ...
        ALLOWED_HOSTS = ["*"]
        ...
    8. Membuat file `.gitignore` di dalam direktori yang sama untuk menentukan berkas-berkas dan direktori-direktori yang harus diabaikan oleh Git.
2. __Membuat aplikasi dengan nama main pada proyek ZaMart.__
    1. Jalankan perintah berikut untuk membuat aplikasi baru, pastikan _virtual environment_ sudah aktif. 
        ```bash
        python manage.py startapp main
        ```
    2. Daftarkan `main` ke dalam proyek dengan membuka berkas `settings.py` di dalam proyek `ZaMart` dan cari variabel `INSTALLED_APPS`. Tambahkan 'main' ke dalam daftar aplikasi yang sudah ada.
3. __Melakukan _routing_ pada proyek agar dapat menjalankan aplikasi `main`.__
    1. Buka berkas `urls.py` di dalam direktori `ZaMart` dan import fungsi `include` dari `django.urls`
        ```python
        ...
        from django.urls import path, include
        ...
        ```
    2. Tambahkan rute URL seperti berikut untuk mengarahkan ke tampilan `main` dalam `urlpatterns`
        ```python
        urlpatterns = [
        ...
        path('main/', include('main.urls')),
        ...
        ]
        ```
4. __Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib.__
    1. Buka berkas `models.py` pada direktori `main` dan isi berkas tersebut dengan kode berikut.
        ```python
        from django.db import models

        class Product(models.Model):
            name = models.CharField(max_length=255)
            amount = models.IntegerField()
            description = models.TextField()
        ```
    2. Lakukan migrasi model dengan menjalankan perintah berikut.
        ```bash
        python3 manage.py makemigrations
        ```
        Lalu jalankan kode selanjutnya.
        ```bash
        python3 manage.py migrate
        ```
5. __Membuat sebuah fungsi pada views.py untuk dikembalikan ke dalam sebuah template HTML.__
    1. Buat direktori baru di dalam direktori `main` bernama `templates`.
    2. Buat berkas baru bernama `main.html` di dalam direktori `templates` dan isi dengan kode berikut.
        ```html
        <h1>Welcome To ZaMart</h1>

        <h5>Name: </h5>
        <p>{{ name }}</p>
        <h5>Class: </h5>
        <p>{{ class }}</p>
        ```
    3. Buka berkas `views.py` yang terletak pada berkas `main`. Tambahkan baris-baris impor berikut di bagian paling atas berkas dan tambahkan fungis `show_main`.
        ```python
        def show_main(request):
            context = {
                'name': 'Naufal Aulia',
                'class': 'PBP E'
            }
            return render(request, "main.html", context)
        ```
6. __Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi  `views.py`.__
    1. Buat berkas `urls.py` di dalam direktori `main`.
    2. Isi `urls.py` dengan kode berikut.
        ```python
        from django.urls import path
        from main.views import show_main

        app_name = 'main'

        urlpatterns = [
            path('', show_main, name='show_main'),
        ]
        ```
7. __Melakukan _depoloyment_ ke Adaptable__
    1. Membuat repositori baru di _github_ yang bernama ZaMart dan lakukan perintah `add`, `commit`, `branch`, `remote`, dan `push`.
    2. _Login_ pada website Adaptable.io dengan menggunakan akun github yang berisi repositori yang ingin di-_deploy_.
    3. Hubungkan Adaptable.io dengan GitHub dan pilih `All Repositories`pada proses instalasi.
    4. Pilih repositori `ZaMart` sebagai basis aplikasi yang akan di-_deploy_.
    5. Pilihlah `Python App Template` sebagai template deployment.
    6. Pilih `PostgreSQL` sebagai tipe basis data yang akan digunakan.
    7. Pilih versi python yang sesuai, dimana versi python yang digunakan saat ini adalah 3.10
    8. Pada bagian `Start Command` masukkan perintah `python manage.py migrate && gunicorn ZaMart.wsgi`.
    9. Masukkan `ZaMart` sebagai nama aplikasi yang juga akan menjadi nama domain situs web 
    10. Centang bagian `HTTP Listener on PORT` dan klik `Deploy App` untuk memulai proses _deployment_ aplikasi.

## Bagan _Request client_ ke web berbasis Django
![MVT MODEL](public/images/MVT.jpeg) 
- Client akan melakukan request ke aplikasi (server Django).
- Setelah itu, server akan memilih View sesuai request yang diberikan oleh client.
- Jika request tersebut perlu mengakses database, maka server akan memilih model serta mengakses database langsung.
- Hasil _response_ dari model akan ditampilkan sesuai template html yang sesuai.
- Template HTML akan menampilkan hasil dari _request_ yang diminta _client_ sebelumnya.

## Kenapa ***Virtual Environment?***
- _Virtual environment_ adalah lingkungan kerja yang terisolasi untuk mengembangkan sebuah perangkat lunak. _Virtual environment_ memungkinkan untuk mengisolasi paket-paket python yang digunakan dalam satu proyek dari paket-paket yang dipakai oleh proyek-proyek lainnya. Terdapat beberapa manfaat yang didapatkan saat menggunakan _virtual environment_ antara lain adalah:
    - Isolasi
    - Manajemen Idependensi
    - Kebersihan
    - Isolasi versi python
    - Portabilitas
- Proyek Django masih dapat dijalankan tanpa menggunakan _virtual environment_, akan tetapi terdapat hal-hal yang harus diperhatikan seperti konflik depensi dengan paket global, penggunaan versi python, dan masih banyak hal lagi. 
- Penggunaan _virtual environment_ dalam menjalankan proyek Django sangat disarankan karena _virtual environment_ membantu menjaga proyek Django bersih, terisolasi, dan lebih mudah dikelola.
## Apa itu ***MVC, MVT, dan MVVM***
- MVC (Model View Controller)
    - Model : Berinteraksi dengan database dan logika bisnis aplikasi
    - View : Menampilkan data kepada pengguna
    - Controller : Berfungsi untuk mengatur alur aplikasi dan sebagai perantara antara Model dan View
- MVT (Model View Template)
    - Model : Berinteraksi dengan database dan logika bisnis aplikasi
    - View : Menampilkan data kepada _user_, namun juga berisi logika untuk menampilkan data kepada pengguna
    - Template : Berfungsi untuk memproses tampilan yang berisi kode HTML yang digunakan untuk menampilkan data
- MVVM (Model View ViewModel)
    - Model : Bertanggung jawab atas abstraksi sumber data
    - View : Berfungsi untuk menginformasikan ViewModel tentang tindakan pengguna. View juga  mengamati ViewModel dan tidak mengandung logika aplikasi apa pun.
    - ViewModel : Bergfungsi untuk mengekspos aliran data yang relevan dengan View. Selain itu, itu server sebagai penghubung antara Model dan View.
- Perbedaan utama antara ketiga model:
    - MVC : Terdapat controller sebagai pengelola alur utama aplikasi dan perantara antara view dan model
    - MVT : Terdapat template sebagai komponen untuk menampilkan tampilan dan view memiliki logika lebih untuk penampilan data
    - MVMM : Terdapat ViewModel sebagai perantara yang mengubah data dari model ke format yang lebih sesuai untuk tampilan

