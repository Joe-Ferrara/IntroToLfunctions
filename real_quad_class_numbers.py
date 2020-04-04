import numpy as np

exec(open('quad_Lfunctions.py').read())
exec(open('fundamental_unit.py').read())


print('{:>5} {:>7} {:>28}'.format('d', 'h_K', 'u_K'))

squares = [i*i for i in range(2, 11)]

for i in range(2, 100):
    square = False
    for s in squares:
        if i%s == 0:
            square = True
            break
    if square == True:
        continue
    else:
        d = i
        if d%4 == 1:
            D = d
        else:
            D = 4*d
        Ld = quad_Lval(d, 1000000)
        if d%4 == 2 or d%4 == 3:
            sol = fun_unit_sol(d)
            u_string = str(sol[0]) + " + " + str(sol[1]) + "*sqrt(" + str(d) + ")"
            u_K = float(sol[0]) + float(sol[1])*np.sqrt(d)
            h_K = Ld*np.sqrt(D)/(2*np.log(u_K))
        else:
            sol = fun_unit_sol(d)
            u_string = "(" + str(sol[0]) + " + " + str(sol[1]) + "*sqrt(" + str(d) + "))/2"
            u_K = (float(sol[0]) + float(sol[1])*np.sqrt(d))/2
            h_K = Ld*np.sqrt(D)/(2*np.log(u_K))
        print('{:>5} {:>7} {:>28}'.format(str(d), str(int(round(h_K))), u_string))
