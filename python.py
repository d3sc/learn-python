# var = input("masukan!")

# if(var) : 
#     print(var.strip())
    
    
# age = 17;
# salary = 5000000.0;
# # float salary = 5000000;

# print(type(age))
# print(type(salary))

#* list
# x = ["laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone"]
# x[1] = "upil"

# print(x);

#* tupple
# tupple type tidak support penambahan item, seperti const
# x = ("laptop", "monitor", "mouse", "mousepad", "keyboard", "webcam", "microphone")
# x[1] = "upil"

# print(x);

#* set
# set tidak memiliki index pada setiap urutan item nya, dan bersifat unik
# set1 = {1, 2, 3, 4, 5}
# set2 = {4, 5, 6, 7, 8}

# union digunakan untuk menggabungkan kedua set.
# union = set1.union(set2)
# print("Union:", union)

# intercestion digunakan untuk mengiris kedua set
# intersection = set1.intersection(set2)
# print("Intersection:", intersection)


#* dictionary
x = {"nama": "ikbar", "umur": 17 }
# menambah data di dictionary
x ["kelas"] = "xiiRPL"
# menghapus data di dictionary
del x["kelas"]
# mengubah data di dictionary
x ["kelas"] = "xiiMM"

# memberikan f didepan sebelum tanda kutip "", dan kita bisa menggunakan template literals
# print(f"helo {x['nama']}")

# memberikan f didepan sebelum tanda kutip "", dan kita bisa menggunakan template literals
# print(f"helo {x['nama']}")
# print(f"{x}")

# data_diri = {"firstName": "ikbar", "lastName": "rabbani", "age": 17, "isMarried": False}

# menggabung string
# print('-'.join(['Dicoding','Indonesia', '!']))

# print('Dicoding Indonesia !'.split())

# teks = '1'
# tambah_number = teks.zfill(2)
# print(tambah_number)

contoh_list = [1, 3, 3, 5, 5, 5, 7, 7, 9]

# contoh_list.

# x = 'Dicoding'
# x[0] = 'F'
# print("halo \n" * 100)
# print(2 ** 3)

# print(1 != 2 or "tests" == "test")
# print(1 != 2 and "tests" == "test")


#* if and else statement
# ketersediaan = "Daging ayam"

# if ketersediaan == "Daging ayam":
#     print("Ibu membeli dan memasak ayam")
# else:
#     print("Ibu membeli dan memasak tempe")

# 1 line if else
# if x : print("helow")
# else : print("ow men")

#* elif statement
nilai = 65

# if nilai>=80:
#    print("Selamat! Anda mendapat nilai A")
#    print("Pertahankan!")
# elif nilai>=70:
#    print("Hore! Anda mendapat nilai B")
#    print("Tingkatkan!")
# elif nilai>=60:
#    print("Hmm.. Anda mendapat nilai C")
#    print("Ayo semangat!")
# else:
#    print("Waduh, Anda mendapat nilai D")
#    print("Yuk belajar lebih giat lagi!")

#* Ternary opt
# lulus = True
# print("selamat") if lulus else print("perbaiki")

#* Ternary tuples opt
# lulus = False
# kelulusan = ("kasian", "wow selamat!")[lulus]

# print(kelulusan)

#* for array
# var_list = [1,2,3,4,5,6,7,8,9,10]
# for i in var_list:
#     print(i)

#* normal for loop
# range(start, stop, step)
# for i in range(1, 10, 2) :
#     print(i)


#* while loop 
# counter = 1

# while counter <= 5 :
#     print(counter);
#     counter+=1 # Increment 

#* for nested
# for i in range(1, 3):
#     for j in range(1, 3):
#         print(i,j)
        
#* Break
# Break statement adalah pernyataan untuk menghentikan perulangan dan kemudian program akan otomatis keluar dari perulangan tersebut,
# lalu dilanjutkan dengan mengeksekusi blok perulangan selanjutnya.
# for huruf in 'Dico ding':
#     # ketika pengulangan sampai pada huruf space maka akan di hentikan 
#     if huruf == ' ':
#         break
#     print('Huruf saat ini: {}'.format(huruf))
    
#* Continue
# for huruf in 'Dico ding':
#     # ketika pengulangan sampai pada huruf space maka akan tetap dilanjutkan 
#     if huruf == ' ':
#         continue
#     print('Huruf saat ini: {}'.format(huruf))

#* Pass
# Pass statement adalah pernyataan yang digunakan jika Anda menginginkan sebuah pernyataan atau blok pernyataan (statement),
# tetapi tidak ada tindakan atau program tidak melakukan apa pun.
# x = 10

# if x > 5:
#     pass
# else:
#     print("Nilai x tidak memenuhi kondisi")

#* list comprehension
# angka = [1, 2, 3, 4]
# pangkat = []
# for n in angka:
#     # membuat semua nilai yang ada pada list akan di pangkatkan 2,
#     # lalu dimasukkan kedalam var pangkat yang berisi list kosong.
#   pangkat.append(n**2)
# print(pangkat)

#* Cara kedua list comprehension
# angka = [1, 2, 3, 4]
# # [ekspresi for var in iterable]
# # atau [ekspresi for_loop_one_or_more_condition]
# pangkat = [n**2 for n in angka]
# print(pangkat)

# evenNumber = []
# for i in range(0,501, 2) :
#     evenNumber.append(i)

# print(evenNumber)

# for i in range(1, 3):    
#     for j in range(1, 3):    
#         print(i,j)

print("helo")