import numpy as np


# ar = np.arange(21)
# np.save('ar',ar)
# arr = np.load('ar.npy')
# ar2 = np.arange(0,21,2)
# print(ar2)
# a = ar2[2:6]
# a[:] = 0
# print(ar2)


# 3d massivlarni indekslash

# arr3d = np.array([[[1,2,3],
#                    [4,5,6],
#                    [7,8,9]],
#
#                 [[10,11,12],
#                  [13,14,15],
#                  [16,17,18]],
#
#                 [[19,20,21],
#                  [22,23,24],
#                  [25,26,27]]])
# print(arr3d)
# print(arr3d.size,' \n \n' ,arr3d.ndim)
# print(arr3d.shape)
# # print('\n',arr3d[2][0:,0]) #nolinchi qator va nolinchi ustun elemntlari
# print('\n',arr3d[2,0:,0:])

# Boolean indekslash

ab = '\n'
# names = np.array(['ali','vali','aziz','laziz','elyor','jasur'])
# print(names)
# data = np.random.randn(6,4)
# print(data)
# tr = names=='jasur'
# print(tr)
# d_j = data[names =='ali',2:],data[names=='vali',2:]
# print(d_j[0],'\n',d_j[1])

# d_ = data[~(names !='jasur'),:1] #Bu ham teng emas belgisi hissoblanadi ~
# print(d_)

# d_ = data[~(names !='jasur'),:2],data[~(names !='elyor'),:2]

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

# arr = np.array([[1, 2, 3], [4, 5, 6], [7, 8, 9]])
# print(arr)
# print(arr[2,0:2])

# ar = np.array([0, 2, 3, 7, 5])
# print(ar)
# print(ar[ar>3])

import numpy as np

# Boolean slice

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

def load_data(file_name):
    """Har bir faylni yuklab ularni ikkita mos massivga ajratuvchi funksiyani tuzish """
    # YOUR CODE HERE
    arr = np.load(file_name)
    arr1 = arr['models'],arr['qnts']
    return arr1
# print(load_data('gm_2020.npz'))
# print(load_data('gm_2021.npz'))
def total_qnts():
    """Ma'lumotlardan foydalanib, 2020 va 2021 yillarda ishlab chiqarilgan jami avtomobillar sonini hisoblaydigan
    funksiya yaratish."""
    data1 = load_data('gm_2020.npz') # ma'lumotlar (2020)
    data2 = load_data('gm_2021.npz') # ma'lumotlar (2021)
    # YOUR CODE HERE
    total = data1[1].sum(),data2[1].sum()
    return total

# print(total_qnts())

def sel_models():
    """Faqatgina Damas, Nexia, Cobalt, va Gentra rusumli avtomabillarni 2020 va 2021 yillarda qancha ishlab chiqarilganini
    barcha ma'lumotlardan ajratib olish"""
    data1 = load_data('gm_2020.npz') # ma'lumotlar (2020)
    data2 = load_data('gm_2021.npz') # ma'lumotlar (2021)
    # YOUR CODE HERE
    models = data1[0],data2[0]
    years = data1[1],data2[1]
    mask = (models[0] == 'Damas') | (models[0] == 'Nexia') | (models[0] == 'Cobalt') | (models[0] == 'Gentra')
    output = years[0][mask],years[1][mask]
    return output
# print(ab,sel_models())

data1 = load_data('gm_2020.npz') # ma'lumotlar (2020)
data2 = load_data('gm_2021.npz') # ma'lumotlar (2021)
# models = data1[0],data2[0]
# years = data1[1],data2[1]
# mask = (models[0] == 'Damas') | (models[0] == 'Nexia') | (models[0] == 'Cobalt') | (models[0] == 'Gentra')
# output = years[0][mask],years[1][mask]
# print(output)
# print(models)
# print(years)
total_cars = np.sum(data1[1])
arr = data1[1]/total_cars*100 # Bu yerda har bir mashinaning umumiy qiymatdagi foizini hissoblash formulasi.
# print(arr)

def ratio_sel_models():
    """Ba'zi avtomabillarning ishlab chiqarish hajmi, jami ishlab chiqarilgan avtomabillar hajmining qanday
    foizini egallashini hisoblash funksiyasi"""
    # YOUR CODE HERE
    models = data1[0], data2[0]
    mask = (models[0] == 'Damas') | (models[0] == 'Nexia') | (models[0] == 'Cobalt') | (models[0] == 'Gentra')
    sum = data1[1].sum(),data2[1].sum()
    percent = data1[1] / sum[0] * 100,data2[1] / sum[1] * 100
    output = percent[0][mask],percent[1][mask]
    return output
# print(ratio_sel_models())