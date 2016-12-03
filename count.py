def main():
    file = open("fairy.txt", "r")
    tot = 0
    for line in file:
        tot += 1
    print(tot)

main()
