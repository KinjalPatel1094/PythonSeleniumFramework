# Exceptions in python


ItemsInCart = 0

# 1 way using raise keyword
if ItemsInCart != 2:
    pass
     #  raise Exception("product cart count not matching")

# 2nd way using assert keyword
# assert(ItemsInCart == 2)

# TRY EXCEPT BLOCK:

try:
    with open('test2.txt', 'r') as filereader:
        filereader.read()

except:
    print("I reached this block as there is failure in try block-file not found")


# Catching the error that PYTHON throws :

try:
    with open('test2.txt', 'r') as reader:
        reader.read()

except Exception as e:
    print(e)

# Finally block : execute everytime no matter pass or fail test

# Finally - use it to add code to delete cookies before starting new test

finally:
    print("clearing the cookies")


