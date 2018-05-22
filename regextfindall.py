
import re
fhand = open('mboxshort.txt')


def findr(y):
    """
    use findall() to get any email address from the file regardless
    of what line it is on.
    """
    for y in fhand:
        """
        find all lines that start with a alpha character,
        have at least 1 non-whitespace character followed
        an @ sign, followed by at least one non-whitespace character,
        and ends in an alpha character
        """
        x = re.findall('[a-zA-Z0-9]\S*@\S*[a-zA-Z]', y)
        if len(x) > 0:
            print("y is:", x)
        return
    
for line in fhand:
    #remove trailing whitespace
    line = line.rstrip()
    #use regex findall()
    findr(line)
