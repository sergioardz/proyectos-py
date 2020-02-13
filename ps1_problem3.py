s = 'azcbobobegghakl'

subs = s[0]
lst = []
for i in range(len(s)-1):
    if s[i+1] >= s[i]:
        subs += s[i+1]
    else:
        lst.append(subs)
        subs = s[i+1]
lst.append(subs)
longest = max(lst, key=len)
print("Longest substring in alphabetical order is: " + longest)