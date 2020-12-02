# answer = 5070541
# Used recursion bc I could

# Sum for the 2 sum problem
sum = 0

def calculate(fuels):
    num = (int(fuels/3) - 2)
    if num > 0:
        temp = calculate(num)
        num = num + temp
        return num
    return 0

# Move each input number into an array and close the input stream once finished
with open(".\input.txt") as f:   
    # Read each line 
    for line in f: 
        fuelNum = int(line.rstrip('\n'))
        temp = (int(fuelNum/3) - 2) # could use math.trunc() but int faster
        sum = sum + temp + calculate(temp)


print(sum)