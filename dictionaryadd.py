
#create dictionary
new = dict()
#create counter to be used as the value of the key:value pair
counter = 0

fhandle = open('romeo.txt')
for line in fhandle:
    #create a list from each line
    words = line.split()
    
    #iterate through each list item
    for i in range(len(words)):

        #check if list item is already in dictionary
        if words[i] in new : continue
        else:
            #update counter
            counter +=1
            #update dictionary; format 'dict[key] = value'
            new[words[i]] = counter
        
print(new)

