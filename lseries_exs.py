

def chi8_val(n):
    res = 0
    for i in range(1, n + 1):
        if i%8 == 1 or i%8 == 7:
            res += 1/i
        elif i%8 == 3 or i%8 == 5:
            res -= 1/i
        else:
            continue
    return res

def chi4_val(n):
    res = 0
    for i in range(1, n + 1):
        if i%4 == 1:
            res += 1/i
        elif i%4 == 3:
            res -= 1/i
        else:
            continue
    return res

from math import sqrt
from math import log
from math import pi


print("      100 terms of L(chi8, 1) = " + str(chi8_val(100)))
print("")
print("    1,000 terms of L(chi8, 1) = " + str(chi8_val(1000)))
print("")
print("   10,000 terms of L(chi8, 1) = " + str(chi8_val(10000)))
print("")
print("  100,000 terms of L(chi8, 1) = " + str(chi8_val(100000)))
print("")
print("1,000,000 terms of L(chi8, 1) = " + str(chi8_val(1000000)))
print("")
print("    log(1 + sqrt(2))/2sqrt(2) = " + str(log(1 + sqrt(2))/(sqrt(2))))
print("")
print("")
print("        100 terms of L(chi4, 1) = " + str(chi4_val(100)))
print("")
print("      1,000 terms of L(chi4, 1) = " + str(chi4_val(1000)))
print("")
print("     10,000 terms of L(chi4, 1) = " + str(chi4_val(10000)))
print("")
print("    100,000 terms of L(chi4, 1) = " + str(chi4_val(100000)))
print("")
print("  1,000,000 terms of L(chi4, 1) = " + str(chi4_val(1000000)))
print("")
print(" 10,000,000 terms of L(chi4, 1) = " + str(chi4_val(10000000)))
print("")
print("100,000,000 terms of L(chi4, 1) = " + str(chi4_val(100000000)))
print("")
print("                           pi/4 = " + str(pi/4))
