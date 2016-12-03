def main():
    file = open("sale_prices.txt", "r")
    count = 0
    original, sale, diff = 0,0,0
    for line in file:
        line = line.strip()
        for char in line.split():
            if count == 0:
                hold = 0
            if count == 1:
                hold = 0
            if count == 2:
                char = char.replace("$","")  
                char = char.replace("'","")
                char = char.replace(",","")
                char = char.replace("}","")
                char = char.replace("]","")
                original = float(char)
                print("Price: ", char)
            if count == 5:
                char = char.replace("$","")
                char = char.replace("'","")
                char = char.replace(",","")
                char = char.replace("}","")
                char = char.replace("]","")
                sale = float(char)
                print(" Discount: ", char)
                count = -1
                if(original - sale > diff):
                    diff = original - sale 
            count += 1
    print(diff)
main()
