"""nama : Ridho Mauliddani
NIM  : 220511101
kelas: TIF22E/R5"""

print("mencari tabung")
import math
#variabel
Jari_jari_tabung = 7
Tinggi_tabung = 10

#rumus tabung
luas_tabung = (2 * math.pi * Jari_jari_tabung) * Jari_jari_tabung + Tinggi_tabung
volume_tabung = math.pi * Jari_jari_tabung * 2 * Tinggi_tabung

# output
print("luas tabung:", luas_tabung)
print("volume tabung :", volume_tabung)