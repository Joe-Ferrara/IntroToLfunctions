

def cont_frac_rat( frac ):
    """Returns continued fraction of rational number frac."""

    num = frac.numerator
    den = frac.denominator

    answer = []
    r1 = num
    r2 = den
    r3 = r1 % r2
    q = r1 / r2

    answer.append(q)

    while r3 != 0:         # euclidean algorithm
        r1 = r2
        r2 = r3
        r3 = r1 % r2
        q = r1/r2
        answer.append(q)

    return answer

def convergents ( contFrac, n ):
    """Returns first n convergents of continued fraction contFrac.

    Uses formulas in Rosen, Elementary Number Theory..., page 355 Thm 10.9."""

    p0 = contFrac[0]
    q0 = 1
    p1 = contFrac[0]*contFrac[1] + 1
    q1 = contFrac[1]

    answer = [Fraction(p0, q0), Fraction(p1, q1)]

    plast1 = p1
    plast2 = p0
    qlast1 = q1
    qlast2 = q0
    for i in range(2, n):
        pnext = contFrac[i]*plast1 + plast2
        qnext = contFrac[i]*qlast1 + qlast2
        convNext = Fraction(pnext, qnext)
        answer.append(convNext)
        plast2 = plast1
        plast1 = pnext
        qlast2 = qlast1
        qlast1 = qnext

    return answer

def convergent_den( contFrac, m):
    """Returns denominator of mth convergent of contFrac.

    These are the q's in the notation of Rosen's book. The mth convergent has subscript m-1."""

    qlast2 = 1

    if m == 1:
        return qlast2

    qlast1 = contFrac[1]

    if m == 2:
        return qlast1

    qnext = 0

    for i in range(2, m):
        qnext = contFrac[i]*qlast1 + qlast2
        qlast2 = qlast1
        qlast1 = qnext

    return qnext

def convergent_num ( contFrac, m):
    """Returns the numerator of the mth convergent of contFrac.

    These are the p's in the notation of Rosen's book. The mth convergent has subscript m-1."""

    plast2 = contFrac[0]

    if m == 1:
        return plast2

    plast1 = contFrac[0]*contFrac[1] + 1

    if m == 2:
        return plast1

    pnext = 0

    for i in range(2, m):
        pnext = contFrac[i]*plast1 + plast2
        plast2 = plast1
        plast1 = pnext

    return pnext

from decimal import *

def cont_frac_sqrt( d, n = 50, prec = 1000):
    """Returns the first n terms of the continued fraction of sqrt(d).

    Uses decimal package to calculate sqrt(d) to prec decimals. This allows an accurate continued fraction. May need to adjust n and prec so the continued fraction is accurate for all n continued fraction digits. Uses the formula in Rosen, Elementary Number Theory..., page 365 Thm 10.15."""

    getcontext().prec = prec

    number = Decimal(d).sqrt()

    alphalast = number
    alast = int(alphalast)
    answer = [alast]

    for i in range(1, n):
        alphanext = 1/(alphalast - Decimal(alast))
        anext = int(alphanext)
        answer.append(anext)
        alphalast = alphanext
        alast = anext

    return answer

def check_for_period(contFrac, k):
    """Checks contFrac, to see if it has period k."""

    l = len(contFrac)
    answer = False
    for i in range(0, l//4):
        period = []
        test = []
        for j in range(0, k):
            period.append(contFrac[i + j])
            test.append(contFrac[i + k + j])
        if period == test:
            answer = True
        if answer == True:
            index = int((l-i)/k)-1
            for j in range(2, index):
                test = []
                for n in range(0, k):
                    test.append(contFrac[i + j*k + n])
                if period != test:
                    answer = False
        if answer == True:
            return answer
    return answer

    # Note: to get sqrt(919) has period 60 need 1000 bit real numbers



def fun_unit_sol(d, N = 100):
    """Returns [x,y] such that x is minimal and
    (1) x^2 - dy^2 = 1 or -1 if d is 2 or 3 mod 4
    (2) x^2 - dy^2 = 4 or -4 if d is 1 mod 4

    Assumes d is squarefree.
    Raises exception if period of continued fraction of sqrt(d) is >= N."""

    contFrac = cont_frac_sqrt(d)

    if d%4 == 2 or d%4 == 3:
        # solution to x^2 - dy^2 = 1 or -1
        # use Rosen, Theorem 11.5 page 404

        period = 0

        for k in range(1, N):
            if check_for_period(contFrac, k) == True:
                period = k
                break
            if k == N-1:
                raise ValueError("Period is larger than N, increase N.")

        x = convergent_num(contFrac, period)
        y = convergent_den(contFrac, period)
        return [x,y]

    else:
        # solution to x^2 - dy^2 = 4 or -4
        # must search for solution
        # use Rosen, Theorems 11.3 (page 402) and 11.4 (page 403)

        # hardwire these
        if d == 5:
            return [1,1]
        if d == 13:
            return [3, 1]

        period = 0

        for k in range(1, N):
            if check_for_period(contFrac, k) == True:
                period = k
                break
            if k == N-1:
                raise ValueError("Period is larger than N, increase N.")

        x = convergent_num(contFrac, period)
        y = convergent_den(contFrac, period)
        sols = [[2*x,2*y]]

        # search for a solution
        for k in range(1, period + 1):
            # convergents are an increasing sequence
            # so this will produce minimal solution
            x = convergent_num(contFrac, k)
            y = convergent_den(contFrac, k)

            if x**2 - d*y**2 == 4:
                sols.append([x,y])
            if x**2 - d*y**2 == -4:
                sols.append([x,y])

        minX = sols[0][0]
        ansIndex = 0
        for i in range(1, len(sols)):
            if sols[i][0] < minX:
                minX = sols[i][0]
                ansIndex = i
        return sols[ansIndex]
