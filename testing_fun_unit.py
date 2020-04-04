exec(open('fundamental_unit.py').read())

squares = [i*i for i in range(2, 10)]

for d in range(2, 100):
    square = False
    for s in squares:
        if d%s == 0:
            square = True
            break
    if square:
        continue
    if d%4 == 2 or d%4 == 3:
        sol = fun_unit_sol(d)
        print("fundamental unit:")
        print(str(sol[0]) + " + " + str(sol[1]) + "*sqrt(" + str(d) + ")")
    else:
        sol = fun_unit_sol(d)
        print("fundamental unit:")
        print("(" + str(sol[0]) + " + " + str(sol[1]) + "*sqrt(" + str(d) + "))/2")
