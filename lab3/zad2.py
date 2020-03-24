'''
B³¹dzenie przypadkowe.

Mniej wiêcej na œrodku ekranu piszemy START.
W kolejnej lini wypisujemy gwiazdkê *.
Idziemy do kolejnej linii.

Rzucamy monet¹.
Na monecie jest +1 i -1 Jak +1 to robimy krok w prawo na ekranie. Tzn. robimy spacje w prawo i wypisujemy *. Jak -1 to robimy krok w lewo, tzn. idziemy o spacje w lewo i wypisujemy *.
Idziemy do kolejnej linii i robimy to samo. Proszê spojrzeæ na rysunek.

              START
|                  *                  | 0
|                   *                 | +1
|                    *                | +2
|                     *               | +3
|                    *                | +2


Tutaj 3 razy poszliœmy w prawo i na koñcu w lewo. Liczba na koñcu ka¿dego wiersza mówi jak daleko jesteœmy od zera.

Po lewej i prawej stronie rysujemy œciany |. Jak gwiazdka uderzy jedn¹ ze œcianek to koniec programu.
Program rysuje ca³¹ œcie¿kê jak wy¿ej oraz na koñcu wypisuje ile razy rzuciliœmy monet¹.

Odleg³oœæ od œcianki do œcianki to 20 spacji.
'''

import random
f = open("Track.txt", "w")
f.write('       START         \n')
f.write('|         *          |0\n')

actual = 10
maximum = 20
moves = 0
while actual<20 and actual>1:
    move = random.randint(0,1)
    if move==0:
        actual = actual - 1
    else:
        actual = actual + 1
    f.write('|')
    for i in range(1,actual):
        f.write(' ')
    f.write('*')
    for i in range(1, maximum-actual+1):
        f.write(' ')
    place = actual - 10
    if place>0:
        f.write('|+' + str(place) + '\n')
    else:
        f.write('|' + str(place) + '\n')
    moves = moves + 1
    
f.write ('Liczba krokow:')
f.write (str(moves))

f.close()