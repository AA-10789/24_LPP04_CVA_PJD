'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

idade = int(input("Introduza a sua idade: "))

if idade < 0:
    print("Idade inválida.")
elif idade <= 17:
    print("É menor de idade.")
else:
    print("É maior de idade.")