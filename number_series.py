n=int(input("Find prime numbers upto:"))
print("\nAll prime numbers upto",n,"are:")
for j in range(2,n+1):
    i=2
    for i in range(2,j):
        if(j%i==0):
            i=j
            break;
    if(i!=j):
        print(j,end=" ")
