#without list comprehension
fruits=["apple","banana","mango"]
new_list=[]
for i in fruits:
    if 'l' in i:
        new_list.append(i)
print(new_list)

#with list comprehension 
#Example-1
fruits=["apple","banana","mango"]
new_list=[i for i in fruits if 'l' in i]
print("new list:-",new_list)
#Example-2
salaries=[25000,36000,22000,23000,37000]
bonus=2500
Current_sal=[i+bonus for i in salaries]
print("Updated Salary List:",Current_sal)
