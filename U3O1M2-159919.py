vineYards = []
weeklyHarvest = []
listTotal = []

O = open("weekly-harvest.txt", 'r')

def weeklyHarvestlist(listTotal):
    for list in listTotal:
        for value in list:
            try:
                weeklyHarvest.append(float(value))
            except ValueError:
                pass

def getProfit(sellAmount, costPrice, salePrice):
    profit = sellAmount*(salePrice-costPrice)
    return profit

def getVintage(totalGrapes):
    if totalGrapes > 100:
        return "Excellent grape harvest"
    elif 40 < totalGrapes < 100:
        return "Good grape harvest"
    elif totalGrapes < 40:
        return "Poor grape harvest"


def costPrice():
    Q = 1
    while Q == 1:
        V3 = 0
        try:
            W = float(input("Input the cost price: "))
        except ValueError:
            print("")
            print("Please input the cost price", '\n')
            V3 = 1
        if V3 != 1:
            if W < 0:
                print("")
                print("Please input the cost price", '\n')
                V3 = 1
        if V3 != 1:
            Q == 0
            return W
            break

def salePrice():
    Q = 1
    while Q == 1:
        V3 = 0
        try:
            W = float(input("Input the sale price: "))
        except ValueError:
            print("")
            print("Please input the sale price", '\n')
            V3 = 1
        if V3 != 1:
            if W < 0:
                print("")
                print("Please input the sale price", '\n')
                V3 = 1
        if V3 != 1:
            Q == 0
            return W
            break

costPrice = costPrice()

salePrice = salePrice()

for line in O:
    line = line.strip('\n')
    line = line.split(' ')

    vname = line.pop(0)
    listTotal.append([vname])
    print(listTotal)

    total = 0
    for i in line:
        total += float(i)

    lti = listTotal.index([vname])
    listTotal[lti].append(total)

O.close()

totalGrapes = 0

weeklyHarvestlist(listTotal)

for list in listTotal:
    for value in list:
        try:
            totalGrapes = totalGrapes + value
        except TypeError:
            pass

lenList = len(weeklyHarvest)

average = totalGrapes/lenList

lowest = 0
for list in listTotal:
    for value in list:
        try:
            if lowest > value:
                lowest = value
            elif lowest == 0:
                lowest = value
        except TypeError:
            pass

highest = 0
for list in listTotal:
    for value in list:
        try:
            if highest < value:
                highest = value
            elif highest == 0:
                highest = value
        except TypeError:
            pass

lowIndex = weeklyHarvest.index(lowest)

highIndex = weeklyHarvest.index(highest)

sellAmount = totalGrapes*(45/100)

profit = getProfit(sellAmount, costPrice, salePrice)

vintage = getVintage(totalGrapes)

print("")

print("Lowest total grapes was {0} with {1}t, Highest total grapes was {2} with {3}t".format(listTotal[lowIndex][0], listTotal[lowIndex][1], listTotal[highIndex][0], listTotal[highIndex][1]))

print("")

print("The profit is ${0} and it was a {1}".format(profit, vintage))

W = open("weekly-harvest1.txt", "w")

W.write("Stats for Gapes: ")

W.write("Average: {0}t, ".format(str(average)))

W.write("Vineyard lowest: {0} ".format(listTotal[lowIndex][0]))

W.write("with {0}t, ".format(str(listTotal[lowIndex][1])))

W.write("Vineyard highest: {0} ".format(listTotal[highIndex][0]))

W.write("with {0}t, ".format(str(listTotal[highIndex][1])))

W.write("Total profit: ${0}".format(str(profit)))

W.close()