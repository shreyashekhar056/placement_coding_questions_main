def prime(i):
    if(i==1):
        return False
    for j in range(2,i):
        if(i%j==0):
            return False
    return True

def sod(i):
    d=list(str(i))
    x=sum([int(i) for i in d])
    if(prime(x)):
        return True
    else:
        return False

def dig(i):
    while(i>0):
        d=i%10
        i=i//10
        if(prime(d)):
            return False
        i=i/10
    return True


for i in range(100,1000):
    if(prime(i) and sod(i) and dig(i)):
        print(i)