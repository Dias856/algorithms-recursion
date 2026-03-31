def sum_array(arr, n):
    if n == 0:
        return 0
    return arr[n-1] + sum_array(arr, n-1)

n = int(input())
arr = list(map(int, input().split()))
print(sum_array(arr, n))
