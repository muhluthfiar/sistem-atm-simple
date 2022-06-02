# Queue Pada Transaksi ATM
Suatu ATM dapat melakukan transaksi. Setiap melakukan transaksi, akan dikenai cooldown selama 2 menit dan jika dilakukan terus-menerus hingga tiga kali akan ditolak oleh sistem karena ATM masih dalam proses penyelesaian transaksi. 

Proses queue terjadi saat user memasukkan perintah fungsi, kemudian sistem  akan memasukkan transaksi ke dalam queue. Total queue yang dapat ditampung sistem sebesar 3 transaksi.

## Cara Kerja Sistem
Terdapat fitur yang tersedia pada Sistem ATM kami, antara lain:

- Register
- Login
- Cek Saldo
- Transfer
- Tambah Saldo
- Tarik Tunai
- Data User
- Kuota Transaksi

## Pembahasan
Pembahasan fitur yang tersedia
> Register

Pengguna baru akan memasukkan username, password pin, dan saldo awal ke dalam sistem. Kemudian sistem akan membuatkan nomor rekening secara random. 

Data pengguna baru akan dimasukkan dalam data pengguna sistem sehingga user bisa melakukan login.

> Login

User perlu memasukkan username dan pin lalu akan dicek oleh sistem apakah sudah sesuai dengan data pada sistem. 

Kemudian jika sudah sesuai, akan menampilkan menu selanjutnya.

> Menu Utama

Setelah user login, sistem akan menampilkan menu utama untuk melakukan transaksi

> Transfer

Sistem meminta nomor rekening yang dituju dan nominal jumlah uang yang akan ditransfer.

Sistem akan menampilkan konfirmasi transfer kemudian menyuruh user untuk memilih lanjut atau batal.

> Tarik Tunai & Tambah Saldo
- Tambah Saldo

  Sistem meminta nominal jumlah uang yang ingin ditambahkan. 

- Tarik Tunai

  Sistem meminta nominal jumlah uang yang ingin diambil

User bisa membatalkan transaksi dengan memasukkan angka nol (0)

> User Data & Cek Saldo
- Cek Saldo

  Sistem akan menampilkan total saldo yang dimiliki oleh user

- User Data
  
  Sistem akan menampilkan data user yang ada pada sistem

> Kuota Transaksi

Sistem akan menampilkan queue yang sedang dijalankan oleh sistem
