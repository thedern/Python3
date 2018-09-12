#EDITS BELOW FOR PYTHON 3.x on my windows box


masterFile = open('6.14BuildSourceMd5sum.txt')
targetFile = open('app01_614_md5sum.txt')


masterD = {}
targetD = {}

#Read in files and create dictionaries.  Key is filname, value is md5sum
print("creating master dictionary")
for line in masterFile:
	#remove carriage return
	line = line.rstrip("\n")
	lst1 = line.split(" ")
	#print "DEBUG", lst1
	masterD[lst1[2]] = lst1[0]

print("creating target dictionary")
for line in targetFile:
	#remove carriage return
        line = line.rstrip("\n")
        lst2 = line.split(" ")
	#print "DEBUG", lst2
        targetD[lst2[2]] = lst2[0]


#for key in masterD:
#	print key, masterD[key]

#find the differences between dicttionaries (python 3x only)

print("\n")
print("\n")

print ("finding hash key/value differences")
x = (masterD.items() - targetD.items())

for item in x:
        print(item)

print("\n")
print("\n")

y = (masterD.keys() - targetD.keys())
for item in y:
        print(item)
