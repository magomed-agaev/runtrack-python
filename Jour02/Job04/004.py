while True:
    try:
        N = int(input("Entier supérieur à zéro : "))
        if N <= 0:
            print("Entrez un entier supéerieur à zéro")
        else:
            break
    except ValueError:
        print("Veuillez entrer un nombre entier valide.")

for i in range(1, N + 1):
    print(f"Table de multiplication de {i}:")
    for j in range(1, 11):
        result = i * j
        print(f"{i} x {j} = {result}")
    print()