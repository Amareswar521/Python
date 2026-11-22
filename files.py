with open("demo.txt","r") as f:
    content=f.readline(2)#f.read()
    print("Content of the file is : ",content)

with open("demo.txt","w") as f:
    f.write("This is a demo file")
    print("File written successfully")

with open("demo.txt","r") as f:
    content=f.read()
    print(content)
    
with open("demo.txt","a") as f:
    f.write("\n hello world")
    print("File written successfully.")

with open("demo.txt","r") as f:
    content=f.readlines()#it is returning a list of lines in the file
    print(content)
    
with open("demo.txt","r+") as f:#read write -modfying file also existing files
    content=f.read()
    print(content)
    f.write("\n good morning.")
    print("file written successfully.")

with open("demo.txt","r") as f:
    content=f.read()
    print(content)

with open("demo.txt","w+") as f: #w+ is erased old data in file.it is perform write and read operatons ,new files.
    f.write("\n today topic is file handling")
    print("file is written successfully.")
    print(f.read())
    
with open("demo.txt","r") as f:
    content=f.read()
    print(content)
    
with open("demo.txt","r+") as f:
    f.seek(0)
    f.write("hi")
    print("file is written successfully.")
    
with open("demo.txt","r") as f:
    content=f.read()
    print(content)

with open("demo.txt","a+")as f:
    f.seek(0)
    f.write("\n python")
    print("file written succefully")

with open("demo.txt","r") as f:
    content=f.read()
    print(content)





