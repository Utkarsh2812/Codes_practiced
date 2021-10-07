m = int(input('Enter marks in 1st subject:  '))
n = int(input('Enter marks in 2nd subject:  '))
o = int(input('Enter marks in 3rd subject:  '))

if(m >= 33 ):
    print('Pass certificate granted for subject 1 ')
else:
    print(' Fail in subject 1 ')
if(n >= 33 ):
    print('Pass certificate granted for subject 2 ')
else:
    print(' Fail in subject 2 ')
if(o >= 33 ):
    print('Pass certificate granted for subject 3 ')
else:
    print(' Fail in subject 3 ')
if((m+n+0)/3 > 40):
    print('You are passed as Total percent is greater than 40')
else:
    print('You are fail as your total percent is less than 40')

print('Regards')