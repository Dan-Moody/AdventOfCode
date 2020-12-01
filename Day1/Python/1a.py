# answer = 1006875
# Array for each number in the input file
array = []

# Sum for the 2 sum problem
sum = 2020

# Move each input number into an array and close the input stream once finished
with open(".\input.txt") as f:    
    for line in f: # read each line
        array.append(int(line))

#---------------------------------------------------------------------

# Checks every value pair until a match is found
# Time complexity: n^2
def bruteForce():
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
                return total
            j = j + 1
        i = i + 1
    return total 

# Use hashtable to search for corrssponding value to achieve sum
# Time complexity: O(n)
def hashing():
    hashtable = {}
    for i in range(len(array)):
        difference = sum - array[i]
        if difference in hashtable:
            return array[i] * difference
        hashtable[array[i]] = array[i]
    return 0 # not found

# sorting O(n log n)

# use different algorithms
# print( bruteForce() )
print( hashing() )
