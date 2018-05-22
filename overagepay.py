hours = input('please enter hours worked\n')
rate = input('please enter your hourly rate\n')

#try:
#    if int(hours) > 40:
#        #Number of hours over 40
#        overage = int(hours) - 40
#        print(f'overage hours are {overage}')
#        #Extra pay is 1.5 x rate for hours over 40
#        extrapay = overage * (int(rate) * 1.5)
#        print(f'extrapay is ${extrapay}')
#        #Total is 40 x rate + the extrapay
#        totalpay = 40 * int(rate) + extrapay
#        print (f'totapay is ${totalpay}')
#    else:
#        totalpay = int(hours) * int(rate)
#        print (f'total pay is ${totalpay}')
#except:
#    print('please enter numbers only')
#    print(f'you entered: {hours} and {rate}')



#Same program as above but as a set of functions
#Can either return the value from the function or, print
#the result from the function's body

def compute_pay(a, b):
    standardpay = a * b
    return standardpay
    #print(f"standard pay is {standardpay}")

def compute_overagepay(a, b):
    overage = a - 40
    extrapay = (overage * (b * 1.5)) + (40 * b)
    return extrapay
    #print (f"pay including overtime is {extrapay}")

try:
    intHours = float(hours)
    intRate = float(rate)

    if intHours > 40:
        #compute_overagepay(intHours, intRate)
        x = compute_overagepay(intHours, intRate)
        print(x)
    else:
        #compute_pay(intHours, intRate)
        x = compute_pay(intHours, intRate)
        print(x)
except:
    print("Enter numbers only")
        

    
