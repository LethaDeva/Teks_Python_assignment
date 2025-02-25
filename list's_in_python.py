# Data Type in Python

# list in python
# list is a collection of different data types

sunil = ['Sunil',34,'Mumbai',6658.35,True]
print(sunil)
print(type(sunil))
print(sunil[0])
print(sunil[1])
print(sunil[2])
print(sunil[-4])


# list slicing

shyam = [0,25,56,89,2,36,6,58,60,78]
print(shyam)
print(shyam[1:5])
print(shyam[1:5:2])
print(shyam[-7 : -5])


# update list

divya =['Divya','Hyd',78977.35,True]

divya[1] = 'Mumbai'
print(divya)

divya[2] = 78977.35 + 1000
print(divya)

divya[3] = False
print(divya)


# slicing list

# append() method it is used to add single element in the end of the list

q = [1,2,3,4,5,6,7]

q.append(8)
print(q)

q.append('Sunil')
print(q)


# extend() method is used to add multiple elements in the end of the list 

q.extend([9,10,11,12])
print(q)


# pop() method is used to remove the last element of the list

a = ['Druva','karnataka',552369.2,35,True]

a.pop()
print(a)

# len() method is used to find the length of the list

print(len(a))

print(len(q))



# count() method is used to count the numbers in list

num = [1,2,3,4,5,6,7]
akshai = ['Druva','karnataka',552369.2,35,True]

print(num.count(5))

print(akshai.count(2))

# index() method is used to find the index of the element in the list

print(num.index(5))
print(akshai.index(1))