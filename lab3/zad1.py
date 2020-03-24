'''
ZnaleŸæ trójki liczb spe³niaj¹ce równanie
a**2 + b**2 = c**2
gdzie a, b i c to s¹ liczby naturalne (1,2,3,..).
np. jedna trójka to a=3, b=4, c=5. Rzeczywiœcie, 9 + 16 = 25.
ZnaleŸæ wszystkie trójki pod warunkiem, ¿e
1 <= a <= 100 oraz
1 <= b <= 100 oraz
a >= b.

Rozwi¹zaæ ten sam problem dla:
a**3 + b**3 = c**3
a**4 + b**4 = c**4
a**5 + b**5 = c**5
'''

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