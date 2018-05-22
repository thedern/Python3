
#counts every letter in the text

import string
char = dict()
lst = list()

fhand = open('romeo-full.txt')
for line in fhand:
    if len(line) == 0: continue
    line = line.rstrip()
    #get each line and remove punctuation
    line = line.translate(str.maketrans('', '', string.punctuation))
    #convert to lowercase
    line = line.lower()
    #split each line into a list of words
    words = line.split()
    #get each letter in each word
    for word in words:
        for letter in word:
            #print(letter)
            char[letter] = char.get(letter, 0) + 1
print(char)

#append tuple in value/key order, so can be sorted by value
for key, val in list(char.items()):
    lst.append((val, key))

#lists are mutable, sort in-place
lst.sort(reverse=True)

#print thet values of the tuple, individually, with a space
for x, y in lst:
    print(x, y)

        
