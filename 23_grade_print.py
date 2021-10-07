h = int(input('Enter the Marks scored by Student:  '))

if(h >= 90 and h <= 100):
    print('Excellent ')
elif(h >= 80 and h < 90):
    print('A')
elif(h >= 70 and h < 80):
    print('B')
elif(h >= 60 and h < 70):
    print('C')
elif(h >= 50 and h < 60):
    print('D')
elif(h < 50):
    print("F")

print('Regards ')