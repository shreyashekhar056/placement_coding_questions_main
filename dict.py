dict={'A': 1, 'B': 10, 'C': 100, 'D': 1000, 'E': 10000, 'F': 100000,}
ip = "ABCFDAABCC"
res=0
for i in ip:
    if (i in dict):
        res += dict[i]
print(res)  