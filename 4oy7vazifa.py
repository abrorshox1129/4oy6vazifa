from random import randint
from typing import Iterable



# class CustomIterator:
#     def __init__(self,num_list:Iterable):
#         self.__num_list = num_list
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#        for i in self.__num_list:
#            print(i)
#
#
# aaa = [1,2,3,4,5,6,7,8,9]
# a = CustomIterator(aaa)
# print(a.__next__())


# -----------------------------------------------------------------------------------
# 2-misol


from typing import Iterable
#
# users = ['Toxir','Bakir','Jalil']
#
# class CustomIterator:
#     def __init__(self,users: Iterable):
#         self.__users = users
#         self.__index = -1
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.__index +=1
#         if self.__index>=len(self.__users):
#             raise StopIteration("Element qolmadi!!")
#
#         return self.__users[self.__index]
#
#
#
# a = CustomIterator(users)
# print(next(a))
# print(next(a))
# print(next(a))

# -----------------------------------------------------------------------------------

# 3-misol
# from typing import Iterable
#
#
#
# class CustomIterator:
#     def __init__(self,users: Iterable):
#         self.__users = users
#         self.__index = len(self.__users)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         self.__index -= 1
#         return self.__users[self.__index]
#
#
# users = ['Toxir','Bakir','Jalil']
# a = CustomIterator(users)
# print(a.__next__())
# print(a.__next__())
# print(a.__next__())

# -----------------------------------------------------------------------------------
# 4-misol
# class LetterIterator:
#     def __init__(self,fayl_name:Iterable):
#         self.__fayl_name = fayl_name
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         with open(self.__fayl_name,mode="r",encoding="utf-8") as file:
#             for i in file:
#                 for m in i:
#                     for n in m:
#                         print(n)
#
#
#
# a = LetterIterator("vazifa.text")
# print(a.__next__())

# -----------------------------------------------------------------------------------
# 5-misol
# class FilterIterator:
#     def __init__(self,num_files:Iterable):
#         self.__num_files = num_files
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         for i in self.__num_files:
#             if i % 2 != 0:
#                 continue
#             else:
#                 return i
#
#
# ss = [1,2,3,4,5,6,7,8,9]
# a = FilterIterator(ss)
# print(next(a))
#


# -----------------------------------------------------------------------------------
# \6-misol
# class FilterIterator:
#     def __init__(self,num_files:Iterable):
#         self.__num_files = num_files
#
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         x = 0
#         for i in self.__num_files:
#             x+=i
#         print(x)
#
#
# ss = [1,2,3,4,5,6,7,8,9]
# a = FilterIterator(ss)
# print(next(a))
# -----------------------------------------------------------------------------------
# 7-misol

from typing import Iterable


#
# class CustomIterator:
#     def __init__(self,word,users: Iterable):
#         self.__users:list = users
#         self. word = word
#         self.__index = len(self.__users)
#
#     def __iter__(self):
#         return self
#
#     def __next__(self):
#         i = self.__users.count(self.word)
#         if i > 0:
#             return f"{self.word} topildi"
#         else:
#             print("Siz qidir so'z ro'yxatdam  mavjud emas!!!")
#
#
# users = ['Toxir','Bakir','Jalil']
# a = CustomIterator("Ali",users)
#
# print(next(a))



# -----------------------------------------------------------------------------------
#                 GENERATORS
# -----------------------------------------------------------------------------------

# 1-MISOL

# def rrange(num:int):
#     for i in range(num+1):
#         yield i
#
# print(rrange(5))
# print(list(rrange(5)))

# -----------------------------------------------------------------------------------
# 2-misol
# def uzunlik(matn:str):
#     for i in matn.split(" "):
#         yield len(i)
#
# a = "Salom dunyon hahaha haahah hshhdjas jsank"
#
# print(list(uzunlik(a)))
# for i in uzunlik(a):
#     print(i)

# -----------------------------------------------------------------------------------
# 3-misol
# num = int(input("Qaysi raqamgacha toq sonlar generatsiyasi kerak: "))
# a = (i for i in range(num) if i % 2 != 0)
# print(list(a))
# -----------------------------------------------------------------------------------
# 4-misol
# num = int(input("Qaysi raqamgacha juft sonlar generatsiyasi kerak: "))
# a = (i for i in range(num) if i % 2 == 0)
# print(list(a))
# -----------------------------------------------------------------------------------
# 5-misol

# def cheksiz():
#
#
#
# print(cheksiz())

# -----------------------------------------------------------------------------------
# 6-misol

# a = int(input("num: "))
# s = ((i,i**2) for i in range(a+1))
# print(dict(s))

# -----------------------------------------------------------------------------------
# 7-misol
# num = [1,2,3,4,5,6,7]
# def yigindi(num):
#     x = 0
#     for i in num:
#         x = x +i
#     yield x
#
# print(list(yigindi(num)))

# -----------------------------------------------------------------------------------
# 8-misol
"""Bu savolda ijobiy raqamlarni sorashgan ekan men bularni musbat son deb oyladim shuning ucun musbat sonlarni filtr qildim!!!!!"""
# def numfiltr(list):
#     for i in list:
#         if i < 0:
#             continue
#         else:
#             yield i
#
# nums = [1,2,-5,-3,-2,3,4,5,-7,-3,-5]
# print(list(numfiltr(nums)))

# -----------------------------------------------------------------------------------
# 9-savol
# import random
# def randomm():
#     for i in range(1):
#         a = randint(1,99999)
#         yield a
#
# for i in randomm():
#     print(i)

# -----------------------------------------------------------------------------------
# 10-misol







# -----------------------------------------------------------------------------------

# 11-misol
# def letter(matn:str):
#     for i in matn.split(" "):
#         yield i[::-1]
#
# a = "salom dunyo alik dunyo"
#
# print(list(letter(a)))

# -----------------------------------------------------------------------------------
# 12-misol

# def solve(num:int):
#     s = 1
#     for i in range(num+1)[1::]:
#         s*=i
#     yield s
#
# print(list(solve(5)))











