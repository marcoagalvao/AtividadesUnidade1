def calcular_desconto_e_preco_a_pagar(preco, percentual):
    valor_desconto = preco * percentual / 100
    preco_a_pagar = preco - valor_desconto
    return valor_desconto, preco_a_pagar

preco = float(input("Preço da mercadoria (R$): "))
percentual = float(input("Percentual de desconto: "))

valor_desconto, preco_a_pagar = calcular_desconto_e_preco_a_pagar(preco, percentual)

print("Valor de desconto:", valor_desconto)
print("Preço a pagar:", preco_a_pagar)
