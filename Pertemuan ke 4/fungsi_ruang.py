import math
def l_limass(luas_segitiga, luas_alas):
    l=  round (luas_alas + luas_segitiga)
    return l

def v_limass(tinggi_segitiga,tinggi_limas,luas_alas):
    volume_limass=round (1/2 * (1/2 * luas_alas * tinggi_segitiga) * tinggi_limas)
    return volume_limass

def Luaskubus ( sisi ):
    lkubus = round (6 * sisi **2)
    return lkubus 

def Volumekubus (sisi) :
    vkubus =  round (sisi **3)
    return vkubus

def lbalok (panjang, tinggi, lebar,) :
    luasbalok = round (2 * (panjang * lebar + panjang * tinggi + lebar * tinggi))
    return luasbalok
def vbalok(panjang,lebar,tinggi):
    volumebalok = round (panjang * lebar * tinggi)
    return volumebalok

def l_bola(jari_jari):
    luas_bola = round (4 * math.pi * jari_jari)
    return luas_bola

def v_bola(jari_jari):
     volume_bola =round (4/3 * math.pi * jari_jari)
     return volume_bola

def luas_lse(luas_alas,luas_sisi):
    luas_limassegiempat = round (luas_alas + luas_sisi)
    return luas_limassegiempat

def volume_lse(luas_alas, tinggi):
    volume_limassegiempat = round (1/3 * luas_alas * tinggi)
    return volume_limassegiempat

def l_tabung(jari_jari, tinggi):
    luas_tabung = round ( (2 * math.pi * jari_jari) * jari_jari + tinggi)
    return luas_tabung

def v_tabung(jari_jari,tinggi):
    volume_tabung = round(math.pi * jari_jari * 2 * tinggi)
    return volume_tabung

def l_kerucut(jari_jari,tinggi):
    luas_kerucut =round(math.pi * jari_jari * (jari_jari + math.sqrt(jari_jari * 2 +tinggi * 2)))
    return luas_kerucut

def v_kerucut(jari_jari):
    volume_kerucut = round(4/3 * math.pi * jari_jari)
    return volume_kerucut

def l_prisma(Alas_segitiga,Tinggi_alas,tinggi_prisma):
    luas_prisma =2 * (math.pi * Alas_segitiga * Tinggi_alas + Alas_segitiga * tinggi_prisma + math.pi * Alas_segitiga * Tinggi_alas)
    return luas_prisma

def v_prisma(Alas_segitiga,Tinggi_alas,tinggi_prisma):
    volume_prisma = round(math.pi * Alas_segitiga * Tinggi_alas * tinggi_prisma)
    return volume_prisma