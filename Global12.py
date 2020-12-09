# l = 10  # Global variable
# def function(a) :
#     # l = 5  # local
#     m = 6
#     global l
#     l = l + 45
#     print(l, m)
#     print(a, "I have printed")
# function("This is me")
# print(l)
def gourav() :
    x = 20
    def rohan() :
        global x
        x = 88
    print("before calling rohan", x)
    rohan()
    print("after calling rohan", x)
gourav()
print(x)
