def remove_duplicates(list):
    for x in range(0, len(list) - 1):
        for y in range(x + 1, len(list) - 1):
            if list[x] == list[y]:
                list.pop(y)
    return list


if __name__ == "__main__":
    myList = [1, 2, 3, 3, 4, 4, 5]
    print(remove_duplicates(myList))

