#tuple is immutable
#ordered
#()
#traversal and indexing
#{}
#doesnt allow duplivcates
#unordered



#a=[4,5,6,78,9]
#a[1]=100
#print(a)

#a={2,2,2,2,23,4,5,55,5}
#print(a)

#no indexing
#set no indexing

#a={1,2,3,4,5,6}
#b={3,4,5,6,7,8,9}
#print(a & b)
#print(a - b)
##print(b-a)
#print(a^b)

#stu={"name":"SACHIN","age":54,"runs":536}
#stu["name"]="RAJU"
#print(stu)

#stu={"name":"SACHIN","age":54,"runs":536}
#@for i in stu.keys:

#stu={"name":"SACHIN","age":54,"runs":536}
#stu["married"]=True
#print(stu)

#student={"name":"Adhvik","marks":[30,50,54,67,90]}
#print(student["marks"][2])


student= [{"name":"Adhvik","marks":[30,50,54,67,90]},
          {"name":"Adharsh","marks":[30,50,54,67,93]},
          {"name":"nik","marks":[30,50,51,66,95]}]
print(student[0]["marks"][0])
print(student[1]["marks"][1])
print(student[2])