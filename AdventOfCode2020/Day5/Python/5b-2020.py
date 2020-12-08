import math
# answer = 564

mySeat = 0 # Of correct passports
fullSeats = []
# Open input for read
with open(".\input.txt") as f:   
    # Read each line
    for line in f: # New line is moving 1 down
        line = line.strip("\n")
        rows = [0,127]
        cols = [0,7]
        
        for i in range(0,7):
            char = line[i]
            # print(i)
            if char == "F":
                rows[1] = math.floor((rows[0]+rows[1])/2)
            if char == "B":
                rows[0] = math.ceil((rows[0]+rows[1])/2)
            # print(rows)
        
        for i in range(7,10):
            char = line[i]
            
            if char == "L":
                cols[1] = math.floor((cols[0]+cols[1])/2)
            if char == "R":
                cols[0] = math.ceil((cols[0]+cols[1])/2)
            # print(cols)

        seatID = (rows[0] * 8) + cols[0]
        fullSeats.insert(seatID, seatID)
        # print(seatID)

        # print("Rows: " + str(rows) + " Cols: " + str(cols) + " seatID: " + str(seatID))


fullSeats.sort()
print(fullSeats)
temp = 0
prev = 0
for x in fullSeats:
    # print("x: " + str(x) + " prev: " + str(prev))
    if temp == 0:
        prev = x
    elif x > (prev + 1):
        print("2x: " + str(x) + " prev: " + str(prev))
        # break
    prev = x
    temp += 1
    

# print(fullSeats)