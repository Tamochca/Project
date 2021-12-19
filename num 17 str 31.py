def numreverse(n):
    a = 0
    while (n > 0):
        a = a * 10 + n % 10
        n = n // 10
    return a


num_1 = int(input())
print(numreverse(num_1 ))