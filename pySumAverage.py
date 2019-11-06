#Sum/Average Program
#Your first and last name:Nicholas Smythe
#Your student ID:1282081

#Build on what you did in the 'List of Names' program
#Instead of entering 10 names, enter 20 numbers (integers)
#Instead of searching for a name in the list
#   Compute the sum of all 20 numbers
#   Compute the average for all 20 numbers

#User interaction-
#Enter a number:
#The sum of the numbers you entered is:
#The average of the numbers you entered is:
end = False
numberslist = []
sumint = 0
for x in range (0,20):
    anumber = int(input("enter a number:"))
    numberslist.append(anumber)

for x in range (0,20):
    sumint= sumint + numberslist[x]
print(sumint)


average = sumint/len(numberslist)
print(average)    
                
    
