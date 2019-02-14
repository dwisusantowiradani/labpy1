#belajar labpy1
Langkah Program Cara Menentukan Bilangan Terbesar Dari 3 Bilangan

Diketahui 3 buah bilangan bil1,bil2,bil3, akan dicari nilai yang terbesar.

    Mulai
    Inisiasi bil1,bil2,bil3 sebagai integer.
    Baca bil1.
    Baca bil2.
    Baca bil3.
    Jika bil1 > bil2 dan bil1 > bil3 maka kerjakan langkah 8, selain itu
    Jika bil2 > bil1 dan bil2 > bil3 maka kerjakan langkah 9, selain itu kerjakan langkah 10.
    Cetak “Bilangan Terbesar Bilangan Pertama”.
    Cetak “Bilangan Terbesar Bilangan Kedua”.
    Cetak “Bilangan Terbesar Bilangan Ketiga”.
    Selesai

Contoh Program Menentukan Bilangan Terbesar Dari 3 Bilangan

#!/user/bin/python3
print ("Program Menentukan Bilangan Terbesar Dari 3 Bilangan\n")

A = int(input("Masukkan Bilangan Pertama = "))
B = int(input("Masukkan Bilangan Kedua = "))
C = int(input("Masukkan Bilangan Ketiga = "))

if A > B & A > C:
	print("\nTerbesar Bilangan Pertama = %s" % A)
elif B > C:
	print("\nTerbesar Bilangan Kedua = %s" % B)
else:
	print("\nTerbesar Bilangan Ketiga = %s" % C)

