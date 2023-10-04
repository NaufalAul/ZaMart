# ZAMART
[Link Adaptable]( https://zamart.adaptable.app/main)

Naufal Aulia - 2206082455 - PBP E

# Tugas 2
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
    2. Tambahkan rute URL main di `urlpatterns` untuk mengarahkan ke tampilan `main`
        
4. __Membuat model pada aplikasi `main` dengan nama `Item` dan memiliki atribut wajib.__
    1. Buka berkas `models.py` pada direktori `main` dan isi berkas tersebut dengan model yang diinginkan.
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
    2. Buat berkas baru bernama `main.html` di dalam direktori `templates` dan isi berkas tersebut dengan kode html yang diinginkan.
    3. Buka berkas `views.py` yang terletak pada berkas `main`. Tambahkan baris-baris impor berikut di bagian paling atas berkas dan tambahkan fungsi `show_main`.
6. __Membuat sebuah routing pada urls.py aplikasi main untuk memetakan fungsi  `views.py`.__
    1. Buat berkas `urls.py` di dalam direktori `main`.
    2. Isi `urls.py` dengan path yang diinginkan.
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


# Tugas 3
## Perbedaan __POST__ dan __GET__ dalam Django
- Perbedan utama antara form POST dan GET dalam Django terletak pada metode yang digunakan untuk mengirim data dari form ke server dan bagaimana data tersebut diproses.
- Form POST
    - Metode POST lebih __aman__ untuk mengirim data sensitif karena data yang dikirim tidak akan terlihat dalam `URL`.
    - Data form dikirim dalam tubuh permintaan HTTP, sehingga tidak terlihat oleh pengguna atau dalam URL.
    - Form POST digunakan ketika ingin mengirim data yang sensitif atau data yang akan memengaruhi perubahan di server, seperti menambahkan data baru ke database.
    
- Form GET
    - Metode GET __kurang aman__ untuk data sensitif karena data yang dikirimkan terlihat dalam URL dan dapat dengan mudah diakses oleh pengguna atau oleh seseorang yang melihat log server.
    - Data form dikirim sebagai parameter query string yang terlihat dalam `URL`.
    - Form GET digunakan ketika ingin melakukan pencarian atau mengambil data dari server tanpa memengaruhi data di server.

- Sumber
    - https://www.baeldung.com/cs/http-get-vs-post
    - https://www.w3schools.com/tags/ref_httpmethods.asp

## Perbedaan utama antara __XML__, __JSON__, dan __HTML__ dalam konteks pengiriman data
PERBEDAAN | XML | JSON | HTML |
| --- | --- | --- | --- |
|Tujuan | Menyimpan dan mentransmisikan data terstruktur | Menyimpan dan mentransmisikan data terstruktur | Merender konten web, seperti teks, gambar, tautan, dan media
|Tipe Data | Tidak memiliki tipe data bawaan, mendukung berbagai tipe data | Mendukung tipe data yang terbatas seperti string, angka, boolean, objek, larik, dan null | Mendukung tipe data khusus untuk elemen-elemen seperti teks, gambar, tautan, dan elemen media |
|Format | Bahasa Markup | Format Data (JavaScript) | Bahasa Markup|
|Basis | SGML | JavaScript | SGML |
|Encoding | Mendukung berbagai encoding | Hanya mendukung UTF-8 encoding | Mendukung berbagai encoding|

- Sumber
    - https://www.deltaxml.com/blog/xml/whats-the-relationship-between-xml-json-html-and-the-internet/
    - https://www.w3schools.com/js/js_json_xml.asp

## Mengapa __JSON__ sering digunakan dalam pertukaran data antara aplikasi web modern?

`JSON` sering digunakan dalam pertukaran data antara aplikasi web modern karena beberapa alasan, antara lain:
- __Ringkas dan mudah dipahami__, JSON memiliki format yang sederhana dan mudah dipahami. Data disusun dalam bentuk pasangan "nama-nilai" yang mirip dengan struktur data dalam bahasa pemrograman, seperti objek dan array. 
- __Ringan__, JSON adalah format yang ringan dalam hal penggunaan bandwidth. Ini sangat penting dalam lingkungan web di mana penghematan bandwidth dapat meningkatkan kinerja dan efisiensi.
- __Mendukung berbagai data__, JSON mendukung berbagai jenis data, termasuk teks, angka, boolean, objek, array, dan null. Ini memungkinkan representasi data yang kompleks dan bervariasi.
- __Dukungan browser__, JSON dapat dengan mudah diurai (parsed) oleh browser web menggunakan JavaScript. Ini membuatnya ideal untuk komunikasi antara aplikasi web klien dan server.

- Sumber
    - https://www.sekawanmedia.co.id/blog/json-adalah/
    - https://media.neliti.com/media/publications/267827-penerapan-data-json-untuk-mendukung-peng-b1a9128a.pdf

## Implementasi _checklist_ dari awal sampai akhir
1. __Membuat input form untuk menambahkan objek model pada app sebelumnya__
    - Membuat `forms.py` pada direktori `main` untuk membuat struktur form yang dapat menerima data item baru. Menambahkan class ProductForm dengan models dari product dan fields `["name", "amount", "price", "description"]`.
2. __Menambahkan 5 fungsi `views` untuk melihat objek yang sudah ditambahkan__
    - Membuat fungsi baru bernama `create_product` yang menerima parameter request. Fungsi tersebut membuat ProductForm baru dan menyimpan dengan input user yang valid. Setelah itu redirect ke '/' (main) setelah data form berhasil disimpan.
    - Mengubah fungsi `show_main` untuk mendapatkan semua data dari Item, lalu Item tersebut ditambahkan ke context yang nantinya akan di render.
    - Menambahkan path url `create_product` pada urls.py di main yang akan menjalankan fungsi `create_product`
    - Membuat file HTML baru `create_product.html` yang isinya form sesuai fields pada forms.py untuk user mengisi inputan.
    - Menambahkan kode pada `main.html` untuk menampilkan data item dan tombol untuk redirect ke halaman form.
    - Membuat fungsi `show_xml` pada view yang isinya mengambil semua data dari Item dan mengembalikan HTTP response dalam format XML.
    - Membuat fungsi `show_json` pada view yang isinya mengambil semua data dari Item dan mengembalikan HTTP response dalam format JSON.
    - Membuat fungsi `show_xml_by_id` pada view yang isinya mengambil data dari Item yang sesuai dengan `primary key` dari url dan mengembalikan HTTP response dalam format XML.
    - Membuat fungsi `show_json_by_id` pada view yang isinya mengambil data dari Item yang sesuai dengan `primary key` dari url dan mengembalikan HTTP response dalam format JSON.

3. __Membuat routing URL untuk masing-masing views yang telah ditambahkan__
    - Mengimpor `show_main, create_product, show_xml, show_json, show_xml_by_id, show_json_by_id ` dari `main.views` untuk melakukan routing URL.
    - Membuat routing url atau path url `xml/` pada urls.py di main yang akan menjalankan fungsi `show_xml`.
    - Membuat routing url atau path url `json/` pada urls.py di main yang akan menjalankan fungsi `show_json`.
    - Membuat routing url atau path url `xml/<int:id>/` pada urls.py di main yang akan menjalankan fungsi `show_xml_by_id` dan meneruskan id ke fungsi tersebut.
    - Membuat routing url atau path url `json/<int:id>/` pada urls.py di main yang akan menjalankan fungsi `show_json_by_id` dan meneruskan id ke fungsi tersebut.

## Hasil akses fungsi views yang menampilkan objek dalam beberapa format
- __HTML__
![HTML](public/images/HTML.png)
- __XML__
![XML](public/images/XML.png)
- __JSON__
![JSON](public/images/JSON.png)
- __XML by id__
![XMLID](public/images/XMLID.png)
- __JSON by id__
![JSONID](public/images/JSONID.png)


# Tugas 4
## Apa itu Django `UserCreationForm`, serta jelaskan apa kelebihan dan kekurangannya?
Django `UserCreationForm` adalah _pre-built form_ yang disediakan oleh Django yang memungkinkan pengembang dengan mudah membuat _form_ untuk pendaftaran pengguna. Django `UserCreationForm` merupakan _subclass_ dari `django.contrib.auth.forms.UserCreationForm` yang merupakan sebuah subkelas dari `Django.contrib.auth.forms`.Django `UserCreationForm` menyediakan `fileds` untuk nama pengguna, kata sandi, dan konfirmasi kata sandi, serta menyertakan validasi untuk memastikan bahwa kata sandi cocok dan memenuhi kompleksitas yang diperlukan.
- Kelebihan Django `UserCreationForm`:
  - __Menghemat waktu development__, `UserCreationForm` menyediakan cara mudah untuk membuat form pendaftaran pengguna dengan kode minimal yang menangani validasi kata sandi dan memastikan bahwa kata sandi cocok, sehingga menghemat waktu dan tenaga pengembang.
  - __Fitur keamanan bawaan__, `UserCreationForm `secara otomatis mengenkripsi kata sandi dengan kunci keamanan yang panjang, memastikan bahwa kata sandi pengguna disimpan dengan aman di database.
  - __Integrasi dengan Django__, `UserCreationForm` terintegrasi dengan baik dengan framework Django, sehingga mempermudah pengembangan aplikasi web menggunakan Django.

- Kekurangan Django 'UserCreationForm':
  - __Fleksibilitas terbatas__, `UserCreationForm` memiliki serangkaian bidang dan aturan validasi yang telah ditentukan sebelumnya. Jika perlu mengkustomisasi form secara ekstensif atau memiliki persyaratan validasi yang rumit, mungkin lebih cocok untuk membuat form kustom dari awal.
  - __Ketergantungan pada Django__, `UserCreationForm` hanya bisa digunakan dalam proyek yang menggunakan _framework_ Django, sehingga sistem autentikasi mungkin tidak cocok untuk aplikasi/proyek yang tidak menggunakan _framework_ Django.

## Apa perbedaan antara autentikasi dan otorisasi dalam konteks Django, dan mengapa keduanya penting?
Autentikasi dan otorisasi dalam Django merupakan hal yang penting, berikut adalah perbedaan dari keduannya:
- __Autentikasi__
  Autentikasi adalah proses verifikasi identitas pengguna. Autentikasi mengonfirmasi bahwa pengguna tersebut adalah siapa yang mereka klaim dengan memeriksa kredensial mereka, seperti nama pengguna dan kata sandi, terhadap database pengguna terdaftar. Sistem autentikasi bawaan Django menyediakan fitur untuk registrasi pengguna, login, dan pengelolaan kata sandi. Ketika pengguna diautentikasi, Django menyetel sebuah _session_ dan melampirkan atribut pengguna pada permintaan, mengizinkan tampilan dan templat untuk mengakses informasi pengguna yang diautentikasi. Autentikasi sangat penting untuk memastikan bahwa hanya individu yang berwenang yang dapat mengakses bagian aplikasi yang dibatasi.

- __Otorisasi__
  Otorisasi menentukan tindakan apa yang boleh dilakukan pengguna dalam suatu aplikasi. Otorisasi mengontrol akses ke berbagai bagian aplikasi berdasarkan peran pengguna, izin, atau kriteria lainnya. Di Django, sistem otorisasi dibangun di atas sistem otentikasi dan menggunakan _user groups_ dan izin untuk mengontrol akses. _User groups_ dapat dibuat untuk mewakili peran atau kategori pengguna yang berbeda, dan izin dapat diberikan ke grup ini. Django menyediakan cara yang fleksibel untuk mengelola akses dan izin pengguna, memungkinkan pengembang untuk menentukan _backend_ dan izin otorisasi khusus sesuai kebutuhan aplikasi mereka.

Secara singkat autentikasi memverifikasi identitas pengguna, sementara otorisasi menentukan tindakan apa yang boleh dilakukan pengguna dalam suatu aplikasi. Autentikasi dan otorisasi penting untuk menjaga keamanan dan integritas aplikasi.Dengan mengautentikasi pengguna, kita dapat memastikan bahwa hanya pengguna sah yang dapat mengakses aplikasi, sementara otorisasi memungkinkan kita mengontrol dan membatasi tindakan yang dapat pengguna lakukan dalam aplikasi berdasarkan peran dan izin pengguna.

## Apa itu cookies dalam konteks aplikasi web, dan bagaimana Django menggunakan cookies untuk mengelola data sesi pengguna?
_Cookies_ adalah sejumlah potongan kecil data yang disimpan di komputer pengguna oleh sebuah situs web. _Cookies_ digunakan untuk mengingat informasi tentang pengguna dan preferensi mereka, memungkinkan situs web memberikan pengalaman pengguna yang dipersonalisasi dan lancar. Dalam konteks aplikasi web, cookie biasanya digunakan untuk manajemen sesi, melacak preferensi pengguna, dan menjaga status pengguna di antara permintaan.

Django menggunakan _cookies_ untuk mengelola sesi pengguna dengan mengenkripsi data sesi dan menyimpannya di sisi server. _Cookies_ yang dikirim ke klien hanya berisi ID sesi yang unik. Ketika klien mengirim permintaan berikutnya, _cookies_ dengan ID sesi akan dikirim ke server dan Django akan menggunakan ID tersebut untuk mengambil sesi data yang sudah disimpan sebelumnya. Dengan ini, Django dapat mengelola data sesi pengguna dengan aman. 

## Apakah penggunaan cookies aman secara default dalam pengembangan web, atau apakah ada risiko potensial yang harus diwaspadai?
Penggunaan _cookies_ secara _default_  dianggap aman dalam pengembangan web karena informasi dalam cookies tidak dapat diubah oleh pengguna atau pihak ketiga tanpa izin. _Cookies_ yang hanya menyimpan informasi seperti ID sesi atau preferensi pengguna biasanya dianggap aman. Akan tetapi, belum tentu penggunaan _cookies_ secara _default_ ini aman. Terdapat risiko keamanan yang dihadapi, antara lain:
- __Cross-Site Scripting (XSS)__, Penyerang dapat memanfaatkan kerentanannya XSS untuk mencuri cookies pengguna. Hal ini dapat menyebabkan akses tidak sah ke akun pengguna dan informasi sensitif. 
- __Cross-Site Request Forgery (CSRF)__, Serangan CSRF terjadi ketika situs web berbahaya mengelabui browser pengguna agar membuat permintaan yang tidak diinginkan ke situs web lain tempat pengguna diautentikasi. Jika situs web target hanya mengandalkan cookie untuk autentikasi, situs tersebut dapat memproses permintaan tidak sah ini, sehingga menyebabkan tindakan yang dilakukan atas nama pengguna tanpa persetujuan mereka. Di Django sendiri, Django memiliki fitur bawaan yang melindungi hampir semua serangan CSRF.
- __Cookie/Session Poisoning__, Jika penyerang berhasil mendapatkan _cookie_ sesi pengguna, mereka dapat menyamar sebagai pengguna tersebut dan mendapatkan akses tidak sah ke akun pengguna.penyerang dapat mencuri cookies pengguna yang disimpan di browser mereka dengan teknik session hijacking atau cross-site scripting (XSS).


## Implementasi _checklist_ dari awal sampai akhir
1. Mengimplementasikan fungsi registrasi, login, dan logout untuk memungkinkan pengguna untuk mengakses aplikasi sebelumnya dengan lancar.
   - Membuat fungsi register untuk membuat akun baru yang mengimplementasikan UserCreationForm.
   - Membuat berkas register.hmtl pada direktori `main/templates` untuk visualisasi fungsi register.
   - Membuat fungsi login_user yang bertujuan untuk mengautentikasi pengguna yang ingin login dan mengatur _cookies_.
   - Membuat berkas login.hmtl pada direktori `main/templates` untuk visualisasi fungsi register.
   - Membuat fungsi logout_user yang bertujuan untuk melogout pengguna dan menghapus _cookies_
   - Menambahkan tombol logout pada main.html
   - Membuat routing url atau path url `register/` pada urls.py di main yang akan menjalankan fungsi `register`.
   - Membuat routing url atau path url `login/` pada urls.py di main yang akan menjalankan fungsi `login_user`.
   - Membuat routing url atau path url `logout/` pada urls.py di main yang akan menjalankan fungsi `logout_user`.
   - Merestriksi akses halaman main dengan menambahkan decorator `@login_required(login_url='/login')`
2.  Membuat dua akun pengguna dengan masing-masing tiga dummy data menggunakan model yang telah dibuat pada aplikasi sebelumnya untuk setiap akun di lokal.
3. Menghubungkan model `Item` dengan `User`.
   - Pada berkas `models.py`  tambahkan import `User` dari `django.contrib.auth.model`.
   - Menambahkan model `user = models.ForeignKey(User, on_delete=models.CASCADE)` pada class Product.
   - Mengubah fungsi `create_product` pada berkas `views.py` untuk mengatur penyimpanan product pada setiap login pengguna.
   - Mengganti name pada context di show_main dengan `request.user.username`.
   - Melakukan migrasi model untuk menyimpan perubahan.

4.  Menampilkan detail informasi pengguna yang sedang logged in seperti username dan menerapkan cookies seperti last login pada halaman utama aplikasi.
   - Pada berkas `views.py' tambahkan import `HttpResponseRedirect`, `reverse`, dan `datetime` pada bagian paling atas.
   - Menambahkan kode pada blok `if user is not None:` pada `login_user` untuk mengatur _cookie_.
   - Menambahkan kode pada blok `if user is not None:` pada `logout_user` untuk mengatur _cookie_.
   - Menambahkan key last_login pada context di show_main dengan isi cookies last_login.
   - Menambahkan pada main.html visual untuk last_login dari context.


# Tugas 5
## Manfaat dari setiap element selector dan kapan waktu yang tepat untuk menggunakannya
1. Class Selector
    - Memilih elemen-elemen yang memiliki atribut class tertentu.
    - Berguna ketika ingin memengaruhi beberapa elemen yang memiliki kelas yang sama tanpa memengaruhi elemen lain yang mungkin menggunakan kelas yang sama.
2. Elemen Selector
    - Memilih semua elemen dengan tipe tag tertentu, misalnya, `<p>`, `<h1>`, atau `<div>`.
    - Berguna ketika ingin memengaruhi semua elemen dengan tipe tag tertentu secara konsisten di seluruh halaman web.
3. ID Selector 
    - Memilih elemen dengan atribut id tertentu, yang harus unik di seluruh halaman web.
    - Digunakan ketika Anda ingin memengaruhi elemen tunggal dengan id tertentu.
4. Descendant Selector 
    - Memilih elemen yang merupakan turunan dari elemen lain, misalnya, memilih semua `<p>` dalam sebuah `<div>`.
    - Waktu yang Tepat: Berguna ketika Anda ingin memengaruhi elemen-elemen tertentu yang berada di dalam elemen lain.
5.  Child Selector (parent > child)
    - Memilih elemen yang merupakan anak langsung dari elemen lain, tidak termasuk anak cucunya.
    - Cocok untuk mengatur tata letak elemen anak yang langsung di dalam elemen induk.
6. Adjacent Sibling Selector (prev + next)
    - Memilih elemen yang merupakan saudara sejajar (siblings) dari elemen lain, dan berada tepat setelahnya.
    - Digunakan ketika Anda ingin memengaruhi elemen yang berdampingan atau berada tepat setelah elemen lain dengan tipe tag yang sama.
7. General Sibling Selector (prev ~ siblings)
    - Memilih semua elemen saudara sejajar yang memiliki elemen sejajar tertentu sebagai saudara.
    - Berguna ketika Anda ingin memengaruhi beberapa elemen saudara sejajar yang memiliki elemen sejajar tertentu.

## Apa itu HTML5 Tag
HTML5 adalah versi terbaru dari bahasa markup HTML (Hypertext Markup Language) yang digunakan untuk membangun struktur dasar halaman web. HTML5 memperkenalkan sejumlah tag baru dan perubahan signifikan dalam cara elemen-elemen HTML digunakan. Banyak elemen baru yang ditambahkan di HTML5 seperti nav, audio, figcaption, progress, command, time, datalist, video, figure, meter, data, section, time, aside, canvas, summary, rp, rt, details, wbr, header, footer, keygen, embed, article, hgroup, bdi, mark, output, source, track, section, ruby dan masih banyak lagi. Terdapat perbedaan HTML5 dengan HTML yang biasa (versi sebelumnya), antara lain adalah:
HTML | HTML5 |
| --- | --- |
Tidak mendukung audio dan video tanpa menggunakan dukungan pemutar flash. | Mendukung kontrol audio dan video dengan penggunaan tag `<audio>` dan `<video>`.
Menggunakan cookie untuk menyimpan data sementara. | Menggunakan database SQL dan cache aplikasi untuk menyimpan data offline.
Tidak mengizinkan JavaScript untuk berjalan di browser. | Mengizinkan JavaScript untuk berjalan di latar belakang. Hal ini dimungkinkan karena JS Web worker API di HTML5.
Bekerja dengan semua browser lama. | Mendukung oleh semua browser baru seperti Firefox, Mozilla, Chrome, Safari, dll.
Versi HTML yang lebih lama kurang ramah seluler. | Bahasa HTML5 lebih _mobile-friendly_.



## Jelaskan perbedaan antara margin dan padding
- Margin
    - Margin adalah ruang kosong di sekitar batas luar elemen HTML.
    - Margin adalah jarak antara elemen HTML dengan elemen-elemen di sekitarnya (elemen tetangga).
    - Margin digunakan untuk mengendalikan jarak antara elemen dengan elemen-elemen di luar elemen tersebut.
    - Margin tidak memiliki latar belakang dan warna, dan tidak berpengaruh pada ukuran atau tampilan elemen itu sendiri.

- Padding
    - Padding adalah ruang kosong di antara batas dalam elemen HTML dan kontennya sendiri.
    - Padding adalah jarak antara konten elemen dan batas dalam elemen tersebut.
    - Padding digunakan untuk mengendalikan ruang di dalam elemen HTML, seperti ruang di antara teks dan batas elemen.
    - Padding tidak memiliki latar belakang atau warna tetapi memengaruhi tampilan elemen, menggeser konten lebih ke dalam elemen tersebut.

Dalam gambaran yang lebih sederhana, margin mengatur jarak di luar elemen (seperti ruang di antara elemen-elemen), sedangkan padding mengatur ruang di dalam elemen (seperti ruang di antara konten dan batas elemen).

## Jelaskan perbedaan antara framework CSS Tailwind dan Bootstrap
- Tailwind
    - Pendekatan Utility-First: Tailwind CSS mengikuti pendekatan "utility-first", di mana Anda membangun tampilan web dengan menggabungkan kelas-kelas kecil yang mengontrol properti seperti warna, margin, padding, dan banyak lagi. Ini memberikan fleksibilitas yang tinggi dalam mengkustomisasi tampilan.
    - Kustomisasi: Tailwind memungkinkan pengguna untuk menyesuaikan desain dengan mudah melalui konfigurasi file, sehingga Anda dapat menentukan gaya desain yang sangat spesifik sesuai kebutuhan Anda.
    - Kecil dan Cepat: Tailwind dibangun dengan ukuran yang lebih kecil daripada Bootstrap, sehingga dapat menghasilkan situs web yang lebih ringan dalam hal ukuran file CSS.

- Bootstrap
    - Pendekatan Komponen: Bootstrap memiliki pendekatan berbasis komponen, di mana elemen UI (seperti tombol, kartu, atau jumbotron) dikemas menjadi komponen yang dapat digunakan kembali. Ini membuat Bootstrap lebih mudah digunakan jika Anda ingin membangun situs dengan cepat menggunakan komponen yang telah tersedia.
    - Desain Responsif: Bootstrap memiliki dukungan bawaan untuk desain responsif, yang memudahkan pengembang untuk membuat situs yang dapat menyesuaikan diri dengan berbagai perangkat dan ukuran layar.
    - Dokumentasi yang Kuat: Bootstrap memiliki dokumentasi yang sangat kuat dan komunitas yang besar, sehingga mudah untuk menemukan sumber daya dan bantuan jika Anda mengalami masalah.

Bootstap digunakan jika ingin membangun situs web dengan cepat dan menginginkan komponen-komponen UI yang sudah ada. Bootstrap juga cocok untuk proyek-proyek kecil atau ketika tidak ingin menghabiskan banyak waktu menyesuaikan desain. Sementara itu, Tailwind dapat digunakan jika ingin memiliki tingkat kontrol yang tinggi atas desain dan siap untuk menulis lebih banyak kode HTML dengan menggabungkan kelas-kelas utilitas. Tailwind cocok untuk proyek-proyek yang memerlukan desain yang sangat spesifik atau desain yang unik.

## Implementasi _checklist_ dari awal sampai akhir
1.  Kustomisasi desain pada templat HTML
    - Kustomisasi halaman login, register, dan tambah inventori
        - Menggunakan _framework_ Bootstrap untuk melakukan kustomisasi pada ketiga halaman tersebut seperti menggunakan button, table, setting margin dan padding bawaan dari Bootstrap.
        - Menggunakan CSS untuk melakukan kustomisasi pada beberapa komponen
    - Kustomisasi halaman daftar inventori menjadi lebih berwarna maupun menggunakan apporach lain seperti menggunakan Card.
        - Menggunakan card untuk kustomisasi daftar inventori serta mengkustomisasi warna table dengan fitur bawaan bootstrap.
        - Menggunakan styling CSS untuk kustomisasi daftar inventori