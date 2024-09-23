'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

dia = 23
mes = 9
ano = 2024


input = input("Introduza a sua data de nascimento (DD/MM/AAAA): ")
dia_introduzido, mes_introduzido, ano_introduzido = map(int, input.split('/'))

idade = ano - ano_introduzido

if (mes_introduzido, dia_introduzido) > (mes, dia):
    idade -= 1


if idade < 0:
    print("Idade inválida.")
elif idade <10:
    print("É uma criança. Menor de idade.")
elif idade <= 17:
    print("É um adolescente. Menor de idade.")
elif idade < 65:
    print("É um adulto. Maior de idade.")
else:
    print("É um idoso. Maior de idade.")


print(f"A sua idade é: {idade} anos.")