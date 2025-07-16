#a=[1,2,3,4,5,6,"virat"]
#print(a[2:5])

#a=[1,2,3,4,5,6,"virat"]
#for i in a:
    #print(i)

#a=[20,14,15,16,17,27]
#print(sum(a))

#a=[20,14,15,16,17,27]
#print(a.count(27))

#a=[20,14,15,16,17,27]
#a.sort()
#print(a)

#a=[20,14,15,16,17,27]
#a.insert(2,500)
#print(a)

#a=[20,14,15,16,17,27]
#a.insert(2,500)
#a.remove(14)
#a.pop()
#print(a)

#a=[20,14,15,16,17,27]
#a.clear()
#print(a)

#a=[20,14,15,16,17,27]
#b=[20,14,15,16,17,27]
#print(a+b)

names=[]
for i in range(5):
    a=input("Enter name{}".format(i+1))
    names.append(a)

index=1
for i in names:
    print("{}.Mr/Ms {}".format(index,i))
    index=index+1

    