###
# Write a program, in any language (incl pseudocode) that iterates the numbers from 1 to 100.
#
# For any value divisible by 4, the program should print "Go".
#
# For any value divisible by 5, the program should print "Figure".
#
# For any value divisible by 4 and 5, the program should print "GoFigure".
###

for i in range(1, 101,):
    if i % 4 == 0 and i % 5 == 0:
        print(f"{i} GoFigure")
    elif i % 4 == 0 and i % 5 != 0:
        print(f"{i} Go")
    elif i % 5 == 0 and i % 4 != 0:
        print(f"{i} Figure")
    else:
        print(f"{i} not divisible by 4 or 5")
    
