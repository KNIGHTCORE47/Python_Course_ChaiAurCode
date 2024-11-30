# NOTE - File in Python

# File in for loop

for line in open("../DEMO.py"):
    print(line, end="")



print("\n")



# File in while loop and not operator

f = open("../DEMO.py")

while True:
    line = f.readline()
    if not line:
        break
    print(line, end="")
