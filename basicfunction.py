
#function that returns "none"
def adder(x, y):
    print(x + y)

#function that returns a value
def subtracter(x, y):
    return x - y

def printHello():
    print("hello")

#-------------------------#

#test adder function; returns NONE
a = adder(6, 6)
print(a)

#test subtracter function; returns a value
b = subtracter(9, 6)
print(b)

#test a loop that calls a function
num = 0
while num < 5:
    printHello()
    num+=1



