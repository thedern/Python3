#Search for lines that contain "From"

counts = dict()
lst = list()
import re
fhand = open('mbox.txt')
    
for line in fhand:
    #remove trailing whitespace
    line = line.rstrip()
    #find lines that begin with from
    if re.search('^From:.+@', line):
        #create dictionary (histogram) of line counts using get method
        counts[line] = counts.get(line, 0) + 1
        
#create a list of key/value tuples from dictionary
for key, val in list(counts.items()):
    #append tuple in value/key format so may be sorted by value
    lst.append((val, key))

#mutable; sort in-place
lst.sort(reverse=True)

#print result
for x, y in lst:
    print(x, y)





