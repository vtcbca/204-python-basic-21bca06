n=int(input("Enter any number:"))
no=1
for a in range(0,n):
    for b in range(0,a+1):
        print(no,end=' ')
        no=no+1
    print()
