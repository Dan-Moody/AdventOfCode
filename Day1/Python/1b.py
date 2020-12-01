# answer = 1006875
# Array for each number in the input file
array = []

sum = 2020

# Move each input number into an array and close the input stream once finished
with open('../input.txt') as f:    
    for line in f: # read each line
        array.append(int(line))


total = 0
i, j, k = 0, 0, 0
while i < len(array):
    temp = sum - array[i]
    j = i + 1
    # print("i: " + str(array[i]))
    while j < len(array):
        temp2 = temp - array[j]
        k = j + 1
        # print("j: " + str(array[j]))
        while k < len(array):
            # print("k: " + str(array[k]))
            if temp2 == array[k]:
                total = array[i] * array[j] * array[k]
                break
            k = k + 1
        j = j + 1
    i = i + 1

print(total)
