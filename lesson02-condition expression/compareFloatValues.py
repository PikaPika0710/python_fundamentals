f1 = 1.11-1.10 #0.010000000000000009
f2 = 2.11-2.10 #0.009999999999999787
print("f1 = ", f1)
print("f2 = ", f2)
epsilon = f1 - f2
if epsilon < 0:
    epsilon = -epsilon
"""    
if f1 == f2:
    print("f1 = f2")
else:
    print("f1 # f2")
"""

if epsilon < 0.0000001:
    print("f1 = f2")
else:
    print("f1 # f2")
