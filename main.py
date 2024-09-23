'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

idade = int(input("Introduza a sua idade: "))

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