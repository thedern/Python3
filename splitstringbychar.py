
#Suppose you want the address/host information after the '@' sign
#Split a string based on character position.

data = "From stephen.smith@uct.ac.za Sat Jan 5 09:14:16 2008"
#find the '@' character
atpos = data.find('@')
print(atpos)

#find the firt asci space character after '@'
sppos = data.find(' ',atpos)
print(sppos)

#slice based on position
host = data[atpos+1:sppos]
print(host)

#Extract the data after the colon and convert to a float

str = 'X-DSPAM-Confidence:0.8475'
colon = str.find(':')
#slice from position right after the colon to the end of the line
final = float(str[colon+1:])
print(final)
