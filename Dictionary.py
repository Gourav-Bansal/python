d1 = ()
# print(type(d1))
d2 = {"Gourav":"Burger", "Saksham":"Pizza"}
# print(d2["Saksham"])
d2 = {"Gourav":"Burger", "Saksham":"Pizza", "Harshit":{"B":"Hi", "L":"Hello"}}
# print(d2["Harshit"]["L"])
#  del d2["Gourav"]   # delete the word
d3 = d2.copy()
del d3["Gourav"]
print(d2)