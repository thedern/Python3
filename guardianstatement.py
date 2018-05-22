fhand = open('mboxshort.txt')
count = 0
for line in fhand:
    #create a list of each line
    words = line.split()
    #guardian statement 1
    if len(words) == 0 : continue
    #guardian statement 2
    if words[0] != 'From' : continue
    #print 3rd item in list
    print(words[2])
