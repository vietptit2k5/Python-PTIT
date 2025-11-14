s = str(input())
tmp = s[len(s)-3:len(s)]
tmp = tmp.lower()
print("yes" if tmp == ".py" else "no")