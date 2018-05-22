
#function to update list
def promptList(list1):
    
    #prompt user for number
    num = input("please enter a number \n")
    print("Debug at prompt:", num)

    #test response and update list1
    if num == 'done':
        #'done' was entered, breaking loop.
        print("Done, list is", list1)
        x = max(list1)
        print ("max list item is", x)
        y = (min(list1))
        print ("min list item is", y)
    else:
        try:
            print("Debug at list:", num)
            
            #update the list formatting the str as int
            list1.append(int(num))
            print(f"list is now {list1}")
            
            #prompt for another number, (loop)
            promptList(list1)

        except:
            print("enter a number or 'done' only")
            promptList(list1)
   
  
#create empty list
list1 = []

#call function, passing in the empty list
promptList(list1)
