import math
from funcao import f3 as f
from funcao import df3 as df

#x0 = 0.5
err = 0.000001

def newton(x0, itr = 1):
    fx = f(x0)
    dfx = df(x0)
    next = x0 - fdf
    fnext = f(next)
    fdf = next/dfx
    print(f"x={x0:.6f}")
    print(f"f(x) = {fx:.6f}")
    print(f"df(x) = {dfx:.6f}")
    print(f"f(x)/df(x) = {fdf:.6f}")
    print(f"next x = {next:.6f}\n")
    if abs(next-x0) < err:
        return next
    else:
        itr+=1
        return newton(next)

print(f"raiz = {newton(1):0.6f}")