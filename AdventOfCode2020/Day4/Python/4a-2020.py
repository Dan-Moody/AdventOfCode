# answer = 200

# byr (Birth Year)
# iyr (Issue Year)
# eyr (Expiration Year)
# hgt (Height)
# hcl (Hair Color)
# ecl (Eye Color)
# pid (Passport ID)
# cid (Country ID) (optional)

sum = 0 # Of correct passports

byr = False
iyr = False
eyr = False
hgt = False
hcl = False
ecl = False
pid = False
cid = False # (optional)

# Resets all the passport fields
def newPassport():
    global byr
    byr = False
    global iyr
    iyr = False
    global eyr
    eyr = False
    global hgt
    hgt = False
    global hcl
    hcl = False
    global ecl
    ecl = False
    global pid
    pid = False
    global cid
    cid = False # (optional)

# Open input for read
with open(".\input2.txt") as f:   
    # Read each line
    for line in f: # New line is moving 1 down
        if line == "\n" :
            # print("End Passport")
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                sum += 1
            newPassport()
            
        else:
            line = line.split()
            for field in line:
                field = field.split(":")
                # print(field)
                if field[0] == "byr":
                    byr = True
                elif field[0] == "iyr":
                    iyr = True
                elif field[0] == "eyr":
                    eyr = True
                elif field[0] == "hgt":
                    hgt = True
                elif field[0] == "hcl":
                    hcl = True
                elif field[0] == "ecl":
                    ecl = True
                elif field[0] == "pid":
                    pid = True
                elif field[0] == "cid":
                    cid = True 
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        sum += 1

print(sum)