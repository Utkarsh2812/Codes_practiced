def games(name):
    print('Which game do you want\n ' + name )

def price(cost):
    GST = ((cost * 18)/100) + cost
    return GST

games("BGMI")
print("Price of Game: " , price(500))