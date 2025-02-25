# stringformating is used to format the string in a proper way


name = "Rajini"
age = 70

print("my name is {} and i am {} years old".format(name,age))

# instead of using format we can use f-string
# user understand easily through f-string than format

print(f'my name is {name} and i m {age} years old')

name = "Sunitha"
age = 30
marital_status = "married"
location = "Chennai"

print(f'my name is {name} and i am {age} years old.i am {marital_status} and i am living in {location}')
