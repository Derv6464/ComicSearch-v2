def cleanCharacter():
    f = open("txt/characterLinks.txt","r")  
    d = open("csv/characterLinksClean.csv","w")
    dataIn = f.read()
    allLink = dataIn.split("\n")
    f.close()

    for i in range(len(allLink)):
        if "," in allLink[i]:
            allLink[i] = allLink[i].replace(",","^")
    
    c = 0
    for i in allLink:
        if "Category:" in i:
            c +=1
            print(i)

    print(len(allLink))
    for i in range(c):
        del allLink[0]
        
    print(len(allLink))
    
    for a in allLink:
        d.write(a + "\n")


    d.close()

def cleanComic():
    f = open("txt/comicLinks.txt","r")  
    d = open("csv/comicLinksClean.csv","w")
    dataIn = f.read()
    allLink = dataIn.split("\n")
    f.close()

    for i in range(len(allLink)):
        if "," in allLink[i]:
            allLink[i] = allLink[i].replace(",","^")

    c = 0
    for i in allLink:
        if "Category:" in i:
            c +=1

    print(len(allLink))
    for i in range(c):
        del allLink[0]
        
    print(len(allLink))
    
    for a in allLink:
        d.write(a + "\n")


    d.close()

def cleanNoEarthChars():
    f = open("txt/characterNoEarthLinks.txt","r")  
    d = open("csv/characterNoEarthLinksClean.csv","w")
    dataIn = f.read()
    allLink = dataIn.split("\n")
    f.close()

    for i in range(len(allLink)):
        if "," in allLink[i]:
            allLink[i] = allLink[i].replace(",","^")

    c = 0
    for i in allLink:
        if "Category:" in i:
            c +=1
            print(i)

    print(len(allLink))
    for i in range(c):
        del allLink[0]
        
    print(len(allLink))
    
    for a in allLink:
        d.write(a + "\n")


    d.close()


