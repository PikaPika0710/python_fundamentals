def ROI(revenue, cost):
    return (revenue-cost)/cost

def invest(ROI):
    if ROI >= 0.75:
        return "Shoud invest!"
    else:
        return "Should not invest!"

try :
    revenue, cost = eval(input("Input revenue and cost: "))
    roi = ROI(revenue, cost)
    print("ROI = ", roi)
    print(invest(roi))
except:
    print("Input the valid value format!!!")
