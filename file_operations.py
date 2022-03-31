file = open("example.txt","r")

lines =0
words = 0

for line in file:
    line = line.strip("\n")
    word = line.strip()
    lines +=1
    words += len(word)
print("LINES:",lines,"WORDS",words)


