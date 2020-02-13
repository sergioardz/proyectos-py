s = 'azcbobobegghakl'

aux = 'bob'

count = 0
for i in range(len(s)):
    if s[i:i+3] == aux:
        count += 1
print("Number of times bob occurs is: " + str(count))