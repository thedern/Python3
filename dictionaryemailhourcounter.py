
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
        #Time is the list item at index 5
        time = line[5].split(':')
        
        #Hour is the list item at index 0
        hour = time[0]
        
        #use dictionary get method to add addresses
        #adds new if does not exist
        #increments counter if address already exists
        emails[hour] = emails.get(hour, 0) + 1
    

#create list using dictionary items method.
for key, val in list(emails.items()):

    #append a tuple of key/val pair (note: append only takes 1 arg at a time,
    #a tuple is a single argument.
    lst.append((key, val))

#sort list smallest to largest
lst.sort()

#print thet values of the tuple, individually, with a space
for key, val in lst:
    print(key, val)

                
             
