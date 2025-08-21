nome = (input("Digite seu nome:"))

salario = float(input("Digite seu salario:"))
perc_bonus = float(input("Percentual do bonus:"))

valor_bonus = ((1000 + salario) * perc_bonus)

print(f"Olá, {nome}. Seu bonus é de: {valor_bonus}")
