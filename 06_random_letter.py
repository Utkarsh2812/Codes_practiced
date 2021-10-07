letter = '''DEAR,  <|NAME|>, 
         YOU ARE SELECTED
 DATE:  <|DATE|>'''

nme = input('Enter your name: \n')
dt = input('Enter Date: \n')

letter = letter.replace( "<|NAME|>" , nme )
letter = letter.replace( "<|DATE|>" , dt )
print(letter)