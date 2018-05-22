text = 'but soft what light in yonder window breaks'

#@ create list from text
words = text.split()

#@ create 2nd list
t = list()

#@ for each word in list, get its length and the word itself and add to second list
for word in words:
        #@ append tuples of word length, word
	t.append((len(word), word))
	#print("Debug:", t)

#@ sort longeset to shortest
t.sort(reverse=True)
#print("Debug:", t)

#Create a new list and add the words only, in order, from the tuple set.
res = list()
for length, word in t:
    #print("Debug:", length, word)
    res.append(word)

print(res)
