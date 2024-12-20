#programme will read names and ages from a file

import csv
#variables
filename="C:\\Users\\User\\source\\repos\\Guests.txt"
READ='r'

#Open file to read
with open (filename,mode=READ) as file:

    filecontents=csv.reader(file)
#use for loop to read the contents
    for row in filecontents:
         print(row)
    # #     #to print individual character,make loop for above list
    # # for singleCharacter in row:
    # #     print(singleCharacter)


    #will seperate the values in each row with comma and remove the sqaure brackets
    # for row in filecontents:
    #     print(",".join(row))

   
