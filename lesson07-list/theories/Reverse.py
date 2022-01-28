lst = [1,2,3,4,5,6]
print(lst)
#reverse the order of list
lst.reverse()
print(lst)


lst2 = reversed(lst)
print(lst)
print(lst2)
for item in lst2:
    print(item, end =" ")