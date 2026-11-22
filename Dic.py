contacts={
    "siva":12345556,
    "satish":2752797,
    "kumar":98620992,
    "bhavani":62972000
}
print(contacts)

for key in contacts.keys():
    print("Keys:",key)

for value in contacts.values():
    print("values : ",value)

for key,value in contacts.items():
    print(f"Key : {key} , Value : {value}")
