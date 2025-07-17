students = [
    {"name":"raju","dept" :"cse","marks": [20,30,40]},
    {"name":"vijay","dept" :"cse","marks":[10,70,43]},
    {"name" : "pavi","dept" :"ece","marks":[22,38,56]},
    {"name": "pavi","dept" :"ece","marks":[26,36,89]},
    {"name" : "pavi","dept" :"ece","marks":[16,90,43]}
]
for i in  students:
    sum1 = sum(i["marks"])
    per=sum1/3
    i["per"] = per
print(students)

des=["FIRST","SECOND","THIRD","FOURTH","FIFTH"]
b=sorted(students,key=lambda x:x["per"],reverse=True)
index=0
for i in b:
    print("{}.{}stands{}:{:.2f}%".format(index+1,i["name"],des[index],i["per"]))
    index=index+1
