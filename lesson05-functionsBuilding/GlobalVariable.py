g = 5
def increase():
    global g
    g = 10
    g = g + 1

increase()
print(g)