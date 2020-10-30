a = input()
b = len(a)
c = []
d = ""
for i in range(b):
    #if i == " ":
        #continue
    c.append(a[b-1-i])
    d = d + c[i]
print(d)
