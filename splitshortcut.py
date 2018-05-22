#Split line shortcut.  A conditional statement was created with no 'else' statement

fhand = open('mboxshort.txt')
for line in fhand:
    #shortcut 'if' statement
    if not line.startswith('From '): continue
    #create list from line
    words = line.split()
    #print the 3rd item from the list
    print(words[2])
    
