
try:
    a,b=map(int,input("Enter values here: ").split())
    c=a/b
except ZeroDivisionError:
    print("Error occured")
    print("cannot divide by zero")
   
#multiple exceptions
try:
   a,b=map(int,input("Enter values here: ").split())
   result=(a/b)
except ValueError:
    print("Please enter numbers only")
except ZeroDivisionError:
    print("Cannot divide by zero")
else:
    print("Result : ",result)
#finally it is excuted error occured or not it is always run
finally:
    print("program complted")

#raise it is used to create custom exceptions in the program
#we can create own exceptions uising this
class Ageerror(Exception):
    pass
age=15
try:
    if age<18:
        raise Ageerror("Age must be 18 or above")
except Ageerror as e:
    print(e)

# as e allows us to store exception object and display its message
try:
    print(10/0)
except ZeroDivisionError as e:
    print("Error : ",e)
    

#Specific Exceptions are Type error,index error,Zerodivisionerror,valueerror,keyerror.
try:
    user_pwd="code521"
    password=input("Enter password here : ")
    if user_pwd!=password:
        raise ValueError("Incorrect password")
except ValueError as e:
    print("Error : ",e)
else:
    print("Login Successfully")

try:
    age=int(input("Enter your age :"))
    if age!=20:
        raise ValueError("Not elligible for this job")
except ValueError as e:
    print("Error",e)
else:
    print("you are eligible for this job")

try:
    with open("demo.txt","r") as f:
        print(f.read())
except FileNotFoundError as e:
    print(e)
else:
    print("file read successfully")
