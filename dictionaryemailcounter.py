
#enter email addresses only in to dictionary
#sort and print the addresses in order of most frequent to least frequent.

emails = dict()
lst = list()

fhand = open('mbox.txt')

for line in fhand:
    line = line.split()
    #guardian statements
    if len(line) == 0: continue
    if line[0] != 'From': continue
    else:
        #print("Debug:", line)
        for i in range(len(line)):
            if '@' not in line[i]: continue
            else:
                #print(line[i])
                #use dictionary get method to add addresses
                #adds new if does not exist
                #increments counter if address already exists
                emails[line[i]] = emails.get(line[i], 0) + 1
#print(emails)
#create list using dictionary items method.
for key, val in list(emails.items()):

    #append a tuple of key/val pair (note: append only takes 1 arg at a time,
    #a tuple is a single argument
    lst.append((val, key))

# sort list largest to smallest
lst.sort(reverse=True)

for key, val in lst:
    print(key, val)

                
             
