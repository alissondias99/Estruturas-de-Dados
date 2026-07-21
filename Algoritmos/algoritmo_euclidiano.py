# O Algoritmo Euclidiano é uma técnica para encontrar de forma rápida o MDC (Máximo Divisor Comum) de dois inteiros.
# O Algoritmo Euclidiano para encontrar o MDC(A,B) é dado por:
# Se A = 0, então MDC(A,B)=B, uma vez que MDC(0,B)=B, e podemos parar a verificação.  
# Se B = 0, então MDC(A,B)=A, uma vez que o MDC(A,0)=A, e podemos parar a verificação.  
# Escreva A na forma do resto do quociente (A = B⋅Q + R)
# Encontre o MDC(B,R) usando o Algoritmo Euclidiano, já que MDC(A,B) = MDC(B,R)

# #Sem recursão
def MDC(A, B):
    while A != 0 or B != 0:
        if A == 0:
            return B
        if B == 0:
            return A
        R = A % B # resto
        Q = round(A / B) # quociente, só serve para verificação
        A = B
        B = R
    return B


print(MDC(1680, 640))

#Com recursão
def MDC(A, B):
    # Condição de parada: se B for 0, o MDC é A
    if B == 0:
        return A
    
    # Chamada recursiva: o novo 'A' passa a ser 'B', e o novo 'B' passa a ser 'A % B'
    return MDC(B, A % B)

print(MDC(1680, 640))