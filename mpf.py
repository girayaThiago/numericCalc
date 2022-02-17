import math
from funcao import f2 as f
from funcao import phif2 as phif

#x0 = 0.5
err = 0.001

#intervalo 0.5 - 1 TODO: prints controlados pela flag
def mpf(x0,itr,flag = True):
    anterior = x0
    atual = phif(anterior)
    delta = abs(atual-anterior)
    while delta > err:
        print(f"x-phix = {delta:.4f}")
        anterior = atual
        atual = phif(anterior)
        print(f"iteração: {itr}\nf(x) = {f(anterior):.4f}\nphi(x) = {atual:.4f}\n")
        itr +=1
        delta = abs(atual-anterior)
    return
    
mpf(0.5,0)