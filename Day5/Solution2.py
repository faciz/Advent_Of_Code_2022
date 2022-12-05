stacks = [['Z','P',"M",'H','R'],
          ['P','C','J','B'],
          ['S','N','H','G','L','C','D'],
          ['F','T','M','D','Q','S','R','L'],
          ['F','S','P','Q','B','T','Z','M'],
          ['T','F','S','Z','B','G'],
          ['N','R','V'],
          ['P','G','L','T','D','V','C','M'],
          ['W','Q','N','J','F','M','L']]

f = open("input.txt","r")
lines = f.readlines()

for line in lines:
    line = line.replace("\n","")
    line = line.split()[1::2]
    move = int(line[0])
    src = int(line[1]) - 1
    dest = int(line[2]) - 1

    stackHeight = len(stacks[src])
    crates = stacks[src][stackHeight-move:stackHeight]
    #print("crates to move: " + str(crates))
    stacks[src] = stacks[src][:stackHeight-move]
    #print("src now looks like: " + str(stacks[src]))
    stacks[dest] = stacks[dest] + crates
    #print("dest now looks like: " + str(stacks[dest]))

for stack in stacks:
    print(stack.pop(), end ="")
print()


    
