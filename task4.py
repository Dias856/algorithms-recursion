def power(b, n):
    if n == 0:
        return 1
    return b * power(b, n-1)

def sum_powers(b, n):
    if n == 0:
        return 1
    return power(b, n) + sum_powers(b, n-1)

b = int(input())
n = int(input())
print(sum_powers(b, n))
