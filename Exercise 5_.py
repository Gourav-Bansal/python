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
                 f.write(str(getdate()))
                 f.write(data_)
                 print("Your data has been entered")
        else :
            with open("gourav-diet", "a") as f:
                data_ = str(input("Write your observation : "))
                f.write(str(getdate()))
                f.write(data_)
                print("Your data has been entered")
    elif a == 2 :
        b = int(input("Enter 1 for exercise and 2 for diet : "))
        if b == 1:
            with open("arnav", "a") as f :
                data_ = str(input("Write your observation : "))
                f.write(str(getdate()))
                f.write(data_)
                print("Your data has been entered")
        else :
            with open("arnav-diet", "a") as f :
                data_ = str(input("Write your observation : "))
                f.write(str(getdate()))
                f.write(data_)
                print("Your data has been entered")
    else :
        b = int(input("Enter 1 for exercise and 2 for diet : "))
        if b == 1:
            with open("harry", "a") as f:
                data_ = str(input("Write your observation : "))
                f.write(str(getdate()))
                f.write(data_)
                print("Your data has been entered")

        else :
             with open("harry-diet", "a") as f:
                 data_ = str(input("Write your observation : "))
                 f.write(str(getdate()))
                 f.write(data_)
                 print("Your data has been entered")

def log_() :
    if a == 1 :
        b = int(input("Enter 1 for exercise and 2 for diet : "))
        if b == 1:
             with open("gourav.txt") as f:
                 d = f.readline()
                 print("[", str(getdate()), "]", d)


        else :
             with open("gourav-diet") as f:
                d = f.readline()
                print(d)
    elif a == 2 :
        b = int(input("Enter 1 for exercise and 2 for diet : "))
        if b == 1 :
            with open("arnav.txt") as f :
                d = f.readline()
                print(d)
        else :
            with open("arnav-diet") as f :
                d = f.readline()
                print(d)
    else :
        b = int(input("Enter 1 for exercise and 2 for diet : "))
        if b == 1:
            with open("harry.txt") as f:
                d = f.readline()
                print(d)
        else:
            with open("harry-diet") as f:
                d = f.readline()
                print(d)

while True :
    a = input("Enter 1 for gourav, 2 for arnav and 3 for harry and enter 'q' for exit : ")
    if a.lower() == 'q':
        exit()

    c = int(input("Enter 1 for log and 2 for entering data : "))
    a = int(a)
    if c == 1 :
        log_()
    else:
        edit_()


