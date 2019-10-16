#List creation and searching
names  = []
for x in range(0,10):
    aname = input("enter a name:")
    names.append(aname)
    
    

print (names)
search = input("enter search name:")
if search in names:
    print(search, "was found")
    
else:
    print (search, "was not found")
    
