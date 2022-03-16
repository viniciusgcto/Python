X = 3
Y = 2

if (Y > X):
    for i in range(X + 1, Y - 1):
        if (i % 5 == 2) or (i % 5 == 3):
            print(i)
elif (X > Y):
    for i in range(Y + 1, X - 1):
        if (i % 5 == 2) or (i % 5 == 3):
            print(i)
