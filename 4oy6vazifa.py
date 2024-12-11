from collections import namedtuple
#
# talabalar = [
#
#     {"name":"Halil","age":23,"major":3},
#     {"name":"Javoxir","age":20,"major":4},
#     {"name":"Jalil","age":19,"major":2},
# ]
#
# talaba = namedtuple("talaba",['name','age','major'])
#
# for user in talabalar:
#     person = talaba(**user)
#     print(f"name: {person.name} age: {person.age} major: {person.major}")

# -------------------------------------------------------------
#2-misol

# products = [
#     ("apple","30$","good"),
#     ("pear","30$","good"),
#     ("banana","10$","good"),
#     ("cherry","40$","good"),
#     ("peach","20$","good")
# ]
#
# fruits = namedtuple("fruits",['product_name','price','quantity'])
#
# for i in products:
#     fruit = fruits(*i)
#     print(f"product_name: {fruit.product_name} price: {fruit.price} quantity: {fruit.quantity} ")

# -------------------------------------------------------------
# 3-misol

# citys = [
#     ("Toshkent","Uzbekistan","38 mln"),
#     ("Moskva","Rossiya","144 mln"),
#     ("Parij","Fansiya","66mln")
# ]
#
# city = namedtuple("city",['city_name','country','population'])
# for i in citys:
#     scity = city(*i)
#     print(f"city_name: {scity.city_name}, country: {scity.country}, population: {scity.population} ")


# -------------------------------------------------------------
# 4-misol







# -------------------------------------------------------------
# 5-misol
# def xayr():
#     def inner(name):
#         return f"Xayr {name}"
#     return inner
#
# hello = xayr()
# print(hello("Ali"))
#
#

# -------------------------------------------------------------


# 6-misol
# def salom():
#     def inner(name):
#         return f"Assalomu alaykum {name}"
#     return inner
#
# hello = salom()
# print(hello("Ali"))


# -------------------------------------------------------------
# 7-misol

# def qoshish():
#     def inner(son):
#         return son+5
#     return inner
#
# a = qoshish()
# print(a(11))

# -------------------------------------------------------------
# 8-misol


# def qoshish():
#     c = 0
#     def inner(son):
#         nonlocal c
#         c+=1
#         return son+c
#     return inner
#
# a = qoshish()
# print(a(11))
# print(a(11))
# print(a(11))
#

# -------------------------------------------------------------
# 9-misol

# def qoshish():
#     def inner(son):
#         return son**2
#     return inner
#
# a = qoshish()
# print(a(72))
#

# -------------------------------------------------------------
# 10-misol
# def  plus_name():
#     x = []
#     def inner(name):
#         nonlocal x
#         x.append(name)
#         return x
#     return inner
#
# ss = plus_name()
# print(ss("Abrorjon"))
# print(ss("Ali"))
# print(ss("Jalil"))

# -------------------------------------------------------------
# 11-misol

# def chegirma(narx:int):
#     def inner(chegirma:int ):
#         return narx-(narx * chegirma /100)
#     return inner
#
# a = chegirma(123)
# print(a(30))



# -------------------------------------------------------------
# 12-misol
# def mahsulot():
#     def inner(mahsulot):
#         return mahsulot*10
#     return inner
# aa=mahsulot()
# print(aa("aaaa"))
#

# -------------------------------------------------------------
# 13-misol

# def plus_str():
#     ii = ""
#     def inner(word:str):
#        return ii + word
#
#     return inner
#
#
# soz = plus_str()
# print(soz("Alik"))
# print(soz("Salom"))

# -------------------------------------------------------------
# 14-misol








# -------------------------------------------------------------
# 15-misol

# def qoshish(son):
#     def inner(daraja):
#         return son**daraja
#     return inner
#
# a = qoshish(2)
# print(a(6))
#

# -------------------------------------------------------------
# 16-misol
# def string():
#     def inner(letter):
#         return letter[::-1]
#     return inner
#
# a = string()
# print(a("Salom"))

# -------------------------------------------------------------
# 17-misol

# def shopping():
#     products = []
#     all_price = 0
#     def inner(product,price):
#         nonlocal products
#         nonlocal all_price
#         products.append(product)
#         all_price += price
#         return f"Umumiy {all_price} so'm bo'ldi"
#     return inner
#
# a = shopping()
# print(a("olma",1000))
# print(a("shaftoli",2000))

# -------------------------------------------------------------
# 18-misol

# def products():
#     p = {}
#     def inner(product,price):
#         p[f"{product}"] = price
#         return p
#     return inner
#
# ss = products()
# print(ss("olma",1000))















