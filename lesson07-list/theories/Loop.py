print("*"*30)
list = [5,7,2,9,6,3,1,10,17,15]

for x in list:
    print(x, end=" ")
print()
print("*"*30)

for i in range(len(list)):
    print(list[i], end = " ")

print()
print("*"*30)

#reverse loop
for y in range(len(list)-1, -1, -1):
    print(list[y], end = " ")

