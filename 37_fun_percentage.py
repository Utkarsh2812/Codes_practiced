def percent(marks):
    p = ((marks[0] + marks[1] + marks[2])/300) * 100 
    return p

marks = [85,36,96]
percentage = percent(marks)

print(percentage)