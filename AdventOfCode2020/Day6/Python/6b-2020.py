# answer = 3382

total = 0 # of yes answers

# Open input for read
with open(".\input.txt") as f:   
    # Read each line
    yes = []
    temp = []
    i = 0
    for line in f: # New line is moving 1 down
        if line == '\n':
            total += len(yes)
            yes = []
            temp = []
            i = 0

        # Takes all the yes answers of the first person in a group
        elif i == 0:
            line = line.strip("\n")
            for char in line:
                if char not in yes:
                    yes.append(char)
            i += 1

        # Compares the yes answers of the current person to those of previous people and remembers the matches
        else:
            line = line.strip("\n")
            for char in line:
                if char in yes:
                    temp.append(char)
            yes = temp.copy()
            temp = []

# Adds the last group bc there is no empty line after it.
total += len(yes)
        
print(total)