"""nama : Ridho Mauliddani
NIM  : 220511101
kelas: TIF22E/R5"""

print("mencari prisma segitiga")

#variabel
Alas_segitiga = float(input(" masukan alas segitiga"))
Tinggi_segitiga = float (input("masukan Tinggi segitiga"))
tinggi_prisma = float(input("masukan tinggi prisma"))  

#rumus prisma segitiga
Luas_segitiga = (1/2) * Alas_segitiga * Tinggi_segitiga
Luas_prisma = (2 * Alas_segitiga * Tinggi_segitiga) + (3 * Alas_segitiga * tinggi_prisma)
volume_prisma = Luas_segitiga * tinggi_prisma

#output
print("Luas prisma :", Luas_prisma)
print("volume prisma:", volume_prisma)