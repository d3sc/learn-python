#Percabangan dan Ternary Operators

##Percabangan

Dalam pemrograman, sebuah kode program dapat berjalan berdasarkan kondisi tertentu. Maknanya, Anda dapat memberikan instruksi berdasarkan "Jika-maka".

    Jika Anda tidak menyelesaikan kelas Memulai Pemrograman dengan Python, maka Anda tidak lulus dari kelas Memulai Pemrograman dengan Python.
    Jika variabel nama kurang dari dua, maka variabel tersebut tidak memenuhi kriteria kondisi.

Statement atau sintaks untuk melakukan percabangan sebagai berikut.

    If
    If adalah statement Python yang akan mengecek nilai variabel di dalamnya memenuhi kriteria suatu kondisi atau tidak. Jika memenuhi kriteria, kondisi tersebut bernilai true. Jika tidak memenuhi kriteria, kondisi akan bernilai false. Jika kondisi if bernilai true, kode yang berada dalam blok kode if akan dieksekusi.

    Struktur dari IF statement sebagai berikut.
    dos:343128e08dbe9bfee35b69caca9ada6620230808093353.jpegSebagai informasi tambahan, kita juga dapat menambahkan 'and' atau 'or' operator dalam kondisi percabangan.

    Else
    Else adalah statement yang menjadi jalan keluar saat kondisi atau hasil evaluasi if statement bernilai false. Ini maksudnya, program akan menjalani blok kode if terlebih dahulu dan jika hasilnya adalah false, program akan menjalankan else statement sebagai jalan keluar atau kondisi terakhir.

    Jika kita gabungkan if dan else, struktur berikut dihasilkan.
    dos:94ecdca01e2bb3081bcb2d76691ab74a20230808093356.jpeg

    ELIF
    Elif merupakan kependekan dari else if dan alternatif untuk if bertingkat atau switch case. Elif statement berada di posisi setelah if. Anda dapat menambahkan elif statement lebih dari satu karena tidak dibatasi dan opsional.

    Struktur keseluruhan percabangan jika kita gabungkan antara if, elif, dan else sebagai berikut.
    dos:9a11c7d66f8332389eaa11633db379b020230808093354.jpeg

##Ternary Operators

Ternary operators termasuk conditional expressions pada Python. Conditional expressions adalah bentuk ekspresi yang bertujuan untuk mengevaluasi kondisi dan mengembalikan nilai berdasarkan hasil evaluasinya. Anda bisa asumsikan bahwa ternary operators ini merupakan versi one-liner dari if dan else.

Ada 2 tipe ternary sebagai berikut.

    Ternary Operators
    Ternary jenis ini adalah jenis expression yang umum digunakan. Struktur dari ternary operators sebagai berikut.
    dos:55b5beb1f21ff93e2191973de343e08120230808093353.jpeg

    Ternary Tuples
    Jenis ternary kedua adalah jenis ternary yang menggunakan tipe data tuples.
    dos:e41b88bfa485f7e06f1d926eb3daab3f20230808093353.jpeg

##Perulangan

Perulangan adalah jenis kode program yang bertujuan untuk meningkatkan efektivitas program dalam membuat kode program berulang. Ada beberapa jenis perulangan dalam Python, yakni for, while, dan for bersarang.

For

For adalah sintaks dalam Python yang bersifat definite iteration. Definite iteration adalah sebuah proses iterasi atau perulangan yang jumlah pengulangannya ditentukan secara eksplisit sebelumnya.

Format dari perulangan for sebagai berikut.

dos:4940bd73b8ab88d8c502cd649593e24820230808093351.jpeg

<iterable> merupakan segala object dalam Python yang dapat diiterasi seperti list, tuple, hingga string. Ada pula <var> merupakan variabel yang akan mengambil elemen berikutnya dari <iterable> setiap kali iterasi berjalan.

While

While adalah sintaks dalam Python yang bersifat indefinite iteration. Indefinite iteration adalah sebuah proses iterasi yang akan berhenti ketika memenuhi kondisi tertentu.

Format dari perulangan while sebagai berikut.

dos:168cdef5465f2254ad9c446142b4696c20230808093351.jpeg

Kondisi merupakan ekspresi yang akan dievaluasi dan menghasilkan nilai true atau false. Selama hasil evaluasi bernilai true, program akan terus berjalan hingga menghasilkan nilai false.

Namun, ada kondisi yang akan menyebabkan perulangan terus berjalan tanpa henti. Kondisi ini disebut dengan infinite loop, kebalikan dari indefinite loop. Kondisi infinite loop berarti kita melakukan perulangan yang tidak pernah memenuhi kondisi yang diinginkan. Contohnya ketika kita melakukan perulangan, tetapi tidak menambahkan increment di akhir kode.

    counter = 1
    while counter <= 5:
        print(counter)

For Bersarang

Ketika Anda membuat perulangan, sering kali menemukan perulangan dalam perulangan atau disebut sebagai nested loop.

Format dari nested loop sebagai berikut.

dos:ca8ab147da674c0c625021cd773ad24320230808093351.jpeg

Anda dapat asumsikan bahwa terdapat dua perulangan, yakni "perulangan luar" dan "perulangan dalam". Program akan melakukan "perulangan luar" terlebih dahulu, lalu akan melakukan "perulangan dalam". "variabel_luar" akan mengambil nilai dari "iterable_luar" sedangkan "variabel_dalam" akan mengambil nilai dari "iterable_dalam".

Kontrol Perulangan

    Break
    Break statement adalah pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis keluar dari perulangan tersebut, lalu dilanjutkan dengan mengeksekusi blok perulangan selanjutnya.

    Jika Anda memiliki perulangan yang bertingkat seperti for bersarang, break akan menghentikan perulangan sesuai dengan tingkatan atau letak perulangannya berada.

    Continue
    Continue statement adalah pernyataan untuk membuat iterasi berhenti, kemudian melanjutkan ke iterasi berikutnya. Continue seolah mengabaikan pernyataan (statement) yang berada antara continue hingga akhir blok.

    Else setelah For
    Pada Python juga dikenal else setelah for dengan fungsinya untuk perulangan yang bersifat pencarian. Else setelah for ini bisa dikatakan sebagai memberikan jalan keluar program saat pencarian tidak ditemukan.

    Perlu diperhatikan oleh Anda, if dan else berkaitan walaupun berbeda blok. Pada else setelah for, statement else tidak akan dieksekusi saat if pernah sekali saja benar. Dengan kata lain, break dalam if harus tidak terjadi untuk memicu else setelah for.

    Else setelah While
    Berbeda dengan else setelah for, pada statement else setelah while, blok statement else akan selalu dieksekusi saat kondisi pada while menjadi salah.

    Pass
    Pass statement adalah pernyataan yang digunakan jika Anda menginginkan sebuah pernyataan atau blok pernyataan (statement), tetapi tidak ada tindakan atau program tidak melakukan apa pun.

    Statement pass digunakan dalam situasi-situasi ketika Python memerlukan adanya pernyataan, tetapi tidak memiliki tindakan yang perlu dilakukan pada saat itu. Biasanya itu adalah kondisi ketika Anda membutuhkan placeholder untuk menunjukkan bahwa tidak ada operasi yang perlu dilakukan. Hal ini dapat membantu kita mengatur struktur kode secara rapi dan memungkinkan penambahan implementasi di kemudian hari.

    List Comprehension
    List comprehension adalah cara untuk menghasilkan list baru berdasarkan list atau iterables yang telah ada sebelumnya. Sintaks dasarnya sebagai berikut.
    dos:d95d4d3ab118c3b561dfd0a60437934720230808093351.jpeg
    Catatan:
        new_list merupakan variabel yang dideklarasikan oleh Anda.
        expression merupakan ekspresi yang akan dijalankan seiring perulangan bernilai benar.
        for_loop_one_or_more_conditions merupakan perulangan for yang Anda definisikan. Contohnya adalah "for n in angka" yang ada pada contoh sebelumnya.

Penanganan Kesalahan (Error Handling and Exception Handling)

Saat Anda membuat program, sering kali menemukan setidaknya dua jenis kesalahan berdasarkan kejadiannya.

    Kesalahan sintaks (syntax errors) atau sering disebut juga sebagai kesalahan penguraian (parsing errors).
    Pengecualian (exceptions) atau sering disebut juga sebagai kesalahan saat beroperasi (runtime errors).

Kesalahan Sintaks (Syntax Errors)

Kesalahan sintaks (syntax errors) adalah jenis kesalahan yang terjadi ketika Python tidak mengerti perintah Anda. Ini mengakibatkan pesan kesalahan muncul sebelum program tersebut berjalan.

Secara umum struktur kesalahan sintaks sebagai berikut.

dos:241fef0c93cf585ea923dc11ef63ca6520230808093351.jpeg

Berikut adalah penjelasan detail satu per satu terkait poin di atas.

    "<nama file>" merupakan file Python yang Anda eksekusi. Jika Anda menggunakan mode script melalui lokal komputer dan program Anda menghasilkan Error, pesan ini akan memunculkan nama script atau file Python Anda.
    <nomor baris> merupakan nomor baris kode dalam file Anda yang mengalami kesalahan.
    <baris kode> merupakan kode yang mengalami kesalahan dalam file Anda.
    <tipe kesalahan> merupakan kelompok atau tipe kesalahan yang Anda alami, contohnya SyntaxError dan IndentationError.
    <pesan kesalahan> merupakan pesan detail kesalahan atau keterangan yang diberikan oleh program. Contohnya “invalid syntax” dan “expected an indented block”.

Pengecualian (Exceptions)

Pengecualian adalah kesalahan yang terjadi ketika Python mengerti perintah Anda, tetapi mendapatkan masalah saat mengikutinya. Umumnya, pengecualian bisa terjadi ketika aplikasi sudah mulai beroperasi.

Jenis kesalahan ini adalah kesalahan yang paling sering ditemui ketika Anda membuat kode program yang kompleks. Meskipun kode atau ekspresi dari Python yang Anda tulis sudah benar, ada kemungkinan terjadi kesalahan ketika perintah tersebut dieksekusi.

Secara umum, struktur pengecualian sama seperti kesalahan sintaksis. Namun, hal yang menjadi pembeda adalah pada struktur pengecualian memberikan pesan "traceback (most recent call last)".

dos:e18e5eb3e504662f04f4cc8ac342cdd220230808093351.jpeg

Pesan ini mengacu pada informasi yang ditampilkan ketika terjadi kesalahan atau pengecualian (exception). Pesan traceback ini menyediakan "jejak" dari kode yang dieksekusi sehingga Anda dapat melacak kembali jalur eksekusi program sebelum mencapai titik error.

Penanganan Pengecualian

Untuk menyelesaikan setiap masalah pengecualian, kita dapat membangun kode program dalam menangani hal tersebut.

Program Python yang Anda bangun dapat dilengkapi penanganan terhadap pengecualian dari tipe kesalahan yang Anda tentukan. Konsep ini dikenal dengan exceptions handling yang menggunakan pernyataan try-except untuk menangani pengecualian tersebut.

Secara keseluruhan, struktur lengkap dari penanganan pengecualian sebagai berikut.

dos:3b6fb67b0cf2d5e46eca76c9ef21a4b920230808093351.jpeg

Pada try statement, program akan menjalankan blok kode yang mungkin terjadi pengecualian. Pada except statement, program akan mengeksekusi statement ini jika terjadi pengecualian. Pada else statement, program akan mengeksekusi statement ini jika tidak terjadi pengecualian. Pada finally statement, program akan mengeksekusi statement ini setelah semua pernyataan di atas terjadi.

Raise Exception

Jika sebelumnya kita menangani kesalahan yang TIDAK DISENGAJA, kali ini kita akan mempelajari cara menangani kesalahan yang DISENGAJA. Umumnya, ketika membuat kode program kita ingin membatasi program tersebut dengan kondisi tertentu.

Perlu diingat bahwa umumnya, raise digunakan bersamaan dengan if-else statement.

Berikut adalah contoh penerapan raise statement untuk menangani kesalahan atau pengecualian yang disengaja.

    var = -1
    if var < 0:
        raise ValueError("Bilangan negatif tidak diperbolehkan")
    else:
        for i in range(var):
            print(i+1)


    """
    Traceback (most recent call last):
      File "/home/glot/main.py", line 3, in <module>
        raise ValueError("Bilangan negatif tidak diperbolehkan")
    ValueError: Bilangan negatif tidak diperbolehkan
