file = open('pelican.txt')
print(file.readable())

# telling you if the file is readable or not; true or false

print()

print(type('pelican.txt'))

# shows data is string type

print()

read = file.readlines()
print(read)

# displaying contents as they are typed

print()

myFile = open('pelican.txt', 'r')
content = myFile.read()
print(content)

contentList = content.split(',')
myFile.close()
print(contentList)

print()

print("The number of items in the list is; " + str(len(contentList)))

print()

with open('pelican.txt') as file:
    for item in file:
        print(item)

# using a loop to print the contents of the file line by line
