#string-str()-is a collection of charactors encloesd with single or double quotes.
#string methods :
string=" python "
str1=string.replace('p','j')
print(str1)
print(string.upper())
print(string.lower())
print(len(string))
print(string.find('y'))
print(string.index('p'))
print(string.capitalize())
print(string.title())
print(string.strip())#remove the both sides space.
print(string.lstrip())#remove the left space only.
print(string.rstrip())#remove the right space only.

#string slicing it is used to extract the part an string or substring with string index.
print(string[0:7])
print(string[1:])
print(string[::-1])
#without len() 
total_char=0
for char in string:
    total_char+=1
print("size of string without len():-",total_char)
# with len()
print("Size of string with len():",len(string))