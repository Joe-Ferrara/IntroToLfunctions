from math import sqrt

def primes_up_to(N):

    ## returns a list of the primes less than N
    ## uses the sieve of Eratosthenes
    ## make sure that sqrt is implimented

    sievebound = int(N/2)
    primes = [2] ## start with 2 and eliminate evens from list
    sieve = [False for _ in range(sievebound)]

    ## needed index arithmetic:
    ## the i^th element of the array corresponds to the odd number 2*i + 1
    ## thus, is p = 2*i + 1, then the number p^2 = 4*i^2 + 4*i + 1 has index 2*i*(i + 1) in the list
    ## if the number m = k*p has index j, then the number m + 2*p has index j + p
    ## so if the i^th index is not yet crossed out, the inner loop starts at 2*i*(i + 1) (corresponding to number p^2) and procceeds with step 2*i + 1 (corresponding to gap of numbers of 2*p)
    ## the gap of 2*p is because we've already taken out the even numbers p^2 + odd*p is even, p^2 + even*p is odd

    crosslimit = int(sqrt(N)/2)
    sieve[0] = True ## 1 is not prime
    for i in range(1, crosslimit):
        if sieve[i] == False:
            for j in range(2*i*(i + 1), sievebound, 2*i + 1):
                sieve[j] = True
    for i in range(0, sievebound):
        if sieve[i] == False:
            primes.append(2*i + 1)
    return primes

def gcd_x_y(a, b):
    """returns [g,x,y] such that g = gcd(a, b) and a*x + b*y = g

    we're assuming a and b are positive integers"""
    # we assume a < b
    switch = False
    if b < a:
        temp = a
        a = b
        b = temp
        switch = True
    # do the extended Euclidean algorithm
    q = int(b/a)
    r = b - q*a
    if r == 0:
        return [a, 1-q, 1]
    x0, x1, y0, y1 = 1, -q, 0, 1
    while r != 0:
        g = r
        x = x1
        y = y1
        b = a
        a = r
        q = int(b/a)
        r = b - q*a
        tempx = x1
        tempy = y1
        x1 = x1*(-q) + x0
        y1 = y1*(-q) + y0
        x0 = tempx
        y0 = tempy
    # remember the order
    if switch == True:
        return [g, y, x]
    else: return [g, x, y]

def quad_Lval(d, n, N=100):
    """Return the sum of n-terms of Lvalue at s=1 of quadratic field Q(sqrt(d)).


    Assumes that d is squarefree. Otherwise may have problems. N is the number of primes to generate in order to get a prime for each residue class mod D where D is the discriminant of Q(sqrt(d))."""

    # get discriminant
    if d%4 == 1:
        D = d
    else:
        D = 4*d
    primes = primes_up_to(N*abs(D))
    chiVals = make_chi_vals(D, primes)
    Lval = make_Lval(chiVals, n, D)
    return Lval

def make_chi_vals(D, primes):
    chiVals = {}
    chiVals[0] = 0
    chiVals[1] = 1
    for i in range(2, abs(D)):
        if gcd_x_y(i, abs(D))[0] > 1:
            chiVals[i] = 0
        else:
            enoughPrimes = False
            for p in primes:
                if p%abs(D) == i%abs(D):
                    val = chi_Val(p, d)
                    chiVals[i] = val
                    enoughPrimes = True
                    break
            if enoughPrimes == False:
                raise ValueError('Not enough primes, increase N')
    return chiVals

def chi_Val(p, d):
    if p == 2: # the d%4 = 1
        if d%8 == 1:
            return 1
        else: # d%8 = 5
            return -1
    else:
        squares_mod_p = set([])
        for i in range(p):
            squares_mod_p.add((i*i) % p)
        if d%p in squares_mod_p:
            return 1
        else:
            return -1

def make_Lval(chiVals, n, D):
    ans = 1
    for i in range(2, n+1):
        newi = i%abs(D)
        ans += (chiVals[newi]/i)
    return ans

def make_coeff(chiVals, n, D):
    ans = [0]*n
    ans[0] = 1
    for i in range(2, n + 1):
        newi = i%abs(D)
        ans[i-1] = chiVals[newi]
    return ans
