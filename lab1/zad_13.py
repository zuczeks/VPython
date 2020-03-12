#3
def perfNumber():
    count = 0 
    i = 0
    listOfNumbers = []    
    while True:
        if count == 4:
            break
        i = i+1
        listOfDiv = []
        for x in list(range(1,i)):
            if i % x == 0:  
                listOfDiv.append(x)
        if sum(listOfDiv) == i:
            listOfNumbers.append(i)
            count = count+1
    print(listOfNumbers)
    

perfNumber()

