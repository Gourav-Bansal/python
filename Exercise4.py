    # Printing a star pattern
n = int(input("Enter no. of rows you want : "))
print("Type 1 or 0")
b=int(input())
a = "*"
if b==1:
    for i in range(0, n):
        print(a)
        a = a + "*"
elif b==0:
    for i in range(n, 0,-1):
        a = i*"*"
        print(a)
else:
    print("Enter either 1 or 0 ")
