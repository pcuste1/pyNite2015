def pal(word):
    if(word != word[-1:0]):
        return

def main():
    file = open("113809of.fic","r")
    count = 0
    for line in file:
        line = line.strip()
        if (line == line[::-1] and len(line) % 2 != 0):
            count += 1
    print(count)
    
main()
