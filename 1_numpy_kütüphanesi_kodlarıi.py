# -*- coding: utf-8 -*-


# NumPy Kütüphanesi Örnekleri

#### Kütüphaneyi içe aktarma
"""

import numpy as np

"""#### Numpy dizileri ve python listeleri"""

liste=[1,5,7,10,15,20,22,30]
np_liste=np.array(liste)
print("liste verileri ",liste,"\n veri tipi",type(liste))
print("numpy liste verileri ",np_liste,"\n veri tipi",type(np_liste))

"""####Listeden numpy dizisi oluşturma"""

sayilar=np.array([1,5,7,10,15,20,22,30])
print("sayilar ",sayilar,"\n veri tipi",type(sayilar))

"""#### Numpy dizilerine istenen verilere erişme"""

print("ilk sayı=",sayilar[0])
print("ikinci sayı=",sayilar[1])
print("son sayı=",sayilar[-1])

print("tüm sayılar=",sayilar[:])
print("ilk iki sayı=",sayilar[0:2])
print("iki dört arası sayılar=",sayilar[1:4])
print("üçten sona kadar olan sayılar =",sayilar[2:])
yarisi=int(len(sayilar)/2)
print("ilk yarısı",sayilar[:yarisi])
print("diğer yarısı",sayilar[yarisi:])

"""Numpy dizileri üretme"""

np.arange(10)

np.arange(10,20)

np.arange(20,50,2)

np.zeros(5)

np.zeros((5,5))

np.ones(5)

np.ones(5)*10

np.ones((3,5))

np.linspace(0,10,20)

np.eye(4) # birim matris

"""Rasgele sayı üretme"""

np.random.rand(5)

np.random.rand(4,3)

np.random.randn(10) # normal dağılıma göre rasgele sayı üretme

np.random.randn(6,6) # normal dağılıma göre 2 boyutlu rasgele sayı üretme

np.random.randint(1,50) # 1(dahil) ile 50 (dahil değil) arası ragele  bir sayı üretme

sayilar=np.random.randint(1,100,10) # 1(dahil) ile 100 (dahil değil) arası ragele  10 sayı üretme
print("sayilar dizisi eleman sayısı           =",sayilar.size)
print("sayilar dizisini şekli                 =",sayilar.shape)
print("sayilar dizinin en büyük değeri        =",sayilar.max())
print("sayilar dizinin en küçük değeri        =",sayilar.min())
print("sayilar dizisi en büyük değerin konumu =",sayilar.argmax())
print("sayilar dizisi en küçük değerin konumu =",sayilar.argmin())

"""Numpy dizisinin boyutunu değiştirme"""

print(sayilar.size)
sayilar.reshape(5,2) # 5 satır ve 2 sütun

# referans yoluya veri alınca orjinal kopyada değişim olur
yeni_sayilar=np.random.randint(1,250,50)
print(yeni_sayilar)
yarisi=yeni_sayilar[:10]
print(yarisi)
yarisi[:]=50
print(yarisi)
print(yeni_sayilar)

# copy yoluya veri alınca orjinal kopyada değişim olmaz
yeni_sayilar=np.random.randint(1,250,50)
print(yeni_sayilar)
yarisi=yeni_sayilar[:10]
yeni_yarisi=yarisi.copy()
print(yeni_yarisi)
yeni_yarisi[:]=50
print(yeni_yarisi)
print(yeni_sayilar)

ornek_sayilar=np.random.randint(1,250,20).reshape(5,4)
ornek_sayilar

"""Çok boyutlu dizilerde seçim işlemi"""

print("ilk satır",ornek_sayilar[0])
print("ilk değer",ornek_sayilar[0][0])
print("son değer",ornek_sayilar[4][3])
print("son değer",ornek_sayilar[-1][-1])

print("ilk değer",ornek_sayilar[0,0])
print("son değer",ornek_sayilar[4,3])
print("son değer",ornek_sayilar[-1,-1])
print("son değer\n",ornek_sayilar[1:3,1:3])

"""Koşula bağlı seçim işlemleri"""

#Koşul kontrolü 10 dan büyük sayılar
ornek_sayilar> 10

#Koşul kontrolü 30 dan küçük sayılar
ornek_sayilar< 30

#Koşullu seçim 10 dan büyük sayılar
ornek_sayilar[ornek_sayilar> 10]

#Koşullu seçim 30 dan küçük sayılar
ornek_sayilar[ornek_sayilar< 30]

#Koşullu seçim 30 dan küçük ve 10 dan büyük sayılar parantez önemli!!
ornek_sayilar[(ornek_sayilar< 30) & (ornek_sayilar> 10)]

"""Numpy dizilerinde işlemler"""

yeni_sayilar=np.random.randint(1,50,15)
yeni_sayilar

print("Sayılar=",yeni_sayilar)
print("Toplam= ",yeni_sayilar+yeni_sayilar)
print("Fark= ",yeni_sayilar-yeni_sayilar)
print("Çarpım= ",yeni_sayilar*yeni_sayilar)
print("Bölme= ",yeni_sayilar/yeni_sayilar)
print("Bölümünden kalan= ",yeni_sayilar%yeni_sayilar)

print("Sayılar=",yeni_sayilar)
print("50 fazlası= ",yeni_sayilar+50)
print("50 eksiği= ",yeni_sayilar-50)
print("2 katı= ",yeni_sayilar*2)
print("yarısı= ",yeni_sayilar/2)

yeni_sayilar*yeni_sayilar

print("Sayılar=",yeni_sayilar)
print("Sinüs değerleri=",np.sin(yeni_sayilar))
print("Kosinüs değerleri=",np.cos(yeni_sayilar))
print("Tanjant değerleri=",np.tan(yeni_sayilar))
print("Logaritmik değerleri=",np.log(yeni_sayilar))
