f = open("csv/characterLinksClean.csv","r")
dataIn = f.read()
chars = dataIn.split("\n")

def find(L, target):
    start = 0
    end = len(L) - 1
    
    while start <= end:
        middle = (start + end)// 2
        midpoint = L[middle]
        if midpoint > target:
            end = middle - 1
        elif midpoint < target:
            start = middle + 1
        else:
            return middle
        
print(find(chars,"/wiki/Snorth_(Earth-616)"))
        