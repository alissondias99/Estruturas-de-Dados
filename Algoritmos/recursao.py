def fat(x):
    if x == 1: # caso baso (condição de parada)
        return 1
    return x * fat(x-1) # caso recursivo

print(fat(99))