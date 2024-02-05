#Task 6


x = input()

for i in range(len(x)):
    if x[i] == " ":
        n = int(x[:i])
        k = int(x[i:])

z = input()
z += " "
lst = []
for j in range(len(z)):
    if z[j] == " ":
        lst.append(int(z[j-1]))

count = 0
for m in range(len(lst)):
    if (lst[m] + k) <= 5:
        count += 1
print(count // 3)
