def calcular_dias_vida_perdidos(cigarros_por_dia, anos_fumando):
    cigarros_totais = cigarros_por_dia * anos_fumando * 365
    minutos_perdidos = cigarros_totais * 10
    horas_perdidas = minutos_perdidos / 60
    dias_perdidos = horas_perdidas / 24
    return dias_perdidos

qtd_cigarro_dia = int(input("Quantidade de cigarros fumados por dia: "))
anos_fumo = int(input("Quantidade de anos fumados: "))

dias_perdidos = calcular_dias_vida_perdidos(qtd_cigarro_dia, anos_fumo)

print("Dias de vida perdidos:", dias_perdidos)
