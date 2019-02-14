
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


