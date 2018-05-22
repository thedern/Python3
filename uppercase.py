#Program will print all lines in uppercase

def enterfile():
    try:
        fh = open(input("please enter file name\n"))
        count = 0
        total = 0
        for str in fh:
            if str.startswith('X-DSPAM-Confidence'):
                count+=1
        
                colon = str.find(":")
                value = float(str[colon+1:])
                print(value)
                total+=value
        
        #exit loop and calcuate
        print("count is :", count)
        print("total is :", total)
        print("average is", (total/count))
    except:
        print("enter a valid file name")
        enterfile()



enterfile()
    

        
