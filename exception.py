## first practice
try:
    result = 6 // 3
    print(result)


except ZeroDivisionError:
    print("division by zero is not possible")

## using accept prevent craces
try:
    print("Give two number i will devide them")
    print("Type q to quit the game")

    while True:
        F_n = input("First number: ")
        if F_n == "q":
            break
        S_n = input("Second number: ")
        if S_n == "q":
            break

        else:
            result = int(F_n)/int(S_n)
        print(result)
        break
except ZeroDivisionError:
    print("Devide by zero is not possible.Please another number")

### file not found crases
flle_name= "ratul.txt"

try:
    with open(flle_name,"w") as r:
        name = r.read()

except:
    msg = "Sorry,The file " + flle_name + " doesn,t exit"
    print(msg)



