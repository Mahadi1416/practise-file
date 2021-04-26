### first creat a text file from file then use like this
file_name="mahadi.txt"

with open (file_name) as f:
    lines = f.readlines()

name_s=""
for line in lines:
    name_s += line.strip()
    print(name_s)
    print(len(name_s))
    print(line.strip())
    print(line.split())

## create file with code
flle_name= "ratul.txt"

with open(flle_name,"w") as r:
    r.write("i love ratul")
    r.write("sa wew  ewrer e re r er e re r er ")




