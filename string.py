# # string is data type in python 
# name= "Ramraj"
# nameshort = name[0:3]# start from index 0 all the way till 3
# print(nameshort) 
# print(name[-4:-1])

# # clicing with skip value 
# # run on windo terminal 
# # word="amazing"
# # word[1:7:5]
# # print(w)

# # negative slicing 
# print(name[-4:-1])
# print(name[1:4])

# print(name[:4])# is same as print (name[0:4])
# print(name[1:])# is same as print (name[1:5])


# string function 
# 1. len() function
name = "rajkumar "
print(len(name))# find the lenght of the charter 
print(name.endswith("mar"))# find the end word of the word 
print(name.startswith("ra"))#find the start word of the charcter
# print(name.capitalize())convert the first word small to capital
print(name.find("raj"))# find the word 

# str(): converts an object to a string 
a=str(123)
print(a) # Output: '123'

# lower(): converts all characters in a string to lowercase
print(name.lower()) # Output: 'rajkumar '

# upper(): converts all characters in a string to uppercase
print(name.upper()) # Output: 'RAJKUMAR '

# strip():removes leading and trailing whitespace
print(name.strip()) # Output: 'rajkumar'    

# split():splits a string into a list where each word is a list 
print(name.split()) # Output: ['rajkumar']

# join():joins the elements of an iterable to the end of the string 
print("-".join(["hello","raj"])) # Output: 'hello-raj'

# replace(): replace a specified phrase with author specified phrase
print(name.replace("raj","rajesh")) # Output: 'rajkumar rajesh'

# count():returns the number of times a specified value appears in the string 
print(name.count("raj")) # Output: 1

# isalpha(): returns 'true' if all characters in the string are alphabets 
print("helol".isalpha()) # Output:True 

# isdigit():returns true if all characters in the string are digit
print("123".isdigit()) # Output:True
