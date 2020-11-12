# spam = open('assets/spam.txt')

# # print(spam)

# content = spam.read()

# print(content)

# print('Is file closed?', spam.closed)

# spam.closed()
# print('Is file closed?', spam.closed)


#alternative way
with open('assets/spam.txt') as file:
    print(file.read())

print('file is closed?', file.closed)


help(file) #lists functions/methods for file w/description
print(dir(file)) #methods and attributes
help(open) #gives details about the open function


with open('assets/brain.jpg', 'rb') as file:
    contents = file.read()

for x in contents[:128]:
    print(type(contents)) #type inspects the contents of the file

with open('assets/brain.copy.jpg', 'wb') as f2:
    f2.write(contents) #creates a copy of brain.jpg to be rewritten 
