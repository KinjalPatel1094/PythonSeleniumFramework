file = open('test.txt')
print(file.read())  # read file
print(file.read(15))  # read up to n number of characters

print(file.readline())  # read by line
print(file.readline())  # read next line

# Interview que: Print line by line using readline method

# readlines() method => same as read method, but it will store lines in list.

linelist = file.readlines()
for i in linelist:
    print(i)

# using while and readline() method
line = file.readline()
while line != "":
    print(line)
    line = file.readline()


file.close()

