def cap(myStr):
    newStr = ""
    marks = ".!?"
    i = 0
    while (i < len(myStr)):
        if i == 0:
            if 97 <= ord(myStr[i]) <= 122:
                newStr += chr(ord(myStr[i]) - 32)
                i += 1
        if myStr[i] in marks and i != (len(myStr) - 1):
            newStr += myStr[i]
            i += 2
            if 97 <= ord(myStr[i]) <= 122:
                newStr += " " + chr(ord(myStr[i]) - 32)
                i += 1
        elif myStr[i] == "i":
            if myStr[i-1] == " " and myStr[i+1] == " ":
                newStr += "I"
                i += 1
            else:
                newStr += myStr[i]
                i += 1
        else:
            newStr += myStr[i]
            i += 1
    print(newStr)

cap("this is a sample text. i wrote it to give it a test.")
