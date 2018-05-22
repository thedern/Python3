#create histogram of every letter in the the file, romeo.txt
#update syntax:  dict_name{key] = value


#create dictionary
new = dict()

fhandle = open('romeo.txt')
for line in fhandle:
    #create a list from each line
    words = line.split()

    #get each word from the list of words
    for i in range(len(words)):

        #get each letter in each word; from the list of words
        for t in range(len(words[i])):
            
            """
            #@use the dictionary's 'get method' to update the dictionary, setting
            #@default value of (0 + 1) if the key does not already exist.
            #@further, the same code increments the value by 1 if key already does exist.
            #@this is a slick shorthand for the if/else ccode commented out below.
            """
            
            c = words[i][t]
            #print("Debug:", c)
            new[c] = new.get(c, 0) + 1

            #@if not already in the dictionary, add as a new key with a value of '1'
            #if (words[i][t]) not in new:
                #new[words[i][t]] = 1

            #@if already in dictionary, increment key's value
            #else:
            #    new[words[i][t]] = new[words[i][t]] + 1
print(new)
        
    
