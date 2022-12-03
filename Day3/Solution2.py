def getLetterValue(letter):
    if ord(letter) > 96:
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26

f = open("input.txt","r")
lines = f.readlines()

priority_sum = 0
for i in range(0, len(lines), 3):
    set1 = set()
    set2 = set()
    set3 = set()

    #Group 1
    line = lines[i].replace("\n","")
    for letter in line:
        set1.add(letter)

    #Group 2
    line = lines[i+1].replace("\n","")
    for letter in line:
        set2.add(letter)

    #Group 3
    line = lines[i+2].replace("\n","")
    for letter in line:
        set3.add(letter)

    badge = set1.intersection(set2).intersection(set3)
    priority_sum += getLetterValue(list(badge)[0])
print(priority_sum)

    
