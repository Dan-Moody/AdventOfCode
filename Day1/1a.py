# answer = 1006875
# Array for each number in the input file
array = []

sum = 2020

# Move each input number into an array and close the input stream once finished
with open('input.txt') as f:    
    for line in f: # read each line
        array.append(int(line))


# print(array)

total = 0
i, j = 0, 0
while i < len(array):
    temp = sum - array[i]
    j = i + 1
    # print("i: " + str(array[i]))
    while j < len(array):
        # print("j: " + str(array[j]))
        if temp == array[j]:
            total = array[i] * array[j]
            break
        j = j + 1
    i = i + 1

print(total)
