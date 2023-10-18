"""nama : Ridho Mauliddani
   NIM  : 220511101
   kelas: TIF22E/R5"""

print("mencari rumus balok")

#variabel
panjang_balok = int(input("masukkan panjang balok"))
lebar_balok = int(input("masukkan lebar balok"))
tinggi_balok = int(input("masukkan tinggi balok"))

#rumus balok
luas_balok = 2 * (panjang_balok * tinggi_balok) + (panjang_balok * lebar_balok) + (lebar_balok * tinggi_balok)
volume_balok = panjang_balok * lebar_balok * tinggi_balok

#output
print(" luas balok:", luas_balok)
print("volume balok :", volume_balok)