# The function myPI is to estimate PI using probability 
# The result is written to the file zad1.txt, estimating PI number with progressive precision

# Theorem:
# We are are shooting to the square with the inscribed circle. The quotient of shots made to the circle and all shots equals approximately the quotient of the circle surface and the square surface, which equals PI for the circle of radius 1.

import random
import math

shots = []
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




    

