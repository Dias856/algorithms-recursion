def is_power(n):
    if n == 1:
        return True
    if n == 0 or n % 2 != 0:
        return False
    return is_power(n//2)

for i in range(33):
    if is_power(i):
        print(i, "is a power of two")
    else:
        print(i, "is not a power of two")
