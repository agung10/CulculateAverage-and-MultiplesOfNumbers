# SOAL 1 - Menghitung rata-rata
# Tuliskan program untuk Soal 1 di bawah ini
print(5 * "\t", "Menghitung rata-rata")

bil_1 = eval(input("\nMasukan bilangan pertama : "))
bil_2 = eval(input("Masukan bilangan kedua   : "))
bil_3 = eval(input("Masukan bilangan ketiga  : "))

hasil = (bil_1 + bil_2 + bil_3) / 3

print("Rata-rata bilangan", bil_1, ",", bil_2, ", dan", bil_3, "adalah", hasil)

print("\n")
# SOAL 2 - Menulis kelipatan bilangan
# Tuliskan program untuk Soal 2 di bawah ini
print(4 * "\t", "Menulis kelipatan bilangan")

bil_bulat = eval(input("\nMasukan sebuah bilangan bulat : "))
kelipatan = eval(input("Masukkan banyak kelipatan : "))

for i in range(kelipatan):
  i += 1
  if (i == kelipatan):
    print((bil_bulat * i), end="")
    continue
  print("{}---".format(bil_bulat * i), end="")
