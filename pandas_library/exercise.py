import pandas as pd
import numpy as np
from pandas import Series

obyekt = Series([29.1,35,41,52,6])
# print(obyekt)
# print(obyekt.values) #faqat elementlarni o'zini chiqarish

obyekt_index = Series([12,23,1,3],index=['a','b','c','d']) #Bu usul bilan indekslarni o'zimiz kiritishimiz mumkin

# qiymatlarga indeks orqli murojat qilish

ind = obyekt_index[['a','b']] #Bu yerda ro'yxat ichida yana bir ro'yxat qilib keyin indekslar berilyapti
# print(ind)

# Filterlash

filt = obyekt[25>obyekt] # Bu yerda faqatgina 25 dan yuqori qiymatlarni so'radik
# print(filt)
# print(obyekt+2) # Arifmetik amallarni bajarishimiz ham mumkin

cars_dic = {'Malibu': 9000,'BMW':5000,'Sonata':4000} #Tayyor lug'atlarni ham indeks va elementga ajratish mumkin
cars = Series(cars_dic)
cara1 = Series({'Malibu': 9000, 'BMW': 5000, 'Sonata': 4000}) # yoki shunchaki lug'at kiritsak ham bo'ladi
# print(cars['BMW'])

models = ['Honda','Malibu','Sonata','Jaguar','BMW','Tesla','Tesla']
cars1 = Series({'Malibu': 9000, 'BMW': 5000, 'Sonata': 4000},index=models) # Indeks tartibini kiritish
cars1[['Honda','Jaguar']] = 4500,5100 #yuqorida ro'yxatda mavjud bo'lmagan elementlarga qiymat berish
# print(cars1)

# Methods of Pandas

# print(cars1.isnull()) #Bu yerda qiymat bor yo'qligini True False yordamida aniqlab beradi
# print(cars1.notnull()) # Bu ham yuqoridagi bilan bi rhil,farqi qiymati NaN bo'lsa False else True
# print(cars1+cars) # To'g'ri keluvchi elementlar ustida arifmetik amallar ham bajarish mumkin

cars1.name = 'Avtolar' # name parametri yordamida obyektga nom berish ham mumkin

cars1.index.name = 'Modellar: ' # Bu yerda esa Indekslarga nom berilmoqda
# print(cars1)

# print(cars1.hasnans) #NaN qiymat bor yo'qligini umumiy tekshirish
# print(cars1.is_unique) #Takroriy qiymatlar bor yo'qligini tekshirish
# print(cars1.iloc[4]) ## ma'lumotlarga indeks tartib raqami bo'yicha murojaat qilish
# print(cars1.unique()) # Ma'lumotlarni takrrolanishsiz qiymatini chiqaradi
# print(cars1.min(),cara1.max()) # Eng kichik va katta qiymatlarni qaytaradi
# print(cars1.mean()) # Elementlarning o'rta qiymati
# print(cars1.where(cars1>0,7000)) # where bu huddi if operatori kabi. agar cars1 elemnti 0 bo'lsa 7000 qiymat berildi
# print(cars1.mask(cars1>0,7000)) # mask() Bu where operatorini teskarisi

# empty = pd.Series(0)
#
# print(empty)

# Data Frame ma'lumot turi







