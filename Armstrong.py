#check whether the given number is armstrong ot not
num=int(input("Enter number here :-"))
temp=num
sum_of_cubes=0
while num>0:
    digit=num%10
    sum_of_cubes+=digit**3 #sum_of_cubes=sum_of_cubes+digit**3
    num=num//10
if temp==sum_of_cubes:
    print("Given number is armstrong")
else:
    print("Given number is not armstrong")
