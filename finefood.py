def main():
    file_name = "foods.txt"
    total = 0
    prod = ""
    id = ""
    dict = {}
    file = open(file_name, "r",encoding='utf-8', errors='ignore')
    for line in file:
        line = line.split()
        if(len(line) >= 1):
            if(line[0] == "product/productId:"):
                dict[line[1]] = [0,0]
            #print(line[0])
    file.close()
    file = open(file_name, "r",encoding='utf-8', errors='ignore')
    for line in file:
        line = line.split()
        if(len(line) >= 1):
            if(line[0] == "product/productId:"):
                dict[line[1]][0] += 1
                id = line[1]
            if(line[0] == "review/score:"):
                dict[id][1] += float(line[1])
            #print(line[1])
    for line in dict:
        if(dict[line][0] >= 100):
            if(dict[line][1] / dict[line][0] > total):
                total = dict[line][1] / dict[line][0]
                prod = line
        #print(line)
    print(prod)
main()
