nome = input("Digite seu nome:")
while nome.isalpha() == False :
    if nome.isdigit():
        print(" -Você digitou algo numero")
        
    elif len(nome) == 0:
        print(" -Você não digitou nada")
        
    elif nome.isspace():
        print(" -Espaço não é validado")
    nome = input("Digite seu nome:")
        
print("-----------------------")

while True:
    salario = input("Digite seu salario:")

    if salario.isalpha():
        print(" -Digite apenas numeros. Ex 899.00 ou 899,00")

    elif len(salario) == 0:
        print(" -Você não digitou nada")
    
    elif salario.isspace():
        print(" -Espaço não é validado")
    
    else:
        try:
            salario = float(salario.replace(",", "."))
            break
        except ValueError:
            print(" -Valor invalido. Digite por exemplo 998.00 ou 998,00")

    
print("-----------------------")

while True :

    perc_bonus = input("Percentual do bonus:")

    
    if perc_bonus.isalpha():
        print(" -Digite apenas numeros. Ex 1,5 ou 1.5")

    elif len(perc_bonus) == 0:
        print(" -Você não digitou nada")
    
    elif perc_bonus.isspace():
        print(" -Espaço não é validado")
    else:
        try:
            perc_bonus = float(perc_bonus.replace(",", "."))
            break
        except ValueError:
            print(" -Valor invalido. Digite por exemplo 1.0 ou 1,0")
    

valor_bonus = ((1000 + salario) * (perc_bonus / 100))
recebimento = salario + valor_bonus
print("-----------------------")
print(f"Olá, {nome}. Seu bonus é de: {valor_bonus}")
print(f"Esse mês irá receber: R$ {recebimento}")
exit()