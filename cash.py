# input is in dollars
# 1c, 10c, 25c, 50c
# print min num of coins
# try totalling, go through list chosing max possible value

def get_change():
    while True:
        try:
            change = float(input("Change owed ($): "))
            if change > 0:
                return change
        except ValueError:
            ...

def main():
    change = get_change()*100

    cents = [25,10,5,1]
    counter = 0
    total = 0
    coins = []
    while total != change:
        if cents[0]+total <= change:
            total+=cents[0]
            coins.append(25)
        elif cents[1]+total <= change:
            total+=cents[1]
            coins.append(10)
        elif cents[2]+total <= change:
            total+=cents[2]
            coins.append(5)
        else: 
            total+=cents[3]
            coins.append(1)
        counter += 1

    print("Number of coins: ",counter)
    print(coins)

main()