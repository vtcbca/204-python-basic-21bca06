a=int(input("Enter any number:"))
b=1
while(b<10):
    if(a%b==0):
        print("{} is divisible by {}".format(a,b))
    b=b+1
