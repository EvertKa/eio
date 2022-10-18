inputNum = input ()
inputString = input ()
indexes = []
steps = []

for i in range(len(inputString)) :
    if inputString[i] == "n":
        indexes.append(i + 1)
    else:
        if len(indexes) != 0:
            steps.append(str(indexes[0]) + "-" + str(indexes[-1]))
            indexes.clear()

print(len(steps))
for step in steps:
    print(step)