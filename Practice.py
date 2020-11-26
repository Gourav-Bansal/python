row = int(input("Enter no. of rows : "))
bool_ = int(input("Enter 1 or 0 : "))
if bool_ == 0:
    bool_ = False
else :
    bool_ = True
if bool_ == True:
    for i in range(row) :
        for i in range((i+1)) :
            print("*")
        print()
