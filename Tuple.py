#Tuple is ordered and immutable.So,we can't change after creation.
ages=(18,20,10,30)
print(ages)
#ages[0]=19
#print(ages)
count = ages.count(18)
print(f"Count of 18 in ages: {count}")
print(f"Index of 30 in ages: {ages.index(30)}")
