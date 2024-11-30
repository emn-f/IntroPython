# Lista com números pares de 1 a 20. Inverter ordem

list = []

for i in range(1, 20):
    if (i % 2 == 0):
        list.append(i)

list.reverse()
print(list)


# Alternativa
list = [i for i in range (1,20) if (i % 2 == 0)]
list.reverse()
print(list)