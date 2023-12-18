mylist = ["ada", "ryba", "graty", "tirexy"]

for x in range(0, 2*len(mylist), 2):
    length = str(len(mylist[x]))
    mylist.insert((x + 1), length)

mytuple = tuple(mylist)
print(mytuple)
