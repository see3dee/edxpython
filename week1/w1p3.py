s = "abcbcd"

CurLong = s[0]
Longest = s[0]
for x in range(1, len(s)):
    if s[x] >= CurLong[-1]:
        CurLong += s[x]
        if len(CurLong) > len(Longest):
            Longest = CurLong
    else:
        CurLong = s[x]
print(Longest)