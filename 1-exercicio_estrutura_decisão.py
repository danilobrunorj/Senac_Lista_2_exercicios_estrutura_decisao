#1-Faça um Programa que peça dois números e imprima o maior deles.#

primeiro = int (input("digite um numero: "   ))  
segundo = int (input("digite outro numero: "   )) 

if primeiro > segundo:
    print('o maior número é o primeiro: ', primeiro)

elif segundo > primeiro:
    print('O maior número é o segundo:', segundo)

else:
    print("numeros iguais")


