counts = { 'chuck' : 1, 'annie' : 42, 'jan' : 100 }

#@ loop and print dictionary contents
#@ note: dictionaries are referenced by key

for key in counts:
    #@ print key, value
    print(key, counts[key])


#@ loop and print dictionary contents with values > 10

for key in counts:
    if counts[key] > 10:
          print(key, counts[key])

#@ loop and print dictionary contents, sorted alphabetically by key

list1 = list(counts.keys())
print(list1)
list1.sort()
for key in list1:
    print(key, counts[key])
