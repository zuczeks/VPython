import math

f = open("Trios.txt", "w")

#maksymalne c dla kazdego przypadku rownania o n-tej potedze bedzie rowne n-temu pierwiastkowi z sumy n-tych poteg a i b (dodatkowo zaokraglenie w dol).
#dla n=2 maxC wynosi 141
#dla n=3 maxC wynosi 125
#dla n=4 maxC wynosi 118
#itd, widac tendencje spadkowa. 
#narzucilam wiec arbitralnie ograniczenie na c rowne 141. Dzieki temu program wykonuje sie w sensownym czasie.
maxC = 141

#dla wyzszych poteg
for i in range(2, 6):
    trios = []
    for b in range(1, 101):
        for a in range (b, 101):
            for c in range(a, maxC):
                if a**i + b**i == c**i:
                    trios.append([a,b,c])
    f.write("Trojki dla potegi" + str(i) + ':\n')
    f.write(str(trios) + '\n')
                    
f.close()