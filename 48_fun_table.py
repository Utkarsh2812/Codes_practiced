def table(num):
    k = 1
    for k in range(11):
        print(str(num) + ' × ' + str(k) + " = " + str( num * k ))

num = int(input('Enter the Number:  '))
table(num)

# Reverse

def table(num):
    k = 1
    for k in range(10 , -1 , -1 ):
        print(str(num) + ' × ' + str(k) + " = " + str( num * k ))

num = int(input('Enter the Number:  '))
table(num)