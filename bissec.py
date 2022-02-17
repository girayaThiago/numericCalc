import math
from funcao import f1 as f
err = 0.001

def bissec(a,b,itr, flag = True):

    fa = f(a)
    fb = f(b)
    intervalo = abs(fa - fb)
    print(f"numero de iterações: {itr}\na = {a:.4f} fa = {fa:.4f}\nb = {b:.4f} fb = {fb:.4f}\nintervalo entre a e b = {intervalo:.4f}")
    if flag:
        print("imprimir restante da solução? (y/n) enter para próximo passo.")
        x = input()
        if x == 'n':
            return
        if x == 'y':
            flag = False
    if intervalo <= err:
        return intervalo
    itr = itr + 1
    if fa > 0 and fb < 0:
        c = (a+b)/2
        fc = f(c)
        if fc > 0:
            bissec(c,b,itr,flag)
        else:
            bissec(a,c,itr,flag)
    elif fa < 0 and fb > 0:
        c = (a+b)/2
        fc = f(c)
        if fc > 0:
            bissec(a,c,itr,flag)
        else:
            bissec(c,b,itr,flag)
    else:
        print("Falhou no teorema do sanduiche")
    pass

bissec(0.8,1.1,1)