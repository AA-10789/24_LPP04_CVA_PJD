'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

dia = 23
mes = 9
ano = 2024

def data_valida(dia_introduzido, mes_introduzido, ano_introduzido):
    if mes_introduzido < 1 or mes_introduzido > 12:
        return False
    if dia_introduzido < 1 or dia_introduzido > 31:
        return False
    if mes_introduzido in [4, 6, 9, 11] and dia_introduzido > 30:
        return False
    if mes_introduzido == 2 and dia_introduzido > 29:
        return False
    if mes_introduzido == 2 and dia_introduzido == 29 and not (ano_introduzido % 4 == 0 and (ano_introduzido % 100 != 0 or ano_introduzido % 400 == 0)):
        return False
    return True

while True:
    try:
        input_data = input("Introduza a sua data de nascimento (DD/MM/AAAA): ")
        dia_introduzido, mes_introduzido, ano_introduzido = map(int, input_data.split('/'))

        if not data_valida(dia_introduzido, mes_introduzido, ano_introduzido):
            print("Data inválida. Tente novamente.")
            continue

        idade = ano - ano_introduzido

        if (mes_introduzido, dia_introduzido) > (mes, dia):
            idade -= 1

        if idade < 0:
            print("Idade inválida.")
        elif idade < 10:
            print("É uma criança. Menor de idade.")
        elif idade <= 17:
            print("É um adolescente. Menor de idade.")
        elif idade < 65:
            print("É um adulto. Maior de idade.")
        else:
            print("É um idoso. Maior de idade.")

        print(f"A sua idade é: {idade} anos.")

        break  

    except ValueError:
        print("Entrada inválida. Por favor, use o formato DD/MM/AAAA.")


# Código original:
# if idade < 0:
#    print("Idade inválida.")
# elif idade <10:
#     print("É uma criança. Menor de idade.")
# elif idade <= 17:
#     print("É menor de idade.")
#     print("É um adolescente. Menor de idade.")
# elif idade < 65:
#     print("É um adulto. Maior de idade.")
# else:
#     print("É maior de idade.")
#     print("É um idoso. Maior de idade.")