# Escreva um programa para controlar uma pequena máquina registradora.
# Você deve solicitar ao usuário que digite o código do produto e a quantidade comprada.
# Utilize a tabela de códigos a seguir para obter o preço de cada produto respectivamente:
# 1 -> 0,50 | 2 -> 1,00 | 3 -> 4,00 | 5 -> 7,00 | 9 -> 8,00.
# Seu programa deve exibir o total das compras depois que o usuário digitar 0.
# Qualquer outro código deve gerar a mensagem de erro "Código inválido".

pagamento_total = 0.0

while True:
    cod_produto = int(input("Código do produto (0 para sair): "))

    if cod_produto == 0:
        break

    preco = 0.0

    if cod_produto == 1:
        preco = 0.50
    elif cod_produto == 2:
        preco = 1.00
    elif cod_produto == 3:
        preco = 4.00
    elif cod_produto == 5:
        preco = 7.00
    elif cod_produto == 9:
        preco = 8.00
    else:
        print("Código inválido!")
        continue

    qtd_produto = int(input("Quantidade: "))
    pagamento_total += preco * qtd_produto

print("Total das compras:", pagamento_total)