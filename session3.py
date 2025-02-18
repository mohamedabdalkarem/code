# ---------------------
# -- Strings Methods --
# ---------------------


# strip() rstrip() lstrip()

a = "    makkeny    "
print(a.strip())
print(a.rstrip())
print(a.lstrip())

a = "#####makkeny####"
print(a.strip("#"))
print(a.rstrip("#"))
print(a.lstrip("#"))

a = "@#@#@#makkeny@#@#@#"
print(a.strip("@#"))
print(a.rstrip("@#"))
print(a.lstrip("@#"))

# title()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.title())

# capitalize()

b = "I Love 2d Graphics and 3g Technology and python"
print(b.capitalize())


# upper()

g = "makkeny"

print(g.upper())

# lower()

h = "makkeny"

print(h.lower())

#string formatting

# firstly:old way formatting

# %s => String
# %d => Number
# %f => Float

name = "mohammed"
age = 22
gpa = 3.6

print("My Name is: " + name)
# print("My Name is: " + name + " and My Age is: " + age)  # Type Error

print("My Name is: %s" % "mohammed")
print("My Name is: %s" % name)
print("My Name is: %s and My Age is: %d" % (name, age))
print("My Name is: %s and My Age is: %d and My Rank is: %f" % (name, age, gpa))

# secondly:old way formatting

myName = "mohammed"
myAge = 22

print("My Name is : {myName} and My Age is : {myAge}")
print(f"My Name is : {myName} and My Age is : {myAge}")

# -- Arithmetic Operators --

# [+] Addition
# [-] Subtraction
# [*] Multiplication
# [/] Division
# [%] Modulus
# [**] Exponent
# [//] Floor Division

# Addition

print(10 + 30)  # 40
print(-10 + 20)  # 10

# Subtraction

print(60 - 30)  # 30
print(-30 - 20)  # -50

# Multiplication

print(10 * 3)  # 30
print(5 + 10 * 100)  # 1005
print((5 + 10) * 100)  # 1500

# Division

print(100 / 20)  # 5.0

# Modulus

print(8 % 2)  # 0
print(9 % 2)  # 1
print(22 % 5)  # 2

# Exponent

print(2 ** 5)  # 32
print(5 ** 4)  # 625

# Floor Division

print(100 // 20)  # 5
print(119 // 20)  # 5
print(142 // 20)  # 7

# -- Assignment Operators --


x = 10  # Var One
y = 20  # Var Two

x += y
x -= y

print(x)

# -----------------------------
# -- Lists --
# -----------
# 1 List Items Are Enclosed in Square Brackets
# 2 List Are Ordered, To Use Index To Access Item
# 3 List Are Mutable => Add, Delete, Edit
# 4 List Items Is Not Unique
# 5 List Can Have Different Data Types
# -----------------------------

myAwesomeList = ["One", "Two", "One", 1, 100.5, True]

print(myAwesomeList)  # Whole List
print(myAwesomeList[1])  # "Two"
print(myAwesomeList[-1])  # True
print(myAwesomeList[-3])  # 1

print(myAwesomeList[1:4])  # ['Two', 'One', 1]
print(myAwesomeList[:4])  # ['One', 'Two', 'One', 1]
print(myAwesomeList[1:])  # ['Two', 'One', 1, 100.5, True]

print(myAwesomeList[::1])  # ['One', 'Two', 'One', 1, 100.5, True]
print(myAwesomeList[::2])  # ['One', 'One', 100.5]

print(myAwesomeList)
# myAwesomeList[1] = 2
# myAwesomeList[-1] = False
myAwesomeList[0:3] = ["A"]
print(myAwesomeList)

# -------------------
# -- Lists Methods --
# -------------------

# append()

myFriends = ["mohammed", "Ahmed", "Sayed"]
myOldFriends = ["ibrahim", "khaled", "Ali"]

myFriends.append("Alaa")
myFriends.append(100)
myFriends.append(150.200)
myFriends.append(True)
myFriends.append(myOldFriends)

print(myFriends)
print(myFriends[2])
print(myFriends[6])
print(myFriends[7])
print(myFriends[7][2])

# extend()

a = [1, 2, 3, 4]
b = ["A", "B", "C"]
c = ["One", "Two"]

a.extend(b)
a.extend(c)

print(a)

# remove()

x = [1, 2, 3, 4, 5, "mohammed", True, "mohammed", "mohammed"]
x.remove("mohammed")
print(x)

# sort()

y = [1, 2, 100, 120, -10, 17, 29]
# y = ["A", "Z", "C"]
y.sort(reverse=True)
print(y)

# reverse()

z = [10, 1, 9, 80, 100, "mohammed", 100]
z.reverse()
print(z)
