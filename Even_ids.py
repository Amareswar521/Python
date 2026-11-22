ids=[501,502,503,504,505,506]
even_ids=[]
odd_ids=[]
for i in ids:
    if i%2==0:
        even_ids.append(i)
    else:
        odd_ids.append(i)
print("Even ids : ",even_ids)
print("Odd ids : ",odd_ids)