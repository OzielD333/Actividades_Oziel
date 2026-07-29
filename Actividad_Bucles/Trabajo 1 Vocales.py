while True:
    letra = input("Ingresar letra (espacio termina): ")
    if letra == " ":
        break
    letra = letra.lower()
    if letra in "aeiou":
        print("Vocal")
    else:
        print("Consonante")
print("Programa finalizado")
#para que tenga commit
