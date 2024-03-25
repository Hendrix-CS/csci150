s = "robot"
print(s[2:])

for c in s:
    if c != 'o':
        print(c)

s = "taxation"
n = 0
for c in s:
    if c == 'a':
        n += 1
print(n)

s = "balloon"
for i in range(len(s) - 1):
    if s[i] == s[i + 1]:
        print(s[i])
