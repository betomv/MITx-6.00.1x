# To print number of times string 'bob' occurs in given string

bobCount = 0
for i in range(len(s) - 2):
    if s[i] == 'b' and s[i + 1] == 'o' and s[i + 2] == 'b':
        bobCount += 1

print ('Number of times bob occurs is:', bobCount)   
