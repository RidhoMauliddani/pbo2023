"""nama : Ridho Mauliddani
NIM  : 220511101
kelas: TIF22E/R5"""

print("mencari limas segitiga")

#variabel
luas_segitiga = float(input("masukkan luas segitiga"))
luas_alas = float(input("masukkan luas alas segitiga"))
tinggi_segitiga = float(input("masukkan tinggi segitiga"))
Tinggi_limas = float(input("masukkan Tinggi limas"))

#rumus
luas_permukaan = luas_alas + luas_segitiga
volume = 1/2 * (1/2 * luas_alas * tinggi_segitiga) * Tinggi_limas
#output
print("luas permukaan :", luas_permukaan)
print("volume :", volume)


