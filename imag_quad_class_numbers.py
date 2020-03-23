import numpy as np
exec(open("quad_Lfunctions.py").read())

squares = [i*i for i in range(2, 11)]

print('{:>5} {:>5}'.format('d', 'h_K'))

for i in range(1, 100):
    square = False
    for s in squares:
        if i%s == 0:
            square = True
            break
    if square == True:
        continue
    else:
        d = -i
        if d%4 == 1:
            D = d
        else:
            D = 4*d
        Ld = quad_Lval(d, 1000000)
        if d == -1:
            hd = Ld*4/(np.pi)
        elif d == -3:
            hd = Ld*6*np.sqrt(abs(D))/(2*np.pi)
        else:
            hd = Ld*np.sqrt(abs(D))/(np.pi)
        print('{:>5} {:>5}'.format(str(d), str(int(round(hd)))))
