#Set is not allow the duplicate elements.

num={1,2,3,4,5}
num.add(6)
print(num)
num.update([7,8,9])
num.remove(3)
print(num)
num.discard(4)#In here,if the value is not found then it is cannot return or show the error it is dislike the remove()
print(num)
num.clear()
print(num)
a={1,2,3,4,5}
b={5,3,4,5,5,1,2}
print(a.union(b))
print(a.difference(b))
print(a.intersection(b))