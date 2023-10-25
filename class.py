#* basic class
# class Mobil:
#     # Atribut
#     warna = "Merah"
    
    
# inisialisasi class
# mobil_1 = Mobil()

# mengganti attr dari class
# mobil_1.warna = "biru"
# print(mobil_1.warna)
# tetapi attr didalam class tidak digantikan, yang tergantikan object yang sudah di inisialisasi 
# print(Mobil.warna)

# tetapi jika mengganti attr dari class nya langsung, maka dapat diubah isi attr di dalam class nya. bukan diubah di object yang sudah di inisialisasi.
# Mobil.warna = "kuning"
# jika kita mengubah value dari class seperti di atas maka kita dapat mengubah value di attr class Mobil.

#* constructor class
#! dalam python self adalah this dalam js
#* jika ada self didalam method class maupun constructor method, kita tidak bisa langsung mengakses nya tanpa menginisialisasi class nya menjadi object.
#* agar method yang memiliki self dapat dijalankan
# class Mobil:
#     def __init__(self, warna, merek, kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan
        

# mobil_1 = Mobil("merah", "upil", 160)
# # mobil_2 = Mobil()

# print(mobil_1.merek)

# mobil_1.warna = "hitam"

# print(mobil_1.warna)

#* decoration function
# def my_decorator(func):
#     def wrapper():
#         print("Sebelum fungsi dieksekusi.")
#         # isi fungsi yang sudah di dekorasi akan dijalnakan di tempat funct(), contohnya print yang ada di tempat fungsi say_hello
#         func()
#         print("Setelah fungsi dieksekusi.")
#     return wrapper

# # menambahkan @ pada awal dari nama fungsi akan membuat fungsi dekorasi dengan fungsi decorator
# @my_decorator
# def say_hello():
#     # ketika menjalankan fungsi print, dia akan dijalankan di tengah / di paramter func() didalam fungsi wrapper di dalam fungsi my_decoration
#     print("Hello, world!")

# # Memanggil fungsi yang sudah didekorasi
# say_hello()

#* class method
# class Mobil:
#     def __init__(self, warna, merek, kecepatan):
#         self.warna = warna
#         self.merek = merek
#         self.kecepatan = kecepatan

#     # ini adalah contoh method
#     def tambah_kecepatan(self):
#         self.kecepatan += 10

# mobil_1 = Mobil("Merah", "tpang", 160)
# print("Sebelum ditambahkan: ")
# print(mobil_1.kecepatan)

# mobil_1.tambah_kecepatan()        # Memanggil metode tambah_kecepatan.

# print("Setelah ditambahkan: ")
# print(mobil_1.kecepatan)

#* static method
# method static tidak terikat dengan instance class, method ini dapat dianggap seperti kita membuat function seperti biasa
# class Mobil:
#     def __init__(self, merek):
#         self.merek = merek
    
#     #* menambahkan ini di method yang ingin di jadikan static
#     #! perhatian, jika menggunakan method static. kita tidak bisa menggunakan self dalam function kita!
#     @staticmethod
#     def intro_mobil():
#         print(f"Ini adalah metode dari kelas Mobil")
        
# # kita juga bisa langsung mengakses method nya lewat class nya langsung, karena dia static.
# Mobil.intro_mobil()

# # kita juga bisa memanggilnya pada saat sudah menginisialisasi class.
# mobil_1 = Mobil("DicodingCar")
# mobil_1.intro_mobil()

#* class method
# class method memiliki parameter diawal, yang ber-output class. contohnya, kita bisa memanggil attr test pada function intro_mobil
class Mobil:
    test = "helow"
    def __init__(self, merek):
        self.merek = merek

    # menambahkan ini di method yang ingin dijadikan class method
    @classmethod
    # untuk penamaan paramter itu bebas, tetapi kita harus mengikuti peraturan dari python agar mudah dibaca oleh user lain
    def intro_mobil(cls):
        print(cls.test)
        
Mobil.intro_mobil()
mobil_1 = Mobil("DicodingCar")
mobil_1.intro_mobil()