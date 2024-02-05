#Task 4

x = ""
while x != "STOP":
    lst1 = []
    x = input()
    if x != "STOP":
        x += " "
        y = ""
        for i in range(len(x)):
            if x[i] == " ":
                lst1.append(int(y))
                y = ""
            else:
                y += x[i]
        lst2 = []
        for i in range(len(lst1) - 1):
            lst2.append(abs(lst1[i] - lst1[i + 1]))
        flag = True
        for j in range(1, len(lst1)):
            if j not in lst2:
                flag = False
        if flag:
            print("UB Jumper")
        else:
            print("Not UB Jumper")
