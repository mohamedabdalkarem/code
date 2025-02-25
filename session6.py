# -------------------------
# -- Function And Return --
# -------------------------
# [1] A Function is A Reusable Block Of Code Do A Task
# [2] A Function Run When You Call It
# [3] A Function Accept Element To Deal With Called [Parameters]
# [4] A Function Can Do The Task Without Returning Data
# [5] A Function Can Return Data After Job is Finished
# [6] A Function Create To Prevent DRY
# [7] A Function Accept Elements When You Call It Called [Arguments]
# [8] There's A Built-In Functions and User Defined Functions
# [9] A Function Is For All Team and All Apps
# ----------------------------------------

def function_name():

  return "Hello Python From Inside Function"

dataFromFunction = function_name()

print(dataFromFunction)
# ---------------------------------------
# -- Function Parameters And Arguments --
# ---------------------------------------

a, b, c = "Osama", "Ahmed", "Sayed"

print(f"Hello {a}")
print(f"Hello {b}")
print(f"Hello {c}")

# def                     => Function Keyword [Define]
# say_hello()             => Function Name
# name                    => Parameter
# print(f"Hello {name}")  => Task
# say_hello("Ahmed")      => Ahmed is The Argument

def say_hello(n):

  print(f"Hello {n}")

say_hello(a)
say_hello(b)
say_hello(c)

def addition(n1, n2):

  print(n1 + n2)

addition(100, 300)
addition(-50, 100)


def addition(n1, n2):

  if type(n1) != int or type(n2) != int:

    print("Only Integers Allowed")

  else:

    print(n1 + n2)

addition(100, 500)

def full_name(first, middle, last):

  print(f"Hello {first.strip().capitalize()} {middle.upper():.1s} {last.capitalize()}")

full_name("   mohammed   ", 'abdelkareem', "adbellah")
# ---------------------------------
# -- Function Default Parameters --
# ---------------------------------

def say_hello(name="Unknown", age="Unknown", country="Unknown"):

  print(f"Hello {name} Your Age is {age} and Your Country Is {country}")

say_hello("mohammed", 36, "Egypt")
say_hello("Mahmoud", 28, "KSA")
say_hello("Sameh", 38)
say_hello("Ramy")
say_hello()
# --------------------
# -- Function Scope --
# --------------------

x = 1  # Global Scope

def one():

  global x

  x = 2

  print(f"Print Variable From Function Scope {x}")

def two():

  x = 10

  print(f"Print Variable From Function Scope {x}")

one()
print(f"Print Variable From Global Scope {x}")
two()
print(f"Print Variable From Global Scope After One Function Is Called {x}")
