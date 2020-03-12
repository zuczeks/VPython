import random
import math

#lista strzalow
shots = []
#czy strzaly sa trafione w kolo
incircle = []

def shot(i):
    shot = []
    x = 2*random.random()-1.0
    y = 2*random.random()-1.0
    shot.append(x)
    shot.append(y)
    shots.append(shot)

for x in range(1,10**6):
    shot(x)
    if math.sqrt(shots[x-1][0]**2 + shots[x-1][1]**2) <= 1:
        incircle.append(1)
    else:
        incircle.append(0)

f = open("zad2.txt", "a")
for x in range(1,101):
    mypi = 4.0*float((sum(incircle[1:x])))/x
    f.write(''+ str(x) + ': ' + str(mypi) + ', ' + str(mypi/math.pi) + '\n')

for x in range(3,7):
    mypi = 4.0*float((sum(incircle[1:10**x])))/10**x
    f.write(''+ str(10**x) + ': ' + str(mypi) + ', ' + str(mypi/math.pi) + '\n')
f.close()




    

