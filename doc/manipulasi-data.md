#Konversi antara Tipe Data

Anda pun dapat melakukan konversi antar tipe data dengan menggunakan beberapa fungsi yang tersedia pada Python. Fungsi merupakan blok kode yang dapat dipanggil untuk melakukan tugas tertentu. Beberapa fungsi yang dapat digunakan untuk mengonversi tipe data pada Python sebagai berikut.

    Konversi integer ke float: float().
    Konversi float ke integer: int().
    Konversi dari-dan-ke string: str(), float(), int().


##Transformasi Angka, Karakter, dan String

Khusus tipe data string, terdapat berbagai fungsi untuk mentransformasikan tipe data string menjadi bentuk lain. Beberapa di antaranya berikut.

    Mengubah Huruf Besar/Kecil
    Mengubah string menjadi UPPERCASE atau lowercase.
        upper()
        lower()

    Awalan dan Akhiran
    Menghapus karakter whitespace pada suatu string.
        rstrip()
        lstrip()
        strip()
        startswith()
        endswith()

    Memisah dan Menggabung String
    Fungsi-fungsi untuk memisahkan dan menggabungkan string.
        join()
        split()

    Mengganti Elemen String
    Metode yang bertujuan untuk mengganti elemen string dengan elemen string lainnya.
        replace()

    Pengecekan String
    Fungsi-fungsi yang bertujuan untuk melakukan pengecekan pada string dan mengembalikan nilai Boolean.
        isupper()
        islower()
        isalpha()
        isalnum()
        isdecimal()
        isspace()
        istitle()

    Formatting pada String
    Fungsi-fungsi untuk pemformatan string.
        zfill()
        rjust()
        ljust()
        center()

    String Literals
    String literals adalah serangkaian karakter yang diapit oleh tanda kutip baik tunggal (') maupun ganda (").

    String dapat ditulis mudah dalam Python dengan cara diapit oleh tanda petik tunggal. Namun, dalam kondisi tertentu, dibutuhkan petik tunggal di tengah string (misalnya struktur kepemilikan dalam Bahasa Inggris—Dicoding's Cat atau penyebutan Jum'at pada hari dalam bahasa Indonesia).

    Solusinya adalah menggunakan escape character yang memungkinkan Anda untuk menggunakan karakter yang sebelumnya tidak bisa dimasukkan dalam string. Umumnya diawali dengan backslash (\) dan diikuti karakter tertentu yang diinginkan. Beberapa contoh escape charactersebagai berikut.
        \' Single quote
        \" Double quote
        \t Tab
        \n Newline (line break)
        \\ Backslash

    Raw String
    Merupakan cara untuk mencetak string sesuai dengan apa pun input atau teks yang diberikan. Umumnya digunakan untuk regex atau beberapa implementasi lain yang sangat bergantung pada keberadaan backslash. Untuk mengimplementasikan raw strings, sisipkan huruf r sebelum pembuka string.

        print(r'Dicoding\tIndonesia')
         
        """
        Output:
        Dicoding\tIndonesia
        """


##Operasi pada List, Set, dan String

Ada beberapa fungsi untuk melakukan operasi pada list, set, dan string. Berikut beberapa di antaranya.

    len()
    Fungsi yang bertujuan untuk menghitung panjang atau banyaknya elemen dari list, set, dan string.

        contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]
         
        print(contoh_list)
        print(len(contoh_list))
         
        """
        Output:
        [1, 3, 3, 5, 5, 5, 7, 7, 9]
         
        9
        """

    min() dan max()
    Fungsi yang digunakan untuk mengetahui nilai minimum dan maksimum dari suatu list.

        angka = [13, 7, 24, 5, 96, 84, 71, 11, 38]
        print(min(angka))
        print(max(angka))
         
        """
        Output:
        5
        96
        """

    count()
    Fungsi yang digunakan untuk mengetahui berapa kali suatu objek muncul dalam list.

        genap = [2, 4, 4, 6, 6, 6, 8, 10, 10]
        print(genap.count(6))
         
         
        """
        Output:
        3
        """

    In dan Not In
    In dan not in merupakan operator yang diperuntukkan untuk mengetahui nilai atau objek yang ada dalam list. Anda bisa menggunakan operator ini untuk memastikan suatu nilai ada dalam list bahkan dalam string. Operatori in dan not inakan mengembalikan nilai boolean True atau False.

        kalimat = "Belajar Python di Dicoding sangat menyenangkan"
        print('Dicoding' in kalimat)
        print('tidak' in kalimat)
        print('Dicoding' not in kalimat)
        print('tidak' not in kalimat)
         
        """
        Output:
        True
        False
        False
        True
        """

    Memberikan Nilai untuk Multiple Variable
    Anda dapat memberikan nilai untuk multiple variable dengan cara berikut.

        data = ['shirt', 'white', 'L']
        apparel, color, size = data
         
        print(data)
         
        """
        Output:
        ['shirt', 'white', 'L']
        """

    sort()
    Fungsi sort() digunakan untuk mengurutkan angka atau huruf. Berikut contoh implementasinya.

    kendaraan = ['motor', 'mobil', 'helikopter', 'pesawat']
    kendaraan.sort()
     
    print(kendaraan)
     
    """
    Output:
     ['helikopter', 'mobil', 'motor', 'pesawat']
    """