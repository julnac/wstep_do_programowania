mylist = []
while True:
    a = input("Podaj wyraz: ")
    if a == "0":
        break
    mylist.append(a)

mylist.sort()

print(mylist)
