# answer = 

# Sum for the 2 sum problem
sum = 0

# Move each input number into an array and close the input stream once finished
with open(".\input.txt") as f:   
    # Read each line 
    for line in f: 
        count = 0
        # Breaks the string into the 3 important sections and remove trailing newline
        fuelNum = int(line.rstrip('\n'))
        sum = sum + (int(fuelNum/3) - 2) # could use math.trunc() but int faster

print(sum)