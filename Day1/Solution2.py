import heapq

f = open("input.txt","r")
lines = f.readlines()

currFood = 0
heap = []

for line in lines:
    line = line.replace("\n","")
    if line == "":
        heapq.heappush(heap, currFood)
        currFood = 0
    else:
        food = int(line)
        currFood += food

threeLargest = heapq.nlargest(3, heap)
print(sum(threeLargest))