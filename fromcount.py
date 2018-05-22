
fhandle=open('mbox.txt')
count=0
#create list of each line
for line in fhandle:
    words = line.split()
    #guardian statement to protect from blank lines and lines that do not start
    #with 'From'
    #print('Debug:', words)
    if len(words) == 0 : continue
    if words[0] != 'From' : continue
    else:
        print(words[1])
        count+=1
print(f'there were {count} lines starting with the word "From"')
