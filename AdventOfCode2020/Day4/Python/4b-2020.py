import re

# answer = 

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
with open(".\input.txt") as f:   
    # Read each line
    for line in f: # New line is moving 1 down
        if line == "\n":
            # print("End Passport")
            if byr and iyr and eyr and hgt and hcl and ecl and pid:
                sum += 1
            newPassport()
            
        else:
            line = line.split()
            for field in line:
                field = field.split(":")
                # byr (Birth Year) - four digits; at least 1920 and at most 2002.
                if field[0] == "byr":
                    if len(field[1]) == 4 and int(field[1]) >= 1920 and int(field[1]) <= 2002:
                        # print("1")
                        byr = True
                # iyr (Issue Year) - four digits; at least 2010 and at most 2020.
                elif field[0] == "iyr":
                    if len(field[1]) == 4 and int(field[1]) >= 2010 and int(field[1]) <= 2020:
                        # print("2")
                        iyr = True
                # eyr (Expiration Year) - four digits; at least 2020 and at most 2030.
                elif field[0] == "eyr":
                    if len(field[1]) == 4 and int(field[1]) >= 2020 and int(field[1]) <= 2030:
                        # print("3")
                        eyr = True
                # hgt (Height) - a number followed by either cm or in:
                # If cm, the number must be at least 150 and at most 193.
                # If in, the number must be at least 59 and at most 76.
                elif field[0] == "hgt": # could use regular expression library but I dont wanted to try withour in this part
                    num = re.split("[a-z]", field[1])
                    unit = re.split("[0-9]", field[1])
                    if unit[len(unit)-1] == "in":
                        # print("a")
                        if int(num[0]) >= 59 and int(num[0]) <= 76:
                            # print(4)
                            hgt = True
                    elif unit[len(unit)-1] == "cm":
                        # print("b")
                        if int(num[0]) >= 150 and int(num[0]) <= 193:
                            # print(5)
                            hgt = True

                # hcl (Hair Color) - a # followed by exactly six characters 0-9 or a-f.
                elif field[0] == "hcl": # Got lazy and am going to use regex
                    word = field[1]
                    if word[0] == "#" and len(word) == 7 and len(re.findall("[0-9,a-f]", word)) == 6:
                        # print("6")
                        hcl = True
                # ecl (Eye Color) - exactly one of: amb blu brn gry grn hzl oth.
                elif field[0] == "ecl":
                    if field[1] == "amb" or field[1] == "blu" or field[1] == "brn" or field[1] == "gry" or field[1] == "grn" or field[1] == "hzl" or field[1] == "oth":
                        # print("7")
                        ecl = True
                # pid (Passport ID) - a nine-digit number, including leading zeroes.
                elif field[0] == "pid":
                    if len(field[1]) == 9 and field[1].isdigit():
                        # print("8")
                        pid = True
                # cid (Country ID) - ignored, missing or not.
                elif field[0] == "cid":
                    cid = True 
    if byr and iyr and eyr and hgt and hcl and ecl and pid:
        sum += 1


print(sum)