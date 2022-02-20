import numpy as np
number=np.random.randint(1,101)
count=0
while True:
    count+=1
    predict_number=int(input('guess number 1 to 100 '))
    if predict_number>number:
        print('too big')
    elif predict_number<number:
        print('too small')
    else:
        print('you got it bro, you guessed number = {} in {} tries'.format(number,count))
        break