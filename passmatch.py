def main():
    file = open("passwords.txt", "r")
    for line in file:
        line = line.strip()
        up, low, dig, special = 0,0,0,0
        for char in line:
            charc = ord(char)
            if charc >= 48 and charc <= 57:
                dig += 1
            elif charc  >= 97 and charc <= 122:
                low += 1
            elif charc >= 65 and charc <= 90:
                up += 1
            elif char not in "!@%#$&?":
                print(char)
                hold = 0
            else:
                special += 1
        if(len(line) > 9 and len(line) < 15):
            if(up >= 4 and low == 2):
                if (dig == 3):
                    if(special == 2):
                        print(line)
                    # print(line)
                # print(line)
           # print(line)
            
        
main()
