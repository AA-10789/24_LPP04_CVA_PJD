'''

                            Online Python Compiler.
                Code, Compile, Run and Debug python program online.
Write your code in this editor and press "Run" button to execute it.

'''

velocid = float(input("Introduza a velocidade em km/h: "))

if velocid < 0:
    print("Valor inválido. Velocidade não pode ser negativa.")
elif velocid > 80:
    multa = (velocid - 80) * 5.00
    print(f"Foi multado. O total da multa é: {multa:.2f}€")
else:
    print("Está dentro do limite de velocidade.")