def permute(s, ans=""):
    if len(s) == 0:
        print(ans)
        return
    for i in range(len(s)):
        permute(s[:i] + s[i+1:], ans + s[i])

s = input()
permute(s)
