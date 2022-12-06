f = open("input.txt","r")
lines = f.readlines()
line = lines[0]

charSet = set()
i = 0
j = 0
while j < len(line):
    if len(charSet) == 4:
        print(j)
        break
    elif line[j] in charSet:
        charSet.remove(line[i])
        i+=1
    else: 
        charSet.add(line[j])
        j+=1

    
