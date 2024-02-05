x = input()
y = input()
lst1, lst2, newLst = [], [], []
for i in range(len(x)):
  if x[i] != " ":
    lst1.append(int(x[i]))
    lst2.append(int(y[i]))
for i in range(len(lst1)):
  for j in range(len(lst2)):
    newLst.append(lst1[i] * lst2[j])

print(newLst)
