#Definisi Subprogram

Subprogram adalah serangkaian instruksi dirancang untuk melakukan operasi yang sering digunakan dalam suatu program. Subprogram yang sering digunakan terdiri dari dua jenis, yakni berikut.

    Fungsi
    Fungsi adalah blok kode yang dapat menerima input, melakukan pemrosesan, dan mengembalikan output. Hasil atau output tersebut dinyatakan dalam sebuah tipe data yang eksplisit, artinya fungsi yang dibuat dapat ditentukan untuk mengembalikan tipe data integer, string, atau lainnya.

    Prosedur
    Prosedur adalah deretan instruksi yang jelas keadaan awal (initial state) dan keadaan akhirnya (final state). Prosedur mirip dengan program secara umum, tetapi memiliki cakupan yang kecil dan terbatas.


##Fungsi

Fungsi dalam pemrograman sebenarnya didasari oleh konsep pemetaan (asosiasi) dan fungsi dalam matematika. Fungsi pada matematika merupakan pemetaan antara dua himpunan nilai, yaitu domain dan range. Kita bisa bayangkan fungsi sebagai sebuah mesin yang memiliki input (domain) dan output (range). Output tersebut pasti terkait dengan input, bagaimana pun kondisinya. Berikut adalah notasi fungsi yang sering dijumpai dalam matematika.

dos:e12261591d74d0acf1c54aa1a31d582a20230821203939.jpeg

Dari gambar tersebut, f merupakan nama fungsi, x adalah input, dan 2x adalah hal yang harus dikeluarkan oleh fungsi tersebut (output).

Dalam pemrograman, fungsi dapat diumpamakan seperti merakit isi black box. 

dos:8576acb9b71e7f93ae1177285ecbc7d420230821203902.jpeg

Selayaknya black box, kita tidak perlu tahu tentang hal yang terjadi di dalam kotak (fungsi) tersebut. Kita hanya perlu fokus pada keadaan awal yang merupakan himpunan nilai yang terdefinisi sebagai input (domain) dan keadaan akhir yang merupakan himpunan nilai yang terdefinisi sebagai output (range).

##Fungsi terbagi menjadi dua jenis, yakni berikut.

    Built-in Functions
    Built-in functions atau dalam bahasa Indonesia berarti fungsi bawaan adalah kumpulan fungsi yang sudah terintegrasi dengan bahasa pemrograman Python sehingga tidak perlu mengimpor modul atau library tambahan. Fungsi bawaan ini menyediakan fungsi-fungsi inti dan merupakan dasar dari bahasa Python. Contoh dari fungsi bawaan adalah print(), len(), type(), range(), dan sebagainya.

    User-defined Functions
    User-defined functions atau dalam bahasa Indonesia berarti fungsi yang didefinisikan pengguna adalah jenis fungsi yang kita definisikan sendiri untuk melakukan tugas spesifik tertentu. Contoh dari user-defined functions adalah fungsi yang telah kita buat di awal materi ini tentang mencari luas persegi panjang. 

Namun, jika Anda ingin menggunakan fungsi di luar built-in functions, Anda bisa mengimpor sebuah library. Library adalah koleksi banyaknya modul yang saling terkait dan dapat digunakan berulang kali. Library dalam Python terbagi menjadi dua jenis, yakni berikut.

    Python Standard Library
    Python Standard Library adalah jenis library yang telah terpasang secara otomatis ketika Anda melakukan instalasi Python. Python Standard Library berisi kumpulan modul dan paket yang disertakan secara default oleh Python. Paket (package) merupakan sebuah direktori yang berisi satu atau lebih modul yang terkait dan saling berhubungan.

    External Library
    Jika sebelumnya impor library tidak perlu dilakukan untuk Python Standard, berbeda halnya dengan external library yang mengharuskan Anda mengimpor library untuk bisa menggunakannya. External Library adalah jenis library yang dikembangkan oleh individu atau organisasi di luar tim inti pengembang Python.

Keterkaitan antara fungsi, modul, package, dan library dapat dilihat pada tabel berikut.
Nama	Definisi	Contoh

##Fungsi
	

Blok kode yang dapat digunakan kembali untuk mengeksekusi fungsionalitas tertentu saat dipanggil.
	

print(), len(), mencari_luas_persegi_panjang()

###Built-in functions
	

Kumpulan fungsi yang sudah terintegrasi dengan bahasa pemrograman Python sehingga tidak perlu mengimpor modul atau library tambahan.
	

print(), len(), range()

###User-defined functions
	

Jenis fungsi yang kita definisikan sendiri untuk melakukan tugas spesifik tertentu.
	

mencari_luas_persegi_panjang()

###Modul
	

File berisi kode Python berupa fungsi, kelas, dan sebagainya.
	

Math, dan semua file yang kita buat sendiri dengan ekstensi ".py" (main.py, var.py, dan sebagainya)

###Package
	

Sebuah direktori berisi satu atau lebih modul yang terkait dan saling berhubungan.
	

NumPy, Pandas

###Library
	

Koleksi dari banyaknya modul dan paket yang saling terkait dan dapat digunakan berulang kali.
	

Matplotlib, TensorFlow, Beautiful Soup

Untuk membuat fungsi sendiri (user-defined functions) dalam Python, kita dapat membuatnya dengan mengikuti struktur berikut.

dos:538ce2a3e67cd3e40bc0ca47c37cc88c20230821203914.jpeg

Fungsi di atas memiliki beberapa elemen yang dapat diikuti, yakni berikut.

    Def: Keyword dari Python untuk membuat fungsi.
    Nama fungsi: Nama yang Anda deklarasikan untuk fungsi yang akan dibuat.
    Parameter fungsi: Variabel yang digunakan untuk menyimpan nilai dari argumen.
    Setiap fungsi harus diakhiri dengan titik dua ":" untuk menandakan awal blok kode fungsi. 
    Setelah titik dua ":", di bawahnya kita mendefinisikan blok kode yang ingin dieksekusi.
    Terakhir, kita menggunakan return keyword yang merupakan bagian dari return statement. Return statement bertujuan untuk mengembalikan nilai atau hasil eksekusi fungsi tersebut. 

Untuk memanggil fungsi yang telah dibuat tersebut, kita dapat mengikuti struktur di bawah ini.

dos:1c3f6d8c6dfca2083faf6553cbd7581020230821203936.jpeg

Dengan catatan sebagai berikut.

    Nama fungsi, tentu Anda harus menyebutkan nama fungsi yang ingin digunakan. Namun ingat, gunakan kurung tutup "()" untuk memanggilnya.
    Argumen bisa dikatakan sebagai nilai yang diberikan kepada fungsi. Nantinya, nilai tersebut akan disimpan dalam parameter fungsi.

Terakhir, untuk membuat fungsi lebih mudah dipahami oleh programmer lain, kita bisa membuat dokumentasi berupa docstring. Docstring merupakan akronim dari documentation string, bertujuan untuk membuat dokumentasi terhadap fungsi yang dibuat. Umumnya, dokumentasi yang dijelaskan berupa argumen, return, deskripsi fungsi, dan sebagainya.

Contohnya sebagai berikut.

def mencari_luas_persegi_panjang(panjang,lebar):
    """
    Fungsi ini digunakan untuk menghitung luas persegi panjang.

    Args:
        panjang (int): Panjang persegi panjang.
        lebar (int): Lebar persegi panjang.

    Returns:
        int: Luas persegi panjang hasil perhitungan.
    """

    luas_persegi_panjang = panjang*lebar
    return luas_persegi_panjang

persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)
print(persegi_panjang_pertama)

Pada kode di atas, kita mendefinisikan docstring dengan memberikan blok komentar dengan tiga double quote (""") tepat di bawah "def" keyword. Elemen yang kita masukkan dalam docstring tersebut adalah deskripsi untuk menjelaskan tujuan fungsi yang dibuat, argumen untuk menjelaskan argumen yang dapat diterima oleh fungsi tersebut, dan return untuk menjelaskan nilai yang akan dikembalikan oleh fungsi.

Argumen dan parameter pada fungsi memiliki beragam jenisnya. Secara umum, berikut adalah jenis-jenis dari argumen dan parameter.

    Keyword Argument
    Keyword Argument adalah jenis argumen yang disertai dengan nama parameter (identifier) dan secara eksplisit disebutkan.

    def mencari_luas_persegi_panjang(panjang,lebar):
        luas_persegi_panjang = panjang*lebar
        return luas_persegi_panjang

    persegi_panjang_pertama = mencari_luas_persegi_panjang(panjang=5, lebar=10)

    Positional Argument
    Kebalikan dari keyword adalah positional, artinya Anda tidak menyebutkan nama parameter (identifier) secara eksplisit.

    def mencari_luas_persegi_panjang(panjang,lebar):
        luas_persegi_panjang = panjang*lebar
        return luas_persegi_panjang

    persegi_panjang_pertama = mencari_luas_persegi_panjang(5,10)

    Positional-or-Keyword
    Jenis ini adalah parameter default dalam Python. Dengan jenis ini, kita dapat menggunakan positional maupun keyword argument ketika memanggil fungsi.

    def greeting(nama, pesan):
        return "Halo, " + nama + "! " + pesan

    print(greeting("Dicoding", "Selamat pagi!"))
    print(greeting(pesan="Selamat sore!", nama="Dicoding"))

    Positional-Only
    Parameter ini hanya dapat dimanfaatkan menggunakan jenis argumen posisi saat pemanggilan fungsi. Parameter ini ditentukan menggunakan sintaks "/".

    def penjumlahan(a, b, /):
        return a + b

    print(penjumlahan(8, 50))

    Keyword-Only
    Parameter ini kebalikan dari yang sebelumnya. Kita harus menggunakan keyword argument untuk memanggil fungsi dengan jenis parameter ini. Parameter ini ditentukan dengan sintaks "*" (asterisk).

    def greeting(*, nama, pesan):
        return "Halo, " + nama + "! " + pesan

    print(greeting(pesan="Selamat sore!",nama="Dicoding"))

    Var-Positional
    Parameter ini menampung jumlah argumen posisi yang bervariasi saat pemanggilan fungsi. Parameter ini ditentukan dengan menggunakan sintaks *args.

    def hitung_total(*args):
        print(type(args))
        total = sum(args)
        return total

    print(hitung_total(1, 2, 3))

    Var-Keyword
    Parameter ini dapat menampung jumlah keyword argument yang bervariasi saat pemanggilan fungsi. Parameter ini ditentukan dengan menggunakan sintaks **kwargs yang berperan sebagai dictionary (seperti tipe datanya). Argumen pada pemanggil fungsi akan berperan sebagai value dan parameter (identifier) berperan sebagai key.

    def cetak_info(**kwargs):
        info = ""
        for key, value in kwargs.items():
            info += key + ': ' + value + ", "
        return info

    print(cetak_info(nama="Dicoding", usia="17", pekerjaan="Python Programmer"))

Selain fungsi yang didefinisikan menggunakan def keyword, kita juga bisa membuat versi one-liner dari fungsi tersebut. Konsep ini disebut dengan fungsi anonim atau juga dikenal sebagai lambda expression. Keterkaitan antara fungsi menggunakan def keyword dengan fungsi anonim dapat dilihat pada gambar bergerak (GIF) berikut. 

dos:7fd93423ab923a121ee43e1e92eb606320230821204813.gif

Nama fungsi (func) setara dengan nama variabel yang digunakan untuk menyimpan ekspresi lambda, args adalah argumen yang kita butuhkan untuk dioperasikan, dan ret_val merupakan nilai yang kita kembalikan (return).

Terakhir, kita dapat mengimpor file berisi fungsi dari satu file ke file yang lain. Hal ini karena setiap file berekstensi .py yang kita buat, dikenal juga sebagai modul oleh Python. Untuk mengimpor fungsi yang diinginkan dari file yang telah ditentukan, Anda hanya perlu menggunakan pernyataan impor. Misalnya, jika Anda memiliki fungsi dalam file hello.py yang ingin diimpor ke file utama bernama main.py, gunakan kode berikut dalam main.py.

import hello 

Anda juga bisa mengimpor kode, seperti fungsi, kelas, hingga variabel secara spesifik. Misalnya Anda ingin mengimpor fungsi “mencari_luas_persegi_panjang” dan variabel “nama” dari modul hello. Gunakan kode di bawah ini.

from hello import mencari_luas_persegi_panjang, nama 


##Prosedur

Dalam KBBI, kata prosedur memiliki makna sebagai tahap kegiatan untuk menyelesaikan suatu aktivitas. Hal ini sama seperti prosedur sebagai subprogram yang merupakan pengelompokan instruksi-instruksi yang sering dipakai dalam program. 

Berbeda dengan fungsi, prosedur tidak mengharuskan adanya parameter input atau output dan dapat dipandang sebagai fungsi yang tidak menghasilkan nilai. Dalam Python, prosedur didefinisikan dengan return tanpa ekspresi atau nilai yang dihasilkan di akhir fungsi.

dos:5d66a73b7b8f651143118bfdeb58959a20230821203900.jpeg

Secara konsep, gambar di atas merupakan kerangka dasar prosedur pada Python. Sekilas memang sangat mirip dengan fungsi, hanya saja kita tidak mendefinisikan return dan bahkan return value. 

Untuk memanggil prosedur, caranya serupa seperti Anda memanggil fungsi. Cukup mendefinisikan satu baris instruksi, seperti "greeting()". Untuk pemberian argumen dan parameter pada prosedur, kita dapat memakai cara yang sama seperti pada fungsi yang telah dijelaskan sebelumnya.

def greeting(name):
    print("Halo " + name + ", Selamat Datang!")

greeting("Dicoding Indonesia")

Anda juga bisa membuat prosedur tanpa memiliki parameter input sehingga hanya memiliki body kode saja. Contohnya, kita membuat prosedur greeting tanpa parameter name dan ia hanya akan menampilkan pesan “Halo Selamat Datang!”. 

def greeting():
    print("Halo Selamat Datang!")

greeting()