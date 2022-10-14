import random
f = open("csv/comicLinksClean.csv","r")

dataIn = f.read()
list1 = dataIn.split("\n")

def getRand(times):
    links = []
    for i in range(times):
        link = random.choice(list1)
        if "^" in link:
            print(link.replace("ˆ",","))
            links.append(link.replace("ˆ",","))
        else:
            print(link)
            links.append(link)
    return(links)
    