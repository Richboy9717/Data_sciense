import numpy as np
import pandas as pd
from pandas import DataFrame as df
# dic = {'Yil': [2021,2020,2019,2018,2017,2016,2015,2010],
#         'Aholi soni': [35,34.5,34,33.9,33,32.8,31.9,30],
#        'Temp ': [1.54,1.48,1.56,1.5,1.44,1.50,1.45,1.33]}
# dt = df(dic)
# print(dt.head(4)) #.head() yordamida biz uchun kerakli bo'lgan ro'yxatnigina qabul qilish mumkin
# print(dt.shape)

# dt.columns = ['Aholi soni','Yil','Temp'] # Ma'lumotlarni ustunlari tartibini almashtirishimiz ham mumkin
                                        # Yoki yangi ma'lumot yaratayotganda kiritish mumkin-->
# change_sort = df({'Yil': [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2010],
#                   'Aholi soni': [35, 34.5, 34, 33.9, 33, 32.8, 31.9, 30],
#                   'Temp': [1.54, 1.48, 1.56, 1.5, 1.44, 1.50, 1.45, 1.33]},columns=['Yil','Aholi soni','Temp'])
# print(change_sort)

# indekslash ham numpy bilan bir hil
indeks_df = df({'Yil': [2021, 2020, 2019, 2018, 2017, 2016, 2015, 2010],
                  'Aholi soni': [35, 34.5, 34, 33.9, 33, 32.8, 31.9, 30],
                  'Temp': [1.54, 1.48, 1.56, 1.5, 1.44, 1.50, 1.45, 1.33]},columns=['Aholi soni','Yil','Temp','YAIM'] ,index=[4,5,6,7,8,9,10,11])
# print(indeks_df)

# Ustunlarga murojat qilish
# print(indeks_df.Temp) # Agar ustunning nomi python o'zgaruvchisi bilan bir hil qoidalar asosida yozilgan bo'lsa . bilan murojat qila olamiz
# print(indeks_df['Aholi soni']) # Aks holda lug'atga murojat qilgandek murojat qilamiz va u Series turiga o'zgaradi

# Default qiymat berish
# print(indeks_df)
indeks_df.YAIM = 0 # Bu yerda YAIM ustuni uchun 0 default qiymat berildi,bu yerga ro'yxat bersak ham bo'laadi
# print(indeks_df)

#Series yordamida aynan biz uchun kerakli qatorni o'zinigina almashtirishimiz ham mumkin
change = pd.Series([500,800,1200],index=[11,9,8])
indeks_df.Yil[8,9,11]= change
# print(indeks_df)

# Yangi ustun qo'shish
# indeks_df['Test'] = 0 # Test ustuni yaaratildi va qiymatiga 0 berildi
indeks_df.YAIM = [1500,1400,1350,1300,1250,1100,1100,1000]
indeks_df['1200 dan yuqori'] = indeks_df.YAIM > 1200 #1200 dan yuqori qiymatni yangi ustunga true false qilibberadi
# print(indeks_df)

# Keraksiz ustunni del yordamida o'chirish mumkin
# del indeks_df['Temp'] #Temp ustunini o'chirdik
# print(indeks_df)
indeks_df['head'] = 0
# print(indeks_df)
