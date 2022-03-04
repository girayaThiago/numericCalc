import math

matriz: list(list(int)) = [[2, 1,-5],
                [8,-2, 3],
                [5, 2,-1]]
matriz2: list(int) = [-2,5,6]

#x0 = 0.5
err = 0.000001

# Para fatorar LU com pivoteamento parcial, temos que selecionar a cada iteração o elemento da coluna com maior valor absoluto
# no caso dessa questão, é o 8
# pivotear ele e transcrever a transformação para a matriz identidade
# | 2  1  -5 |  | 1  0  0 |      | 8  -2  3 |  | 0 1 0 |
# | 8  -2  3 |  | 0  1  0 |  ->  | 2  1  -5 |  | 0 0 1 |
# | 5  2  -1 |  | 0  0  1 |      | 5  2  -1 |  | 1 0 0 |
# encontrar os coeficientes de multiplicação para as linhas 2,3 
#
# | 8  -2  3 |   (1    0   0)                           | 1     0   0 |
# | 2  1  -5 |   (m21  1   0) -> tiramos a matriz L ->  | -0.25  1   0 | (essa é a matriz parcial, falta escalonar o restante (repetir os passos))
# | 5  2  -1 |   (m31  m32 0)                           | -0.625 0   1 |
#
# | 8  -2    3  |
# | 0  1,5 -6,5 |
# | 0  2,5 -1,75| <- 2,5 é o maior em modulo, trocar
#
# | 8  -2    3  | | 0 1 0 |     | 8  -2  3    |  | 0 1 0 |
# | 0  1,5 -6,5 | | 0 0 1 | ->  | 0 2,5  -6,5 |  | 1 0 0 |
# | 0  2,5 -1,75| | 1 0 0 |     | 0 1,5  -1,75|  | 0 0 1 |
#
# calculando m32 = 2,75/3,3 = 0,8333~
#
# | 8  -2  3    |  | 0 1 0 |    (1    0   0)                           |    1   0     0 |
# | 0 2,5  -6,5 |  | 1 0 0 | -> (m21  1   0) -> tiramos a matriz L ->  | -0.25  1     0 |
# | 0 1,5  -1,75|  | 0 0 1 |    (m31  m32 0)                           | -0.625 0,6   1 |
#
# | 8  -2  3    | 
# | 0 2,5  -6,5 | = U
# | 0   0  -5,65| 

# |    1   0     0 |
# | -0.25  1     0 | = L
# | -0.625 0,6   1 |

# | 8  -2  3    |
# | 0 2,5  -6,5 | = A 
# | 0 1,5  -1,75|

# | 0 1 0 |
# | 1 0 0 | = P
# | 0 0 1 |

# | -2 |
# |  5 | = X
# |  6 |

# P.A = L.U = P.X 

#TODO: terminar a fatoração e criar função para alimentar a matriz
identidade: list(list(int)) = [[1,0,0],
                    [0,1,0],
                    [0,0,1]]

def pivoteamento(m: list(list(int)), i: list(list(int))) -> list(list(int)):
    for i in m.count():
        i[0]

    return

pivoteamento