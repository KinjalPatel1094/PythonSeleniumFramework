# if else statement
name = "kinjal patel"

if name == "kinjal patel":
    print("correct name")
else:
    print("different name")

print("hi there")


age = 2024-1994

if age >= 31:
    print("getting mature")
else:
    print("still young kinji")

calc = 2050-age

if calc == 50:
    print("oh my god")
else:
    print("no worry")

# For loop statement

# Iterate through list

obj = [1, 2, 3, 4, 5]

for i in obj:
    print(i)
print("separate statement than for loop")

# second for loop example on real range without list

# sum of first five numbers

# no need to declare list
summ = 0
for j in range(1, 6):  # range(i, j) => i to j-1
    summ = summ + j
print(summ)  # end of for loop here , this is separate statement or it will print sum everytime in for loop

print("********************")
for k in range(0, 10, 3):  # adding 3 in numbers up to 10-1 , it is just like k++ in javascript/java
    print(k)

print("********************")
for m in range(5):  # if i=0, no need to add it , this will just start from 0. printing up to m-1 here
    print(m)

# WHILE LOOP

print("WHILE LOOP")
num = 10

# Position statements correctly - most important
while num > 1:
    if num == 7:
        num = num - 1
        continue
    if num == 4:
        break
    print(num)  # this line is of while loop not if statement because of its position
    num = num - 1