
#@ Sort dictionary by value, higest to lowest

d = {'a':10, 'b':20, 'c':30}
lst = list()

for key, val in d.items():
    #print("Debug:", key, val)
    #populate list with key/val tuples
    lst.append((val, key))

#print unsorted for comparison
print(lst)
#sort the list in reverse order
lst.sort(reverse=True)
print(lst)


