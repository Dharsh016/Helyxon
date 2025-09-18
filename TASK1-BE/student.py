import json
students=[
    {'name':'dharsh','age':21},{'name':'sam','age':20},{'name':'tom','age':25}]
stu_sort=sorted(students,key=lambda x:x['age'])
with open('stu_sort.json','w') as f:
    json.dump(stu_sort,f,indent=4)
print("Students sorted by age")
for i in stu_sort:
    print(i)

