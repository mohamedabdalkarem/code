# -----------------------------
# -- Tuple --
# -----------
# 1- Tuple Items Are Enclosed in Parentheses
# 2- You Can Remove The Parentheses If You Want
# 3- Tuple Are Ordered, To Use Index To Access Item
# 4- Tuple Are Immutable 'You Cant Add or Delete'
# 5- Tuple Items Is Not Unique
# 6- Tuple Can Have Different Data Types
# -----------------------------

# Tuple Syntax & Type Test
TupleOne = ("mohammed", "Ahmed")
TupleTwo = "mohammed", "Ahmed"

print(TupleOne)
print(TupleTwo)

print(type(TupleOne))
print(type(TupleTwo))

# Tuple Indexing

TupleThree = (1, 2, 3, 4, 5)
print(TupleThree[0])
print(TupleThree[-1])
print(TupleThree[-3])

# Tuple Assign Values

TupleFour = (1, 2, 3, 4, 5)
#TupleFour[2] = "Three"
# print(TupleFour)  # 'tuple' object does not support item assignment

# Tuple Data

TupleFive = ("mohammed", "mohammed", 1, 2, 3, 100.5, True)
print(TupleFive[1])
print(TupleFive[-1])
# -----------------------------
# -- Set --
# ---------
# 1- Set Items Are Enclosed in Curly Braces
# 2- Set Items Are Not Ordered And Not Indexed
# 3- Set Indexing and Slicing Cant Be Done
# 4- Set Has Only Immutable Data Types (Numbers, Strings, Tuples) List and Dict Are Not
# 5- Set Items Is Unique
# -----------------------------

# Not Ordered And Not Indexed

mySetOne = {"mohammed", "Ahmed", 100}
print(mySetOne)
# print(mySetOne[0])

# Slicing Cant Be Done

mySetTwo = {1, 2, 3, 4, 5, 6}
# print(mySetTwo[0:3])

# Has Only Immutable Data Types

# mySetThree = {"mohammed", 100, 100.5, True, [1, 2, 3]} # unhashable type: 'list'
mySetThree = {"mohammed", 100, 100.5, True, (1, 2, 3)}

print(mySetThree)

# Items Is Unique

mySetFour = {1, 2, "mohammed", "One", "mohammed", 1}
print(mySetFour)

# ---------------------------
# -- Dictionary --
# ----------------
# 1- Dict Items Are Enclosed in Curly Braces
# 2- Dict Items Are Contains Key : Value
# 3- Dict Key Need To Be Immutable => (Number, String, Tuple) List Not Allowed
# 4- Dict Value Can Have Any Data Types
# 5- Dict Key Need To Be Unique
# 6- Dict Is Not Ordered You Access Its Element With Key
# ----------------------------

# Dictionary

user = {
  "name": "mohammed",
  "age": 36,
  "country": "Egypt",
  "skills": ["Html", "Css", "JS"],
  "rating": 10.5
}

print(user)
print(user['country'])
print(user.get("country"))

print(user.keys())
print(user.values())

# Two-Dimensional Dictionary

languages = {
  "One": {
    "name": "Html",
    "progress": "80%"
  },
  "Two": {
    "name": "Css",
    "progress": "90%"
  },
  "Three": {
    "name": "Js",
    "progress": "90%"
  }
}

print(languages)
print(languages['One'])
print(languages['Three']['name'])

# Dictionary Length

print(len(languages))
print(len(languages["Two"]))

# Create Dictionary From Variables

frameworkOne = {
  "name": "Vuejs",
  "progress": "80%"
}

frameworkTwo = {
  "name": "ReactJs",
  "progress": "80%"
}

frameworkThree = {
  "name": "Angular",
  "progress": "80%"
}

allFramework = {
  "one": frameworkOne,
  "two": frameworkTwo,
  "three": frameworkThree
}

print(allFramework)

# -- Comparison Operators -

# Equal + Not Equal

print(100 == 100)
print(100 == 200)
print(100 == 100.00)

print("#" * 50)

print(100 != 100)
print(100 != 200)
print(100 != 100.00)

print("#" * 50)

# Greater Than + Less Than

print(100 > 100)
print(100 > 200)
print(100 > 100.00)
print(100 > 40)

print("#" * 50)

print(100 < 100)
print(100 < 200)
print(100 < 100.00)
print(100 < 40)

print("#" * 50)

# Greater Than Or Equal + Less Than Or Equal

print(100 >= 100)
print(100 >= 200)
print(100 >= 100.00)
print(100 >= 40)

print("#" * 50)

print(100 <= 100)
print(100 <= 200)
print(100 <= 100.00)
print(100 <= 40)

print("#" * 50)

# --------------------
# --  Control Flow  --
# -- If, Elif, Else --
# -- Make Decisions --
# --------------------

uName = "mohammed"
uCountry = "egypt"
cName = "Python Course"
cPrice = 100

if uCountry == "Egypt":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 80}")

elif uCountry == "KSA":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 60}")

elif uCountry == "egypt":

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 50}")

else:

  print(f"Hello {uName} Because You Are From {uCountry}")
  print(f"The Course \"{cName}\" Price Is: ${cPrice - 30}")

  