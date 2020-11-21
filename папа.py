q = (int(input("?\n")))
w = (input('Только четные?\n'))
if w == "y":
    for qq in range(q):
        if qq % 2 == 0:
            print(qq)
if w == "n":
    for qq in range(q):
            print(qq+1)
