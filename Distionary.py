# distionary is a collection of key value pairs.
# key is unique and value is not unique.
# key is used to access the value.
# key and value are separated by colon(:)
# key value pairs are separated by comma(,)

dict1 = {"name": "deva","age": 25, "location" : "chennai","salary": 30000}
dict5 = {"name": "lucky","age": 25, "location" : "chennai","salary": 30000}
print(type(dict1))

print(dict1["name"])
print(dict1["age"])
print(dict1["salary"])
print(dict1["location"])


dict2 = {3:"idly", 4:"dosa", 5:"vada", 6:"pongal", 7:"upma"}

print(dict2[3])
print(dict2[4])
print(dict2[5])
print(dict2[7])
print(dict2[6])

dict3 = {6:"vey biryani",5:"chicken biryani",4:"mutton biryani",3:"prawn biryani",2:"egg biryani"}

print(dict3[5])
print(dict3[4])
print(dict3[3])
print(dict3[2])
print(dict3[6])

# we can use get method to get the vaalue of the  key
# if the key is not available it will return none
# if the key is not available we can pass the default value as second argument
# if the key is not available it will return the default value

print(dict3.get(4))

# keys() method is used to get the keys from the dictionary

print(dict3.keys())


# values() method is used to get the values from the dictionary
# we get only values from the dictionary
# we get vales in the form of list

print(dict3.values())

# items() method is used to get the key value pairs from the dictionary
# we get key and value as a tuple

print(dict2.items())

# pop() method is used to remove the key value pair from the dictionary
# we need to pass the key as an argument

print(dict1.pop("name"))

# popitem() method is used to remove the last key value pair from the dictionary

print(dict1.popitem())

# clear() method is used to remove all the key value pairs from the dictionary

print(dict1.clear())

# update() method is used to add the key value pairs to the dictionary
# we need to pass the dictionary as an argument

print(dict1)
print(dict5)
print(dict1.update(dict2))


# copy() method is used to copy the dictionary to another dictionary

print(dict1.copy())


