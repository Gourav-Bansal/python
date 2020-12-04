#      Health Management System
#  3 clients - harry, rohan, hammad
# Total 6 fies
# write a function that inputs client name
def getdate() :
    import datetime
    return datetime.datetime.now()

def edit_() :

    if a == 1 :
        b = int(input("Enter 1 for exercise and 2 for diet : "))
        if b == 1 :
            with open("gourav.txt", "a") as f:
                 data_ = str(input("Write your observation : "))
                 f.write(data_)
                 print("Your data has been entered")
        else :
            with open("gourav-diet", "a") as f:
                data_ = str(input("Write your observation : "))
                f.write(data_)
                print("Your data has been entered ")
    elif a == 2 :
        b = int(input("Enter 1 for exercise and 2 for diet : "))
        if b == 1:
            with open("arnav", "a") as f :
                data_ = str(input("Write your observation : "))
                f.write(data_)
                print("Your data has been entered")
        else :
            with open("arnav-diet", "a") as f :
                data_ = str(input("Write your observation : "))
                f.write(data_)
                print("Your data has been entered")
    else :
        b = int(input("Enter 1 for exercise and 2 for diet : "))
        if b == 1:
            with open("harry", "a") as f:
                data_ = str(input("Write your observation : "))
                f.write(data_)
                print("Your data has been entered")
        else :
             with open("harry-diet", "a") as f:
                   data_ = str(input("Write your observation : "))
                   f.write(data_)
                   print("Your data has been entered")

def log_() :
    if a == 1 :
        b = int(input("Enter 1 for exercise and 2 for diet : "))
        if b == 1:
             with open("gourav.txt") as f:
                 f.readline()
                 getdate()

        else :
             with open("gourav-diet") as f:
                 getdate()
                 f.readline()
    elif a == 2 :
        b = int(input("Enter 1 for exercise and 2 for diet : "))
        if b == 1 :
            with open("arnav.txt") as f :
                getdate()
                f.readline()
        else :
            with open("arnav-diet") as f :
                getdate()
                f.readline()
    else :
        b = int(input("Enter 1 for exercise and 2 for diet : "))
        if b == 1:
            with open("harry.txt") as f:
                getdate()
                f.readline()
        else:
            with open("harry-diet") as f:
                getdate()
                f.readline()


a = int(input("Enter 1 for gourav, 2 for arnav and 3 for harry : "))
c = int(input("Enter 1 for log and 2 for entering data : "))
if c == 1 :
    log_()
else:
    edit_()





