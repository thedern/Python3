
def prompt(list1):
    num = input("please enter a number:\n")
    if num == "done":
        print("done")
    else:
        try:
            #check to ensure number was passed and append to list
            list1.append(int(num))
            print("list1 is now", list1)
            b = sum(list1)
            print("sum of list", b)
            c = len(list1)
            #find the average by dividing sum by the number of items in list
            print("average of list", (b/c))
            #find max number in list
            print("max number in list is", max(list1))
            #find min number in list
            print("min number in list is", min(list1))
            prompt(list1)
            
        except:
            print("enter a number or 'done' only")
            prompt(list1)

#create empty list
list1 = []

#pass list to prompt so it may be filled
prompt(list1)

    
