"""nama : Ridho Mauliddani
NIM  : 220511101
kelas: TIF22E/R5"""

print("mencari rumus limas segiempat")

# variabel
luas_alas = float(input("masukkan luas alas"))
luas_sisi = float(input("masukkan luas sisi"))
tinggi_limas = float(input("masukkan tingi limas"))

# rumus
luas_permukaan = luas_alas + luas_sisi
volume = 1/3 * luas_alas * tinggi_limas

#output
print("luas permukaan :", luas_permukaan)
print("volume : ", volume)