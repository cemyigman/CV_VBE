import numpy
# numpy kutuphanesinin icindeki modullerin hepsini yuklemek icin kullanilir.
# Kullanim: numpy.char.lstrip(...)

import numpy as np
# numpy kutuphanesinin icindeki modullerin hepsini yuklemek icin kullanilir.
# Kullanim: np.char.lstrip(...)

from numpy import char as nc
# Sadece numpy kutuphanesindeki "char" modulunu yuklemek icin kullanilir.
# Kullanim: nc.lstrip(...)

from numpy import *
# numpy kutuphanesindeki tum moulleri cagirmak icin kullanilir. KULLANIMI ONERILMEZ !!!

help(numpy)
# Kutuphaneler ile ilgili "Yardim" bilgilerini gormek icin kullanilir.

#################
# Array kopyalama
#################
x = np.array([1, 2, 3, 4, 5, 6, 7, 8, 9, 10])
print(x)
y = np.copy(x)
print(y)

#################
# Array transpoze etme
#################
x = np.arange(9).reshape((3, 3))
print(x)
y = np.transpose(x)
print(y)

#################
# Listeyi Array haline getirme
#################
x = [1, 2, 3, 4, 5]
print("List: ", x)
y = np.asarray(x)
print("Array: ", y)

#################
# Matrix
#################
x = np.arange(4).reshape((2, 2))
print(x)
y = np.asmatrix(x)
print(y)

#################
# Array birlestirme
#################
a = np.array([[1, 2], [3, 4]])
b = np.array([[5, 6]])
c = np.concatenate((a, b), axis=0)
print("c:", c)
d = np.concatenate((a, b), axis=None)
print("f: ", d)

#################
# Metin operasyonlari
#################
# Buyuk harfe cevirme
x = np.array(['a', 'b', 'c', 'd', 'e'])
print(x)
y = np.char.capitalize(x)
print(y)
# Kucuk harfe cevirme
x = np.array(['A', 'B', 'c', 'D'])
y = np.char.lower(x)
print(y)
# Buyuk harf kucuk harf degisimi
x = np.array(['1a', '2B', '3C', '4d'])
print(x)
y = np.char.swapcase(x)
print(y)
# Ilk harfi buyuk harf yapma
x = np.array(['cem', 'can'])
print(x)
y = np.char.title(x)
print(y)
# Metin ortalama
# Bit metni etrafina belirli karakter ekleyerek ortalama
a = ['cem']
print(a)
print(np.char.center(a, 7, fillchar='_'))
# Karakter silme (Soldan. Sagdan silme icin --> rstrip)
x = ['__cem']
y = np.char.lstrip(x, '_')
print(y)
a = ["Mr. John Doe"]
b = np.char.lstrip(a, 'Mr. ')
print(b)

#################
# Yapilandirilmis Array uzerinde lstrip ornegi
#################
name = ['Dr. Cosmo Kramer', 'Mr. Bob Dylan', 'Cathy', 'Doug']
age = [25, 45, 37, 19]
weight = [55.0, 85.5, 68.0, 61.5]

x = np.zeros(4, dtype=int)
print(x)

data = np.zeros(4, dtype={'names': ('name', 'age', 'weight'), 'formats': ('U20', 'i4', 'f8')})
print(data)
print(data.dtype)

data['name'] = name
data['age'] = age
data['weight'] = weight
print(data)
print(data['name'])

# Get first row
print(data[0])

# Get name from last row
print(data[-1]['name'])
print(data[0]['name'])

y = np.char.lstrip(data[0]['name'], 'Dr. ')
print(y)

data[0]['name'] = np.char.lstrip(data[0]['name'], 'Dr. ')
print(data[0])

#################
# Karakter arama. Belirli bir karakterin index ini bulamk icin kullanilir.
x = np.array(['abcdefghijklm123456'])
y = np.array([1, 'abcdefghijklm123456', 3, 4, 'aaa'], dtype='U10')
print(x)
print(np.char.find(x, 'c', start=0, end=None))
print(np.char.find(x, 'y', start=0, end=None))

# Cesitli metin tipi kontrolleri
print(np.char.isalpha(x))
print(np.char.isalnum(x))
print(np.char.isnumeric(x))
print(np.char.isnumeric(y))

# Bir metnin belirlenen karakter/karakterlerele baslayip baslamadiginin kontrolu.
print("Does it start with?", np.char.startswith(x, 'a', start=0, end=None))

# Uzunluk
print(np.char.str_len(y))

# Array icinde mantiksal arama ve sonuca gore elemanlari degistirme

x = np.array([1, 2, 4, 8, 16, 32, 64, 128])
y = np.where(x > 32, x, x)
print(y)

xx = np.arange(10)
print(xx)
yy = np.where(xx < 5, xx, 10*xx)
print(yy)

# Sirala Arama. Siralanmis bir Array uzerinde yeni girilecek bir elemanin hangi index e gireceginin bulunmasi.
# side="left" kullanilirsa soldan, "right" kullanilirsa sagdan yakalasarak esitlik durumunda tercihe gore index belirler.
print(np.searchsorted([1,3,4,5], 2, side='left'))


# Temel betimleyici istatistikler
x = np.random.randint(1,1000,100)
print(x)
print(np.ptp(x, axis=0))
print("Median: ", np.median(x))
print("Mean: ", np.mean(x))
print("Standard Deviation", np.std(x))
print("Variance", np.var(x))
print("Standard Deviation without NaNs", np.nanstd(x))
print("Mean without NaNs", np.nanmean(x))
print("Median without NaNs", np.nanmedian(x))






