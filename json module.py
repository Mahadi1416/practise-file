## save data
import json
numbers =[1,2,3,4,5,6,7,7]
file_name = "numbers.json"
with open (file_name,"w") as file_obj:
    json.dump(numbers,file_obj)
#load data
numbers =[1,2,3,4,5,6,7,7]
file_name = "numbers.json"
with open (file_name) as f:
    numbers = json.load(f)
print(numbers)

## saving with dump
import json
user_name = input("Write your name: ")

file_name = "user_name.json"
with open (file_name,"w") as f_n:
    json.dump(user_name,f_n)
    print("we will remember " + user_name + ". when you will come back")

## reading with load
file_name = "user_name.json"
with open(file_name) as f:
    user_name=json.load(f)
    print("Well come back " + user_name)

## if we give a new file name it will open a new file other wise it will givw the exist file result

import json

file_name = "user_name.json"
try:



    with open(file_name) as file_obj:
        user_name = json.load(file_obj)
except FileNotFoundError:
    user_name = input("Write your name: ")

    file_name = "user_name.json"
    with open(file_name, "w") as f_n:
        json.dump(user_name, f_n)
        print("we will remember " + user_name + ". when you will come back")

else:
    print("Well come back " + user_name)
