# #conditional statements in python
# # if we have two conditions we prefer to use if-else statement
# # if we have 3 or more statements we prefer to use if-elif-else statement


# if-else statement 
# finding positive and negative numbers

num = int(input("Enter the number: "))

if num >0:
    print("it is a positiv number",num)
else:
    print("it is a negative number")


#if-elif-else()
# finding the maximum nuber amoung 3 numbers

a = int(input("enter the first number"))
b = int(input("enter the secound number"))
c = int(input("enter the third number"))


if(a >= b and a >= c):
    print("firts number is maximum: ", a)
elif(b >= c):
    print("secound number is maximum: ", b)
else:
    print("third number is naximum:", c)


# finding the minimum number amound 4 numbers

D  = int(input("Enter the first number"))
E  = int(input("Enter the secound number"))
F  = int(input("Enter the third number"))
G  = int(input("Enter the fourth number"))

if(D <= E and D <=F):
    print("first number is  the minimum: ",D)
elif(E <= F and E <= G):
    print("secouund number is  the minimum: ",E)
elif(F <= G):
    print("third number is  the minimum: ",F)
else:
    print("fourth number is  the minimum: ",G)



# traffic signal 

light = "black"

if(light == "red"):
    print("stop")
elif(light == "green"):
    print("go")
elif(light == "yellow"):
    print("look")
else:
    print("broken")


# students grading system

marks = int (input("enter the marks"))

if(marks >= 90 and marks <= 100):
    grade = "A"
elif(marks >= 80 and marks < 90 ):
    grade = "B"
elif(marks >= 70 and marks < 80):
    grade = "C"
elif(marks >=50 and marks < 50):
    grade = "D"
else:
    grade = "F"

print ("grade of the student ->",grade)




# finding odd and even numbers

num = int (input("enter the number :"))



if(num % 2 == 0):
    print("even")
else:
    print("odd")


