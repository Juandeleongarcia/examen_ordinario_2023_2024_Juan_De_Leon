def imprimir_piramide(n):
    for i in range(1, n + 1, 2):
        espacios = (n - i) // 2
        print(" " * espacios + "*" * i + " " * espacios)

def main():
    while True:
        try:
            n = int(input("Ingrese un número entero mayor o igual a 1: "))
            if n >= 1:
                break
            else:
                print("Por favor, ingrese un número mayor o igual a 1.")
        except ValueError:
            print("Por favor, ingrese un número entero válido.")

 
    imprimir_piramide(n)

if __name__ == "__main__":
    main()
