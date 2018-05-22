

fhandle=open('romeo.txt')
#print(fhandle)

masterList = []

#read each line and split the text into a list object
for line in fhandle:
    words = line.split()
    #print(words)
    
    #get each item in the list
    for t in range(len(words)):
        #print each item in the list
        print(words[t])
        #if the item is not already in masterList, add it
        if words[t] in masterList : continue
        else:
            masterList.append(words[t])
print(masterList)
print(len(masterList))
