import random

n = random.randint(1, 10000)
print(n)
st = str(n)
l = len(st)
for j in range(0, 4):
    inp = int(input("Enter ur number"))
    p = str(inp)
    k = 0
    list1 = []
    for i in range(0, l):
        if (st[i] == p[i]):
            k += 1
            list1.append(st[i])
        else:
            list1.append("x")

    if (k == l):
        print("U picked the right number")
        break
    else:
        print(k, "digts are correct")
    for i in range(0, 4):
        print(list1[i], end=" ")
    print("\n")




