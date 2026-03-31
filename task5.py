def reverse_numbers(n):
    if n == 0:
        return
    x = int(input())
    reverse_numbers(n-1)
    print(x, end=" ")

n = int(input())
reverse_numbers(n)
