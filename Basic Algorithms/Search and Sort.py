'''Code for Searching and Sorting'''
item=[0,9,7,11,34,12,13,15,18,19]                                         #problem given value
#item=list(map(int,input("Enter Positive List of Items").split()))        #user input value
n=int(input("Enter your Search Item"))

'''Simple Linear Search'''
for i in range(len(item)):
    if item[i]==n:
        print("Found at Index",i)
        print("Found at Position of Item",i+1)
        break
else:
        print("Not Found")
print("The Elements are: ",item)
        
'''Sorting'''        
item.sort()
print("The Sorted Elements are: ",item)

