def prime(n1):
    k=0
    for i in range(1, n1):
        if(n1 %i == 0):
            k+=1
    if(k==1):
        print("Prime")
    else:
        print("Not prime")


n=int(input("Enter the number:"))
prime(n)
