# answer = 6662

total = 0 # of yes answers

# Open input for read
with open(".\input.txt") as f:   
    # Read each line
    yes = []
    for line in f: # New line is moving 1 down
        if line == '\n':
            # print("new line")
            # print(yes)
            total += len(yes)
            yes = []
        line = line.strip("\n")
        for char in line:
            if char not in yes:
                # print("here")
                yes.append(char)
total += len(yes)
        
print(total)