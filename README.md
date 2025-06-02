# bencana-alam
 
- projek ini memiliki 2 tabel, tabel negara untuk menyimpan nama negara dan total bencana yang terjadi dalam negari itu dan tabel bencana alam yang meyimpan id negrara(sebagai foreign key untuk mengakses negara yang mengalami bencana alam), tipe bencana alam,nama bencana alam, dan tahun bencana alam

- dalam webUInya terdapat 3 tombol yaitu: filter negara, tambah negara dan tambah becana

-tombol filter negara bekerja dengan menggunakan query.filterby untuk mendapatkan semua bencana alam yang mempunyai id negara itu

-tombol tambah negara pertama mengecek apakah negara yang diinput sudah di dalam tabel dan jika iya ,programnya akan reload halaman tambah negara ,tapi kalau tidak programnya akan menambah negeri itu ke tabel negara

-tombol tambah bencana bekerja seperti tombol tambah negara tetapi menambah filter tahun dan id negara

-grafik yang ditampilkan dibuat dengan menggunakan library chartjs dan info dari tabel sql terfilter
