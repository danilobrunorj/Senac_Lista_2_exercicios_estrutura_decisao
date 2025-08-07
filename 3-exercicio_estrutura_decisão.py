#3-Faça um Programa que verifique se uma letra digitada é "F" ou "M". Conforme a letra escrever: F - Feminino, M - Masculino, Sexo Inválido.


sexo = input("digite o sexo, F para feminino ou M para masculino: ").lower()



if sexo == "f":
    print("feminino")
elif sexo == 'm':
    print("masculino")

else:
    print(" Sexo inválido")
