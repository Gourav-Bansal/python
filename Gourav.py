"""a = open("gourav.txt", "w")
b = a.write("Hii everyone, it's gourav And i am 17 years old.\n")
print(b)
a.close()"""
   # Handle read and write
a = open("gourav.txt", "r+")
print(a.read())
a.write("thank you")
print(a.read())
