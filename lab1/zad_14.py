# Describe the given number in terms of parity and being the prime number
def numberDesc():
    nb = input('Podaj liczbe:')
    if nb % 2 == 0:
        print ("Liczba jest parzysta")
    else:
        if nb == 1:
            print ("Liczba jest nieparzysta")
        else: 
            check = 0;
            for x in list(range(2,nb/2)):
                if nb % x == 0:
                    print ("Liczba jest nieparzysta")
                    check = 1
                    break
                else:
                    continue
            if check == 0:
                print ("Liczba jest pierwsza")

numberDesc()


            
    
