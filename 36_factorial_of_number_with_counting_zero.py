n = int(input('Enter the Number: '))
factorial = 1

for i in range (1 , n+1):
    factorial = factorial * i 
print(f'The facrorial of {n} is {factorial}')

res = [int(x) for x in str(factorial)] # This line will convert the integral value of Factorial to list
print(res.count(0))