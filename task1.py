def sum_of_squares(n):
    if n == 1:
        return 1
    return n*n + sum_of_squares(n-1)

n = int(input())
print(sum_of_squares(n))
