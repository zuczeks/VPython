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