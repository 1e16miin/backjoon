word = str(input())

cnt = [0 for i in range(26)]
max = 0
temp = 0
idx = -1
num = 1
for i in range(len(word)):
    temp = ord(word[i])
    if temp >= 97:
       temp -= 32
    cnt[temp-65] += 1

for i in range(26):
    if max != 0 and cnt[i] == max:
        num += 1
    else:
        if cnt[i] > max:
            num = 1
            max = cnt[i]
            idx = i

if num != 1:
    print("?")
else:
    print(chr(idx+65))