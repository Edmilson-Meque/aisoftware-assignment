# Lista de exemplo de dicionários
lista_funcionarios = [
    {'nome': 'Ana', 'idade': 28, 'salario': 50000},
    {'nome': 'Bruno', 'idade': 45, 'salario': 85000},
    {'nome': 'Carla', 'idade': 22, 'salario': 42000}
]

# --- Implementação Manual ---
# Tive de me lembrar da sintaxe da função 'sorted' e como usar 'lambda'
def ordenar_manual(lista, chave):
    """Ordena manualmente uma lista de dicionários por uma chave."""
    return sorted(lista, key=lambda x: x[chave])

# --- Implementação Sugerida pelo GitHub Copilot ---
# Comecei a digitar 'def ordenar_por_salario...'
# O Copilot sugeriu a função inteira imediatamente.
def ordenar_com_copilot(lista, chave):
    """
    Função sugerida pelo Copilot para ordenar uma lista de dicionários.
    (O Copilot também sugeriu o uso de 'operator.itemgetter',
    mas a sugestão com lambda foi a mais direta.)
    """
    return sorted(lista, key=lambda x: x[chave])

# Testando ambas
print("Ordenado por 'salario' (Manual):")
print(ordenar_manual(lista_funcionarios, 'salario'))

print("\nOrdenado por 'idade' (Copilot):")
print(ordenar_com_copilot(lista_funcionarios, 'idade'))
