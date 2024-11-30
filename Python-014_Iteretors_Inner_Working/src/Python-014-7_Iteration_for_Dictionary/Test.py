myDict = {
    "a" : 1,
    "b" : 2,
}

for key in myDict.keys():
    print(key)



print("\n")



# Raw method:

myDict_iterator = iter(myDict)

print(myDict_iterator)
print(myDict_iterator.__next__())

print(myDict_iterator)
print(myDict_iterator.__next__())

# print(myDict_iterator)
# print(myDict_iterator.__next__())