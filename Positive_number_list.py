#Positive and negative numbers
nums=list(map(int,input().split()))
positive_numbers=[]
negative_numbers=[]
for i in nums:
    if i>0:
       positive_numbers.append(i)
    else:
       negative_numbers.append(i)
print("Positive numbers in the list are : ",positive_numbers)
print("Negative numbers in the list are : ",negative_numbers)
