ids=[501,502,503,504]
#ids=list(map(int,input("Enter values here: ").split()))
ids.append(505)
print(ids)
ids.insert(4,506)
print(ids)
ids.pop(2)
print(ids)
ids.remove(502)
print(ids)
ids.reverse()
print("Reverse order list:",ids)
del ids[1]
print(ids)
