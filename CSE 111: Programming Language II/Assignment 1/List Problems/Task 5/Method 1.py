#Task 5

s = input()
upp, low, oddDig, evenDig = "", "", "", ""

for i in range(len(s)):
    if 65 <= ord(s[i]) <= 90:
        upp += s[i]
    elif 97 <= ord(s[i]) <= 122:
        low += s[i]
    else:
        if int(s[i]) % 2 == 0:
            evenDig += s[i]
        else:   
            oddDig += s[i]

def sortStr(givenStr):
    lst = []
    sortedStr = ""
    for i in range(len(givenStr)):
        lst.append(ord(givenStr[i]))
    for i in range(len(lst)):
        for j in range(i, len(lst)):
            if lst[j] < lst[i]:
                temp = lst[i]
                lst[i] = lst[j]
                lst[j] = temp
    for k in range(len(lst)):
        sortedStr += chr(lst[k])
    return sortedStr

upp = sortStr(upp)
low = sortStr(low)
evenDig = sortStr(evenDig)
oddDig = sortStr(oddDig)

print(low + upp + oddDig + evenDig)
