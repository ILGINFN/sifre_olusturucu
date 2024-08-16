karakterler  ="+-/*!&$#?=@<>abcdefghijklnopqrstuvwxyzABCDEFGHIJKLMNOPQRSTUVWXYZ1234567890"

import random

adet = int(input("Kaç karakterli bir şifre istiyorsun?\n"))
hesap = input("Hangi hesabın için şifre oluşturmak istiyorsun?\n")

def sifre_olustur(sayi):
    sifre = ""
    for i in range(sayi):
        sifre += random.choice(karakterler)

    return sifre

with open("sifrelerim.txt", "a") as doc:
    sifre = sifre_olustur(adet)
    doc.write(f"{hesap} : {sifre}\n")

print(sifre)