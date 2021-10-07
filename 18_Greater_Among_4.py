b = int(input('Enter 1st number: '))
c = int(input('Enter 2nd number: '))
d = int(input('Enter 3rd number: '))
e = int(input('Enter 4th number: '))

if(b>c and b>d and b>e):
    print('Greater number among all is: ' , b , 'i.e 1st one')
elif(c>b and c>d and c>e):
    print('Greater number among all is: ' , c , 'i.e 2nd one')
elif(d>b and d>c and d>e):
    print('Greater number among all is: ' , d , 'i.e. 3rd one')
elif(e>b and e>c and e>d):
    print('Greater number among all is: ' , e , 'i.e 4th one')
else:
    print('All are equal')

print('Completed 👍')