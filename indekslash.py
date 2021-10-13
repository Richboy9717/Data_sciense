# Numpy kutubxonasini chaqirib olish
import numpy as np

# Masala sharti : Elementlari 0 dan 9 gacha
# (9 ning o'zi massiv elementiga kirmaydi), '
# 'qadami esa 1 ga teng bo'lgan (3, 3) o'lchamli massiv yarating.

def nd_array():
    """Elementlari 0 dan 9 gacha (9 ning o'zi massiv elementiga kirmaydi), qadami esa 1 ga teng bo'lgan (3, 3) o'lchamli massiv """
    # YOUR CODE HERE
    arr = np.arange(0,9)
    arr.shape = 3,3
    return arr

# print(nd_array())

"""Funksiyani tekshirish"""
arr = nd_array() # massiv
assert arr.size == 9  # elementlar soni
assert type(arr) == np.ndarray # #numpy array

# Yuqorida yaratilgan massivning elementlari 6 va 7 ga teng bo'lgan qismini kesib olish funksiyasini tuzing.

def sliced_array_2d():
    """Yuqorida yaratilgan massivning elementlari 6 va 7 ga teng bo'lgan qismini kesib olish funksiyasi """
    # YOUR CODE HERE
    return arr[2,0:2]

# print(sliced_array_2d())

# 3-o'lchamli massivni quyidagi listdan yarating, hamda 12, 13, 15, va 16 elementlarini kesib oling.
#
def sliced_array_3d():
    """3-o'lchamli massivni yuqoridagi listdan yaratish, hamda 12, 13, 15, va 16 elementlarini kesib olish funksiyasi"""
    # YOUR CODE HERE
    arr3d = np.array([[[ 0,  1,  2],
                       [ 3,  4,  5],
                       [ 6,  7,  8]],

                      [[ 9, 10, 11],
                       [12, 13, 14],
                       [15, 16, 17]],

                      [[18, 19, 20],
                       [21, 22, 23],
                       [24, 25, 26]]])
    return arr3d[:]

# print(sliced_array_3d()[1,1:,:2])

# reshape bu tayyor arrayni massivini hamda shakli8ni o'zgartirib  beradi
# a = np.zeros((20,4)).reshape(5,4,4)
# a[3][1,2:]+=7
# print(a)

#Boolean

def boolean_slicing():
    """Boolean indekslash yordamida ma'lumotlarni kesib olish """
    # YOUR CODE HERE
    names = np.array(['Hasan', 'Husan', 'Javohir', 'Elyor', 'Hasan', 'Javohir', 'Elyor'])
    data = np.array([[5, 6, 1, 1],
                    [9, 1, 1, 1],
                    [7, 7, 4, 2],
                    [1, 5, 1, 9],
                    [9, 9, 4, 5],
                    [7, 5, 9, 6],
                    [5, 3, 7, 4]])
    mask = (names == 'Javohir') | (names == 'Elyor') |(names == 'Hasan')
    return data[mask]
# print(boolean_slicing())