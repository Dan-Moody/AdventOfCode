# answer = 244
# right 3 down 1

sum = 0 # Number of trees you encounter

# Move each input number into an array and close the input stream once finished
with open(".\input.txt") as f:   
    # Read each line 
    width = 0 # How far to the right you are
    for line in f: # New line is moving 1 down
        line = line.strip('\n')
        # print(line.split())
        print("Location: " + str(width%(len(line))) + ", What's there: " + str(line[width%(len(line))]) + " width: " + str(width) + " line length: " + str(len(line)))
        # print(line)
        if line[width%(len(line))] == '#':
            sum += 1
        # print(line)
        width += 3

print(sum)