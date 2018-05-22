
fhandle = open('mbox.txt')
new = dict()
new2 = dict()
new3 = dict()

for line in fhandle:
    #create a list of each line of text
    words = line.split()
    #guardian statements
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    else:
        #print("Debug:", words)
        #get 3rd item in list which should be day of week
        c = words[2]
        d = words[1]
        """
        @Use the dictionary 'get method' to update the dictionary with
        a new key:value pair where one does not exist. Or, increment the
        key's value where the key already exists.
        """
        #get histogram of days
        new[c] = new.get(c, 0) + 1

        #get histogram of email addresses
        new2[d] = new2.get(d, 0) + 1

        
        atsign = d.find("@")
        host = d[atsign+1:]
        new3[host] = new3.get(host, 0) + 1
        


print(new)
print(new2)
print(new3)



        
        
