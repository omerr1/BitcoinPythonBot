

FILE_NAME = "BTC_DATA.csv"
SELECT_LAST = 120

CAPITAL = 100

THRESHOLD = 0.015


def main():
    total = CAPITAL
    while(True):

        buyprice=0
        sellprice=0

        while(True):
            data = getData()
            change = calculatePre(data,data[0])
            if (change > THRESHOLD):
                buyprice = data[len(data) - 1]
                break
        
        while(True):
            data = getData()
            change = calculatePre(data,buyprice)
            if (abs(change) > THRESHOLD):
                sellprice = data[len(data) - 1]
                break
        
        diff = (buyprice - sellprice) * (CAPITAL / buyprice)
        total += diff
        print("Current Trade: " + str(diff) +  " | Total Asset Value: " + str(total))
    
def getData():
    with open(FILE_NAME, 'r+') as f:
        data =  f.read()
    data.strip()
    data = list(data.split("\n"))
    data.remove(data[len(data)-1])
    data_float = [float(x) for x in data]
    return data_float[-SELECT_LAST:]

def calculatePre(data,num):
    return  100 * (data[len(data)-1] - num) /  num 

if __name__ == "__main__":
    main()
