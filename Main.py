import csv
import matplotlib.pyplot as plt

def preProcess(doc):
    csv_reader = csv.reader(doc, delimiter = ",")
    line = 0
    data = {}
    for row in csv_reader:
        if line == 0:
            line+=1
            continue
        else:
            if row[0] in data:
                raise Exception
            else:
                data[int(row[0])]=[float(row[1]), float(row[2]), float(row[3]), float(row[4])]
                line+=1
    return data

def getUserData():
    print(
    """
    1: DAX Index
    2: SMI Index
    3: CAC Index
    4: FTSE Index
    """
    )
    good = False
    while not good:
        try:
            choice = int(input("Which one would You like to see: "))
            if choice < 1 or choice > 4:
                good = False
            else:
                good = True
        except ValueError:
            pass
    return choice - 1


def plotData(data):

    plt.plot(data[0], data[1], "r")
    plt.xlabel("Day")
    plt.ylabel("Price")
    plt.suptitle("Daily Closing Prices From 1991 - 1998")
    plt.show()

def generatePoints(data, userChoice):
    xList = []
    yList = []
    for day,prices in data.items():
        xList.append(day)
        yList.append(prices[userChoice])
    return (xList, yList)




def main():
    doc = open("EuStockMarkets.csv")
    data = preProcess(doc)
    choice = getUserData()
    points = generatePoints(data, choice)
    plotData(points)








if __name__ == "__main__":
    main()
