'''
B��dzenie przypadkowe.

Mniej wi�cej na �rodku ekranu piszemy START.
W kolejnej lini wypisujemy gwiazdk� *.
Idziemy do kolejnej linii.

Rzucamy monet�.
Na monecie jest +1 i -1 Jak +1 to robimy krok w prawo na ekranie. Tzn. robimy spacje w prawo i wypisujemy *. Jak -1 to robimy krok w lewo, tzn. idziemy o spacje w lewo i wypisujemy *.
Idziemy do kolejnej linii i robimy to samo. Prosz� spojrze� na rysunek.

              START
|                  *                  | 0
|                   *                 | +1
|                    *                | +2
|                     *               | +3
|                    *                | +2


Tutaj 3 razy poszli�my w prawo i na ko�cu w lewo. Liczba na ko�cu ka�dego wiersza m�wi jak daleko jeste�my od zera.

Po lewej i prawej stronie rysujemy �ciany |. Jak gwiazdka uderzy jedn� ze �cianek to koniec programu.
Program rysuje ca�� �cie�k� jak wy�ej oraz na ko�cu wypisuje ile razy rzucili�my monet�.

Odleg�o�� od �cianki do �cianki to 20 spacji.
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