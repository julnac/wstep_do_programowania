try:
    print(x)
except NameError:
    print("NameError")

try:
    result = 10 / 0
except ZeroDivisionError:
    result = 0

try:
    int("invalid")
except ValueError:
    print("ValueError")

try:
    lst = [1, 2, 3]
    print(lst[4])
except IndexError:
    print("IndexError")

try:
    with open("nonexistentfile.txt") as f:
        print(f.read())
except FileNotFoundError:
    print("FileNotFoundError")

try:
    open("existingfile.txt", "x")
except FileExistsError:
    print("FileExistsError")

try:
    "hello" + 5
except TypeError:
    print("TypeError")

try:
    object().attribute
except AttributeError:
    print("AttributeError")

try:
    dct = {"key": "value"}
    print(dct["nonexistent_key"])
except KeyError:
    print("KeyError")
