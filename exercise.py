import numpy as np
# # Boolean indekslash
#
ab = '\n\n'
# names = np.array(['ali','vali','aziz','laziz','elyor','jasur'])
# print(names)
# data = np.random.randn(6,4)
# print(data)
# tr = names=='jasur'
# print(tr)
# d_j = data[names =='ali',2:],data[names=='vali',2:]
# print(d_j[0],'\n',d_j[1])
#
# d_ = data[~(names !='jasur'),:1] #Bu ham teng emas belgisi hissoblanadi ~
# print(d_)
#
# d_ = data[~(names !='jasur'),:2],data[~(names !='elyor'),:2]
#
# mask = (names == 'jasur') | (names == 'elyor') # bu yerda | bu belgi or vazifasini bajaradi
# print(mask)
#
# mask = (names == 'jasur') | (names == 'elyor') | (names== 'ali') #bu bir nechta elementni kesib olish uchun usul
# print(mask)
# print(data,ab)
# dat = data[mask,2:]
#
# print(dat)
#
# # Manfiy elementlarni o'zgartirish
# print(data,ab)
# data[data<0] = 0
# print(data)
#
# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr)
# print(arr[2,0:2])
#
# ar = np.array([0, 2, 3, 7, 5])
# print(ar)
# print(ar[ar>3])
#
# import numpy as np
#
# # Boolean slice
#
# names = np.array(['Hasan', 'Husan', 'Javohir', 'Elyor', 'Hasan', 'Javohir', 'Elyor'])
# data = np.array([[5, 6, 1, 1],
#                  [9, 1, 1, 1],
#                  [7, 7, 4, 2],
#                  [1, 5, 1, 9],
#                  [9, 9, 4, 5],
#                  [7, 5, 9, 6],
#                  [5, 3, 7, 4]])
#
# mask = (names == 'Javohir') | (names == 'Elyor')
# print(mask)
# two_names = data[mask]
# print(two_names)

# b = list(range(10))
# for s in b:
#     print(s)
#     b.append(s)

# float_range

# def float_range(start,stop,step=0.0):
#     royxat = []
#     while start <= stop:
#         if step > 0:
#             royxat.append(start)
#             start = start + step
#         else:
#             royxat.append(start)
#             start = start+1
#     for r in royxat:
#         print(r)
# print(float_range(1,70,5.8))


#Chiziqli Algebra| Transpose & Swapaxes haqida

# a = np.arange(8).reshape(4,2)
# print(a)
# a = a.T
# print('Transposega misol',ab,a) #Bu yerda uznasiga turgan o'q vertikalga o'zgardi
#
# a = a.swapaxes(0,1)
#
# print(ab,' Swapaxesga misol',ab, a) #Bu yerda esa vertikal o'qni yana gorizontalga o'zgartirildi
#
# #dot bu bir massivni ikkinvhi massivga ko'paytirishga ishlatiladi
#
# a = np.dot(a , a.T) #Gorizontal Transposani Vertikalga ko'paytmasi
# print(a)


# Universal Funksiyalar | Unary turi

#Unary bu parametr sifatida bitta massiv qabul qila oladigon funksiya tushuniladi

# arr = np.arange(20)
# arr = arr.reshape(4,5)
# print(arr)
# sq = np.sqrt(arr)
# print(sq)
#
# # kvadratga oshirish
# square = np.square(arr)
# print(square)
#
# eksp = np.exp(arr)
# print(eksp)
#
# #Logorifm E asosga ko'ra massivning logorifimini qaytarqadi
#
# log = np.log(arr[1:])
# print(log)
#
# # modf bu qoldiqni va butun sonni ajratadi
#
# qoldiq,butun = np.modf(log)
# print(qoldiq,ab,butun)
# butun = np.array(butun)
# print(butun)

# sign bu funksiya massivning elementlari musbat yoki manfiyligi haqida ishora beradi "1 - Musbat" -1 Manfiy
rand = np.random.randn(6)
# rand = np.array(rand).reshape(3,2)
# print(rand)
# sig = np.sign(rand)
# print(sig.T)

# floor

# fl = np.floor(rand)
# # print(fl)
#
# max = np.maximum(rand,fl)
# print(max)

# where taqqoslash operatori

# xarr = np.random.randn(4,4)
# yarr = np.random.randn(4,4)
# print(xarr,ab,ab,yarr)
# cond = [True,False,False,True]
# result = np.where(cond,xarr,yarr) #Agar son == True print(yarr) else: xarr
# print(ab,result)

# print(rand)
# result = np.where(rand<0 , 5 , 7)  #wheredan keyin shartni yoziladi
# print(result)

arr1 = np.arange(6).reshape(2,3)
arr2 = np.arange(6,12).reshape(2,3)
# print(arr1,ab,arr2)
#
# print(arr2.sum(axis=0)) #bu massivni vertikal ravishda umumiy qiymatini qaytaradi
# print(arr2.sum(axis=1)) #bu massivni gorizontal ravishda umumiy qiymatini qaytaradi

# mean bu massivning o'rta qiymatini qaytaradi

# mean = np.mean(arr2) #barcha elementlarning o'rta qiymati
# print(arr2.mean())
# print(mean)

# cumsum yig'indilarni hissoblab boruvchi yig'indi

# cum = np.cumsum(arr2)
# print(arr2)
# # print(cum) #Sonlarni ketma-ket bir biriga qo'shib natijalarni chiqarib boradi
#
# cump = np.cumprod(arr1[1:]) #Bu esa sonlarni ketma-ket bir biriga ko'paytirib natijalarni chiqarib boradi
# print(arr1[1:])
# print(cump)
#
# print(arr1.max())

array = np.array([0, 1, 2, 3])
print(array.cumsum())