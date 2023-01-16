Password Manager

Password Manager adalah program sederhana untuk mengelola password menggunakan MySQL. Program ini menyediakan fitur seperti registrasi, login, menambah, memperbarui, dan menghapus akun, serta menampilkan akun yang tersimpan. Program ini menggunakan modul mysql.connector untuk terhubung dengan database MySQL dan modul getpass untuk menerima input password tanpa menampilkannya di layar. Program ini juga menggunakan hashlib untuk mengenkripsi password yang disimpan di database.

Fitur

  Registrasi
  
  Login
  
  add
  
  update
  
  delete
  
  displays
  
Penggunaan

  Clone atau download repository ini
  
  Buat database MySQL dengan nama "password_manager"
  
  Import file "password_manager.sql" ke dalam database tersebut
  
  Buka terminal atau command prompt dan arahkan ke direktori yang menyimpan file python
  
  Jalankan perintah python password_manager.py
  
Screenshot

registrasi


  ![register](https://user-images.githubusercontent.com/90265405/212736627-fa025767-2d6e-4f62-ae74-030e61d1c1d1.jpeg)
  
  
login


  ![login](https://user-images.githubusercontent.com/90265405/212736643-912de30f-1b6d-4ec9-a5c0-4cccad67696f.jpeg)
 
 
account database


  ![dbAccounts](https://user-images.githubusercontent.com/90265405/212736679-a639908d-3fc9-49e2-b20a-7e2d66f77c15.jpeg)


users database
 
 
 ![users](https://user-images.githubusercontent.com/90265405/212736693-209c7ae0-e78c-439c-b3f1-f383c8c708ad.jpeg)
  
  
  
  
Keterangan

  Pastikan anda sudah terinstall python dan library yang diperlukan diatas
  
  Pastikan anda sudah mengatur konfigurasi koneksi database yang benar di kode program
  
  Jangan lupa untuk mengubah password root pada konfigurasi koneksi database agar aman
  
  Program ini hanya digunakan untuk tujuan pendidikan dan tidak disarankan untuk digunakan pada sistem yang sesungguhnya.
