n = int(input('Enter the Number: '))
factorial = 1

for i in range (1 , n+1):
    factorial = factorial * i 
print(f'The facrorial of {n} is {factorial}')