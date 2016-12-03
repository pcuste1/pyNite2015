def ana(line):
    a,p,l,e = 0,0,0,0
    for c in line:
        if (c == "a"):
            if(a == 1):
                return False
            a += 1
        elif (c == "p"):
            if(p == 2):
                return False
            p += 1
        elif (c == "l"):
            if(l == 1):
                return False
            l += 1
        elif (c == "e"):
            if(e == 1):
                return False
            e += 1
        else:
            return False
    if(a == 1 and p == 2 and l == 1 and e == 1):
        return True
                
def main():
    file = open("text.txt", "r")
    list = []
    for line in file:
       if ana(line.strip()):
           list.append(line)
    for line in list:
           print(line, end= " ")

main()
