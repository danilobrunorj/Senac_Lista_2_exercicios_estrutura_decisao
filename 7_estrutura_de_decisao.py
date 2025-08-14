# 7. Faça um Programa que leia três números e mostre o maior e o menor deles.
primeiro = float(input('Digite o primeiro número: '))
segundo = float (input ('Digite o segundo número: '))
terceiro =float(input ('Digite o terceiro número: '))

if primeiro > segundo and primeiro > terceiro:
  print(f' O maior é : {primeiro}')

elif segundo > primeiro and segundo > terceiro:
    print(f' O maior é : {segundo}')

else:
    print(f' O maior é : {terceiro}')

if primeiro < segundo and primeiro < terceiro:
  print(f' O menor é : {primeiro}')

elif segundo < primeiro and segundo < terceiro:
    print(f' O menor é : {segundo}')

else:
    print(f' O menor é : {terceiro}')