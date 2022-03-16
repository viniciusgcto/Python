
n = int(input())
for i in range(n):
    num = int(input())
    sum = 0

    for j in range(1, (num+1)):
        if num%j == 0:
            sum = sum + 1
    if sum != (2):
        print(num,"nao eh primo")

    else:
        print(num,"eh primo")