# calculo de IMC (Índice de massa corporal)
from time import sleep
print("-=" * 31)
print("     \033[1;37mTabela de classificação para adultos (19 a 59 anos)\033[m")
print("-=" * 31)

nome = str(input("Digite o nome do paciente: ")).strip().lower()
idade = int(input("Informe sua idade: "))
if 18 < idade <= 59:
    peso = float(input("Informe o quanto você pesa: (Kg) "))
    altura = float(input("Informa sua altura: (m) "))
    print("\033[1;37mAnalisando Informações digitadas...\033[m")
    sleep(2.3)

    imc = peso / (altura ** 2)

    if imc < 18.5:
        print("\033[34m-=\033[m" * 35)
        print(f"   \033[1;37mPaciente:\033[m {nome.capitalize()}")
        print(f"   \033[1;37mIdade:\033[m {idade} Anos")
        print(f"   O peso do paciente é de {peso} Kg, e á sua altura é de {altura} Metros")
        print(f"   Seu IMC será de: {imc:.1f}")
        print(f"   \033[1;37mClassificação:\033[m Magreza \033[36m(Abaixo do peso!)\033[m")
        print("\033[34m-=\033[m" * 35)

    elif 18.5 <= imc <= 24.9:
        print("\033[34m-=\033[m" * 35)
        print(f"   \033[1;37mPaciente:\033[m {nome.capitalize()}")
        print(f"   \033[1;37mIdade:\033[m {idade} Anos")
        print(f"   O peso do paciente é de {peso} Kg, e á sua altura é de {altura} Metros")
        print(f"   Seu IMC será de: {imc:.1f}")
        print(f"   \033[1;37mClassificação:\033[m Peso normal \033[1;32m(Saúdavel)\033[m")
        print("\033[34m-=\033[m" * 35)

    elif 25 <= imc <= 29.9:
        print("\033[34m-=\033[m" * 35)
        print(f"   \033[1;37mPaciente:\033[m {nome.capitalize()}")
        print(f"   \033[1;37mIdade:\033[m {idade} Anos")
        print(f"   O peso do paciente é de {peso} Kg, e á sua altura é de {altura} Metros")
        print(f"   Seu IMC será de: {imc:.1f}")
        print(f"   \033[1;37mClassificação:\033[m Sobrepeso \033[33m(Pré-obesidade)\033[m")
        print("\033[34m-=\033[m" * 35)

    elif 30 <= imc <= 34.9:
        print("\033[34m-=\033[m" * 35)
        print(f"   \033[1;37mPaciente:\033[m {nome.capitalize()}")
        print(f"   \033[1;37mIdade:\033[m {idade} Anos")
        print(f"   O peso do paciente é de {peso} Kg, e á sua altura é de {altura} Metros")
        print(f"   Seu IMC será de: {imc:.1f}")
        print(f"   \033[1;37mClassificação:\033[m Obesidade Grau 1 \033[33m(Cuidado!)\033[m")
        print("\033[34m-=\033[m" * 35)

    elif 35 <= imc <= 39.9:
        print("\033[34m-=\033[m" * 35)
        print(f"   \033[1;37mPaciente:\033[m {nome.capitalize()}")
        print(f"   \033[1;37mIdade:\033[m {idade} Anos")
        print(f"   O peso do paciente é de {peso} Kg, e á sua altura é de {altura} Metros")
        print(f"   Seu IMC será de: {imc:.1f}")
        print(f"   \033[1;37mClassificação:\033[m Obesidade Grau 2 \033[33m(Cuidado!)\033[m")
        print("\033[34m-=\033[m" * 35)

    else:
        print("\033[34m-=\033[m" * 35)
        print(f"   \033[1;37mPaciente:\033[m {nome.capitalize()}")
        print(f"   \033[1;37mIdade:\033[m {idade} Anos")
        print(f"   O peso do paciente é de {peso} Kg, e á sua altura é de {altura} Metros")
        print(f"   Seu IMC será de: {imc:.1f}")
        print(f"   \033[1;37mClassificação:\033[m Obesidade Grau 3 \033[31m(Grave!)\033[m")
        print("\033[34m-=\033[m" * 35)
else:
    print(" \033[31mERROR\033[m ".center(58, "-"))
    print(f"   Olá {nome.capitalize()}!")
    print("   O sistema só aceta idade entre \033[1;37m19\033[m a \033[1;37m59\033[m anos!")
    print(" \033[31mERROR\033[m ".center(58, "-"))
