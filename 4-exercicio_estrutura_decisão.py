#4-Faça um Programa que verifique se uma letra digitada é vogal ou consoante.#

vogais = ['a', 'e', 'i', 'o', 'u']

entrada = input("digite uma letra: ").lower()

if entrada in vogais:
    print("você digitou uma vogal")

else:
    print("você digitou uma consoante")

