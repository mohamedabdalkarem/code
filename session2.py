#variables

# 1 Can Start With (a-z A-Z) Or Underscore
# 2 You Cannot start With Num Or Special Characters
# 3 Can Include (0-9) Or Underscore
# 4 Cannot Include Special Characters
# 5 Name is Not Like name [ Case Sensitive ]
# 6 Cannot Use Reserved Words
# --------------------------------------

name = "mohammed abdalkareem"    #  Normal
myName = "mohammed abdelkareem"  #  camelCase
my_name = "mohammed abdelkareem" #  snake_case

print(name)
print(myName)
print(my_name)

print(help("keywords"))  # To Show All Reserved Words

#data types

print(type(10))  # int => Integer
print(type(100))  # int => Integer
print(type(-50))  # int => Integer

print(type(100.9))  # float => Floating Point Number
print(type(1.950950))  # float => Floating Point Number
print(type(-100.9595))  # float => Floating Point Number

print(type("Hello Python"))  # str => String

# Escape Sequences Characters

# \b => Back Space
# \newline => Escape New Line + \
# \\ => Escape Back Slash
# \' => Escape Single Quotes
# \" => Escape Double Quotes
# \n => Line Feed
# \t => Horizontal Tab

#concatentation

first_name= "mohammed"
second_name = "abdalkareem"
print(first_name + " " + second_name)

full_name = first_name + " " + second_name
print(full_name)

#--------------------------------------

#string
Single_Quote= 'This is Single Quote'
Double_Quotes = "This is Double Quotes"

print(Single_Quote)
print(Double_Quotes)

str1 ='mohammed abdalkareem"eng"'
str2 ="mohammed abdalkareem'eng'"

print(str1)
print(str2)

# Strings Indexing & Slicing

# 1 Every Element Has Its Own Index
# 2 Python Use Zero Based Indexing ( Index Start From Zero )
# 3 Use Square Brackets To Access Element


# Indexing ( Access Single Item )

str = "makkeny"

print(str[0])  # Index 0 = M
print(str[6])  # Index 6 = y

print(str[-1])  # Index -1 = First Character From End
print(str[-6])  # Index -6 = 6th Character From End

# Slicing ( Access Multiple Sequence Items )
# [Start:End] End Not Included
# [Start:End:Steps]

print(str[2:4])  # kk

print(str[:10])  # If Start Is Not Here Will Start From 
print(str[3:])  # If End Is Not Here Will Go To The End 
print(str[:])  # Full Data

print(str[0::1])  # Full Data

print(str[::2]) #make two steps
print(str[::3]) #make three steps
 
 