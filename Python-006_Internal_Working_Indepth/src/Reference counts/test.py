import sys

print(sys.getrefcount(24601))
print(sys.getrefcount(1))
print(sys.getrefcount('a')) #Compiler Optimization Loop
print(sys.getrefcount('apple'))