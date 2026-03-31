def reverse_strings(n):
    if n == 0:
        return
    s = input()
    reverse_strings(n-1)
    print(s)

n = int(input())
reverse_strings(n)
