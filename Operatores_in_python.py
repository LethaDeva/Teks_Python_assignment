# Arithemitic operators (+,-,*,/,%,**)

a = 4
b = 4

print(a  + b)
print(a  - b)
print(a  * b)
print(a  / b)
print(a  % b) # it finds the remainder between operands
print(a  ** b)

# relational operators (==,!=,>,<,<=,>=)

a = 50
b = 20

print(a == b )
print(a != b )
print(a > b )
print(a < b )
print(a >= b )
print(a <= b )

# assignment operator (=,+=,-=,*=,/=,%=,**=)

num = 20

num += 10

print(num)

num = 20

num -= 10
print(num)

num = 20

num *= 10
print(num)

num = 20

num /= 10
print(num)

num = 20

num % 5
print(num)

num = 20

num **= 10
print(num)

# logical operator (not,And,or)

# not

a = 50
b = 30

print(not False)
print(not (a < b))

# And

val1 = True
val2 = False

print( "and operator : ", val1 and val2) # it shows true while both the values are true.

print( "or operator : ", val1 or val2) # if atlest is tere is one true it shows the truth only.



# identity operator 

num_x= 89
num_y= 56

print(num_x is num_y)
print(num_x is not num_y)


#input in python it prints the values always a string

name = input("enter your name: ")
print("welcome",name)


#int (input()) it stores the integer values

number = int(input("enter your number"))

print("your number is here",number)

print(type(number),number)



name = input("enter your name: ")
age = int(input("enter your age:"))
marks = float(input("enter your marks: "))

print ("welcome", name)
print("age = ",age)
print("marks = ",marks)


