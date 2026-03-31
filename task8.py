def generate(n, k, current=""):
    if n == 0:
        print(current.strip())
        return
    for i in range(1, k+1):
        generate(n-1, k, current + str(i) + " ")

n, k = map(int, input().split())
generate(n, k)
