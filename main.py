def calcular_media(lista_de_notas):
    if not lista_de_notas:
        return 0.0
    
    soma_total = sum(lista_de_notas)
    quantidade_notas = len(lista_de_notas)
    
    return soma_total / quantidade_notas

# Dados de teste para simulação
notas_turma = [7, 8, 6, 10, 5]
media_final = calcular_media(notas_turma)

print(f"Média final: {media_final:.2f}")
