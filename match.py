n=int(input("no of teams"))
teams=[]
for i in range(n):
    a=input("enter team name")
    teams.append(a)
meet=int(input("enter no of meeting bw pairs"))

    
            
match=[]
for i in range(n-1):
    for j in range(i+1,n):
        for i in range(meet):
            match.append([teams[i],teams[j]])

print("-------")
index=1
for i in match:
    print("match {}:{} vs {}".format(index,i[0],i[1]))
    index=index+1