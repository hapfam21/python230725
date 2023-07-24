# demoindexing.py
strA = 'python is very powerful'
print(strA[0])
print(strA[1])
print(strA[0:3])
print(strA[:3])
print(strA[-3:])
print(strA[-8:])

colors = ["red", "blue", "green"]
print(colors)
print(len(colors))
print(colors[0])

for item in colors:
    print(item)

colors.append("white")
print(colors)
colors.insert(1,"pink")
print(colors)
colors += "red"
print(colors)
print(colors.pop())
print(colors.pop())
print(colors.pop(1))
print(colors)
colors.extend(["black", "red", "pink", "white"])
print(colors)
colors.remove("black")
print(colors)
colors.sort()
print(colors)
colors.reverse()
print(colors)