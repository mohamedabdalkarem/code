# "Child" if age is less than 12.

# "Teenager" if age is between 12 and 18.

# "Adult" if age is above 18.
age=int(input("Enter your age: "))
print("Child" if age<12 else "Teenager" if age>=12 and age<=18 else "Adult")
print("Child" if age<12 else "Teenager" if age>=12 and age<=18 else "Adult")    