import string
fhand = open('romeo-full.txt')
counts = dict()
for line in fhand:
    #print("Debug", line)
    #remove punctuation
    line = line.translate(str.maketrans('', '', string.punctuation))
    #print("Debug", line)
    #change all lines to lower case
    line = line.lower()
    #create a list from each line
    words = line.split()
    for word in words:
        counts[word] = counts.get(word, 0) + 1
        # get method is short-hand for if/else below
    
    """
        if word not in counts:
            counts[word] = 1
        else
            counts[word] +=1
    """      
lst = list()
#create a list of the key/value pairs in counts, using the items method
for key, val in list(counts.items()):
    #append a tuple, value first, then key so can be sorted by value
    lst.append((val, key))

#sort list in reverse order, largest to smallest. For entires with values that
#are equal, the key will then be used for the sort.
lst.sort(reverse=True)

#print the top 10 most common words in romeo-full.txt
for key, val in lst[:10]:
    print(key, val)
