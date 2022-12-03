def getLetterValue(letter):
    if ord(letter) > 96:
        return ord(letter) - 96
    else:
        return ord(letter) - 64 + 26

f = open("input.txt","r")
lines = f.readlines()

priority_sum = 0
for line in lines:
    line = line.replace("\n","")
    first_half = line[:len(line)//2]
    sec_half = line[len(line)//2:len(line)]
    first_half_letters = set()
    for letter in first_half:
        first_half_letters.add(letter)
    for letter in sec_half:
        if letter in first_half_letters:
            priority_sum += getLetterValue(letter)
            break
print(priority_sum)

    
