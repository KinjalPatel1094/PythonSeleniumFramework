# TO write file , you have to first read it and ave it in list
# Reverse the list  using reversed() method
# then write the list back to the file.


# same as filereader = file.open('test.txt' ,'r') , file.close()
with open('test.txt', 'r') as filereader:
    content = filereader.readlines()     # store file content in list
    reversed(content)                    # reverse the list
    with open('test.txt', 'w') as filewriter:
        for w in reversed(content):
            filewriter.write(w)           # write it back to file




