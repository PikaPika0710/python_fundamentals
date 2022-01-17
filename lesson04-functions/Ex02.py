from time import sleep

'''   *
      * *
      * * *
* * * * * * *
* * *
* *
* 
'''

n = 7
for i in range(n):
    if i == n // 2:
        for j in range(n):
            print("*", end=" ")
    elif i > n // 2:
        for j in range(n//2):
            if j < n - i:
                print("*", end=" ")
    else:
        for j in range(n):
            if j < n // 2:
                print(" ", end=" ")
            else:
                if j <= n // 2 + i:
                    print("*", end=" ")
    print()

'''   *       
      * *     
      *   *   
* * * * * * * 
*   * 
* *   
*  
'''
sleep(1)
for i in range(n):
    if i == n // 2:
        for j in range(n):
            print("*", end=" ")
    elif i > n // 2:
        for j in range(n//2):
            if j == 0 or j == n - i - 1:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    else:
        for j in range(n):
            if j < n // 2:
                print(" ", end=" ")
            else:
                if j == n // 2 or j == n//2 + i:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
    print()
'''
      * * * * 
      * * * 
      * * 
      *       
    * * 
  * * * 
* * * * 
'''
sleep(1)
for i in range(n):
    if i == n // 2:
        for j in range(n):
            if j == n//2:
                print("*", end=" ")
            else:
                print(" ", end=" ")
    elif i > n // 2:
        for j in range(n):
            if j <= n//2:
                if j >= n - i - 1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
    else:
        for j in range(n):
            if j < n // 2:
                print(" ", end=" ")
            else:
                if j < n-i:
                    print("*", end=" ")
    print()
'''
      * * * * 
      *   *   
      * *     
      *       
    * * 
  *   * 
* * * * 
'''
sleep(1)
print()
for i in range(n):
    if i == n // 2:
        for j in range(n):
            if j == n//2 :
                print("*", end=" ")
            else:
                print(" ", end=" ")
    elif i > n // 2:
        for j in range(n):
            if j <= n//2:
                if j == n//2 or j == n - i - 1 or i == n-1:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
    else:
        for j in range(n):
            if j < n // 2 :
                print(" ", end=" ")
            else:
                if j == n//2 or j == n-i-1 or i == 0:
                    print("*", end=" ")
                else:
                    print(" ", end=" ")
    print()


''' 
while i < n:
    print(" ", end=" ")
    if i == (n - 1) // 2:
        j = 0
        while j < n:
            print("*", end=" ")
            j = j+1
    elif i > (n - 1) // 2 :
        j = 0;
        while j < n - i :
            print("*", end=" ")
            j = j + 1
    elif i < (n - 1) // 2:
        j = 0;
        while j < n:
            if j<n//2:
                print(" ", end=" ")
            else:
                if j <= n//2 + i:
                    print("*", end=" ")
            j = j + 1;
    i = i+1
    print()
'''
