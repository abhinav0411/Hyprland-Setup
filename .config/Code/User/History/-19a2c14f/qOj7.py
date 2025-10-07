count = 0
j = 3
s = "aababcabc"
for i in range(len(s) - j):
    sett = set()
    sett.add(s[i])

    if s[i+1] in sett:
        continue
    sett.add(s[i+1])

    if s[i+2] in sett:
        continue

    else:
        count += 1
    print(i)
print(count)