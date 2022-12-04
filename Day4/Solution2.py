#6-8,5-10

f = open("input.txt","r")
lines = f.readlines()

total = 0
for line in lines:
    line = line.replace("\n","")
    line = line.split(",")
    assignmentOne = [int(i) for i in line[0].split("-")]
    assignmentTwo = [int(i) for i in line[1].split("-")]

    if assignmentOne[0] >= assignmentTwo[0] and assignmentOne[0] <= assignmentTwo[1]:
        total += 1
    elif assignmentOne[1] >= assignmentTwo[0] and assignmentOne[1] <= assignmentTwo[1]:
        total += 1
    elif assignmentTwo[0] >= assignmentOne[0] and assignmentTwo[0] <= assignmentOne[1]:
        total += 1
    elif assignmentTwo[1] >= assignmentOne[0] and assignmentTwo[1] <= assignmentOne[1]:
        total += 1
print(total)