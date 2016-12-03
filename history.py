def main():
    file = open("machistory.txt", "r")
    numadded = 0
    total = 0
    for line in file:
        for word in line.split():
            letters = 0
            word.strip()
            if word[0] == "M" or word[0] == "m" and len(word) >= 2:
                for char in word:
                    if char not in "1234567890":
                        letters += 1
                print(word, "  :  ", letters, " : ", total)
                numadded += 1
            total += letters
           
    print(total / numadded)

main()
