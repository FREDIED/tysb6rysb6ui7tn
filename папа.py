q = (int(input("?\n")))
w = (input('Только четные?\n'))
if w == "y":
    for number in range(q):
        if number % 2 == 0:
            print(number)
if w == "n":
    for number in range(q):
            print(number+1)
