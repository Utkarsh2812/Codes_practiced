numb = int(input('Enter a number: '))
prime = True

for b in range( 2 , numb ):
    if (numb % b == 0):
        prime = False
        break
if prime:
    print('This is a Prime Number')
else:
    print('This is not a Prime Number')


# Second Method

n = int(input("Enter the number: "))
for i in range( 2 , n ):
    if(n % i == 0):
        print('Its not prime')
    else:
        print("Its prime")
    break

print("Done")

