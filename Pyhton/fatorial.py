n = int(input("Digite um número:"))
i = n
fat = 1

if n >= 0:
    while i > 1:
        fat *= i
        i-=1
    print(f"O fatorial de {n} é {fat}")
else:
    print("O fatorial só é definido para números inteiros não-negativos.")  