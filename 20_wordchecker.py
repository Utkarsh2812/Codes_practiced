a = input('Enter a Comment\n ')

if('make a lot of money' in a or 'click this' in a or 'buy now' in a or 'subscribe this' in a):
    print('A spam comment ...  sshhshsh : ')
else:
    print(a , 'is correct')

print('Completed 👍')