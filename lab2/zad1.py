# The function myPI is to estimate PI using Liebniz equation
# The result is written to the file zad1.txt, estimating PI number with progressive precision

import math

def myPI(i): 
    _sum = 0
    parz = 1;
    for x in range(1,i+1):
        if parz == 0:
            parz = 1 
            _sum = _sum - 1.0/(2.0*x-1)  
        else:
            parz = 0
            _sum = _sum + 1.0/(2.0*x-1)
    return 4*_sum
        


f = open("zad1.txt", "a")
for x in range(1,101):
    f.write(''+ str(x) + ': ' + str(myPI(x)) + ', ' + str(myPI(x)/math.pi) + '\n')
for x in range(3,8):
    f.write(''+ str(10**x) + ': ' + str(myPI(10**x)) + ', ' + str(myPI(10**x)/math.pi) + '\n')
f.close()



