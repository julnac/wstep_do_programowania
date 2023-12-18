mylist1 = ["babel", "boryna", "bagatela","boom", "amory","anno"]
mylist2 = ["abba", "ala", "amory","anno"]
mylist3 = []
for item_1 in mylist1:
    for item_2 in mylist2:
        if item_1 == item_2:
            mylist3.append(item_1)

print(mylist3)

