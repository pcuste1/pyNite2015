def main():
    file = open("shakes.txt", "r")
    list = []
    for line in file:
        for char in line.split():
            for word in char.split():
                if(word[0] not in ",./<>?;':\"[]{}|1234567890!@#$%^&*()_+-=`~"):
                    list.append(word.lower())
                
    print(list)

main()
