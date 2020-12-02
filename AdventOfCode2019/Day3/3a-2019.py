# answer = 

sum = 0

# Move each input number into an array and close the input stream once finished
with open(".\\testInput1.txt") as f:   
    # Starting positons
    start = [0,0]
    wire1Pos = [0,0]
    wire2Pos = [0,0]

    wire1PosNew = [0,0]
    wire2PosNew = [0,0]

    # List of all wire instructions
    wire1 = f.readline().split(',')
    wire2 = f.readline().split(',')

    for instrWire1 in wire1:
        direction = instrWire1[0]
        if direction == 'U': # Up 
            wire1PosNew[1] = wire1PosNew[1] + instrWire1[1:len(instrWire1)]
        if direction == 'D': # Down
            wire1PosNew[1] = wire1PosNew[1] - instrWire1[1:len(instrWire1)]
        if direction == 'L': # Left
            wire1PosNew[0] = wire1PosNew[0] - instrWire1[1:len(instrWire1)]
        if direction == 'R': # Right
            wire1PosNew[0] = wire1PosNew[0] + instrWire1[1:len(instrWire1)]
        

        for instrWire2 in wire2:
            direction = instrWire2[0]
            if direction == 'U': # Up 
                wire2PosNew[1] = wire2PosNew[1] + instrWire2[1:len(instrWire2)]
            if direction == 'D': # Down
                wire2PosNew[1] = wire2PosNew[1] - instrWire2[1:len(instrWire2)]
            if direction == 'L': # Left
                wire2PosNew[0] = wire2PosNew[0] - instrWire2[1:len(instrWire2)]
            if direction == 'R': # Right
                wire2PosNew[0] = wire2PosNew[0] + instrWire2[1:len(instrWire2)]

            maxXWire1 = max(wire1Pos[0], wire1PosNew[0])
            minXWire1 = min(wire1Pos[0], wire1PosNew[0])
            maxYWire1 = max(wire1Pos[0], wire1PosNew[0])
            minYWire1 = min(wire1Pos[0], wire1PosNew[0])

            maxYWire2 = max(wire2Pos[0], wire2PosNew[0])
            minYWire2 = min(wire2Pos[0], wire2PosNew[0])
            maxXWire2 = max(wire2Pos[0], wire2PosNew[0])
            minXWire2 = min(wire2Pos[0], wire2PosNew[0])
