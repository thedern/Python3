score = input('please enter a score between 0.0 and 1.0\n')

try:
    fscore = float(score)
    if fscore >= 0.0 and fscore <= 1.0:
        if fscore >= 0.9:
            print('A')
        elif fscore >= 0.8 and fscore <= 0.9:
            print('B')
        elif fscore >= 0.7 and fscore <= 0.8:
            print('C')
        elif fscore >= 0.6:
            print('D')
        else:
            print('F')
    else:
        print('score out of range')
except:
    print('please enter a number')
