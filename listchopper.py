t1 = [1, 2, 3, 4, 5, 6]


#modifies the list but returns none
def list_chop(x):
    t1.pop()
    t1.pop(0)
    print(t1)

    
#modifies the list but returns new list
def list_chop2(x):
    t2 = []
    for i in range(len(t1)):
        t2.append(t1[i])
    return t2
    
    
list_chop(t1)

t2 = list_chop2(t1)


print("T2 is ", t2)
print("T1 is ", t1)
#proof that the list objects are not the same object
print(t2 is t1)


