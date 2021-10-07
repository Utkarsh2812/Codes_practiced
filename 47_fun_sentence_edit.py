def sentence(string , word):
    str = string.replace( word , "")
    return str.strip()

St = "Python is evolving in a great pace "
print(sentence(St , "evolving"))