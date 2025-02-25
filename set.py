# set is a collection of unique elements
# set is unordered
# set does not allows duplicates
# set is mutsble

# a = {1,2,3,4,5}
# b = {"apple","graps","bananna","orange"}
# c = {True, 3.2, 7 , "car", False}


# removing dublictes from list[]

# list = [1,2,2,5,6,6]
# list = set ([1,2,2,5,6,6]) 
# print(list)


# removing dublictes from string ""
# str = "deva","deva","ravi","shyam","raghu"
# str = set (("deva","deva","ravi","shyam","raghu"))
# print(str)


# removing dublictes from tuple()

# tup = (12,"deva","deva",210.2,"radha")
# tup = set((12,"deva","deva",210.2,"radha",))
# print(tup)


# indexing in set's

# tup = {1,2,3,3,5,36,55}
# print(tup.add(25))
# print(tup)


# removing elements from set using

# tup = {23,"deva",225.3,"deva","raghu"}
# print(tup.remove("deva"))
# print(tup)


# discard is also nothing but remove

# tup = {23,"deva",225.3,"deva","raghu"}
# print(tup.discard("raghu"))
# print(tup)


# 4 diffrent types of operations witch present in set's
# 1 is union
# 2 is intersection
# 3 is difference
# 4 is symemtric_difference


# union of A and B
# it delets the dublicats and prints the output

# tup1 = {25,36,55,22,56,25}
# tup2 = {33,568,569,78,22}
# print(tup1.union(tup2))

# using symbolic representation

# tup1 = {25,36,55,22,56,25}
# tup2 = {33,568,569,78,22}
# print(tup1 | tup2)


# intersection of A and B

tup1 = {25,36,55,22,56,25}
tup2 = {33,568,569,78,22,36,25}
print(tup1.intersection(tup2))


# using symbolic representation

tup1 = {25,36,55,22,56,25}
tup2 = {33,568,569,78,22,36,25}
print(tup1 & tup2)


# difference between A and B

tup1 = {1,2,3,4,5,6}
tup2 = {3,8,9,5}
print(tup1 - tup2)


# symmentric_difference

tup1 = {1,2,3,4,5,6}
tup2 = {3,8,9,5}
print(tup1 ^ tup2)
