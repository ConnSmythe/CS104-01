#List creation and searching
end=False
names  = []
for x in range(0,10):
    aname = input("enter a name:")
    names.append(aname)
    
    
while not end:
    
    print (names)
    search = input("enter search name:")
    if search == ("end"):
        end=True
    elif search in names:
        print(search, "was found")
    
    elif search not in names:
        print (search, "was not found")
