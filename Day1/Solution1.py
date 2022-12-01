f = open("input.txt","r")
lines = f.readlines()

maxFood = 0
currFood = 0

for line in lines:
    line = line.replace("\n","")
    if line == "":
        if currFood > maxFood:
            maxFood = currFood
        currFood = 0
    else:
        food = int(line)
        currFood += food

print(maxFood)