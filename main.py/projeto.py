# Pedro Diagro Lopes - 568393
# João Vctor Tozzatti Matiro - 567510

import numpy as np
from datetime import datetime

def coletar_dados():
    colaboradores = []
    for i in range(5):
        print(f"\nColaborador {i+1}:")
        try:
            nome = input("Nome: ")
            departamento = input("Departamento: ")
            horas = float(input("Horas trabalhadas no dia: "))
            pausas = int(input("Pausas realizadas (quantidade): "))
            estresse = int(input("Nível de estresse (1 a 5): "))
            if estresse < 1 or estresse > 5:
                raise ValueError("Estresse deve estar entre 1 e 5.")
            tarefas = int(input("Tarefas concluídas: "))

            colaborador = {
                "nome": nome,
                "departamento": departamento,
                "horas": horas,
                "pausas": pausas,
                "estresse": estresse,
                "tarefas": tarefas
            }
            colaboradores.append(colaborador)
        except ValueError as e:
            print(f"Entrada inválida: {e}. Tente novamente.")
            return coletar_dados()
    return colaboradores


def calcular_media_horas(lista):
    return np.mean([c["horas"] for c in lista])

def maior_estresse(lista):
    return max(lista, key=lambda c: c["estresse"])["nome"]

def colaboradores_produtivos(lista):
    return [c["nome"] for c in lista if c["tarefas"] >= 5]

def alerta_equilibrio(lista):
    return [c["nome"] for c in lista if c["estresse"] >= 4 and c["pausas"] <= 1]


def analises(lista):
    horas = np.array([c["horas"] for c in lista])
    estresse = np.array([c["estresse"] for c in lista])
    return {
        "media_horas": np.mean(horas),
        "desvio_horas": np.std(horas),
        "media_estresse": np.mean(estresse)
    }

def gerar_relatorio(lista):
    stats = analises(lista)

    print("Relatorio Workbalance AI")

    print("Média de horas trabalhadas:", round(stats["media_horas"], 1), "h")

    print("Desvio padrão de horas:", round(stats["desvio_horas"], 1))
    
    print("Média de estresse:", round(stats["media_estresse"], 1))
    
    print("Colaborador mais estressado:", maior_estresse(lista))
    
    print("Colaboradores com 5+ tarefas:", colaboradores_produtivos(lista))
    
    print("Alerta de equilíbrio:", alerta_equilibrio(lista))

    try:
        with open("relatorio_workbalance.txt", "w", encoding="utf-8") as f:
    
            f.write("RELATÓRIO WORKBALANCE AI\n")
    
            f.write("Média de horas trabalhadas: " + str(round(stats["media_horas"], 1)) + "h\n")
    
            f.write("Desvio padrão de horas: " + str(round(stats["desvio_horas"], 1)) + "\n")
    
            f.write("Média de estresse: " + str(round(stats["media_estresse"], 1)) + "\n")
    
            f.write("Colaborador mais estressado: " + maior_estresse(lista) + "\n")
    
            f.write("Colaboradores com 5+ tarefas: " + str(colaboradores_produtivos(lista)) + "\n")
    
            f.write("Alerta de equilíbrio: " + str(alerta_equilibrio(lista)) + "\n")
    except:
        print("Erro ao salvar o arquivo.")

def feedback(colaborador):
   
    if colaborador["estresse"] >= 4 and colaborador["pausas"] <= 1:
        return f"{colaborador['nome']}: alta carga e poucas pausas. Sugestão: reorganize suas tarefas."
    
    elif colaborador["tarefas"] >= 5 and colaborador["estresse"] <= 3:
        return f"{colaborador['nome']}: ótimo desempenho! Continue equilibrando suas pausas."
    
    else:
        return f"{colaborador['nome']}: desempenho estável, mantenha o equilíbrio."

if __name__ == "__main__":
    colaboradores = coletar_dados()
    gerar_relatorio(colaboradores)

    print("\nFeedback individual:")
    for c in colaboradores:
        print(feedback(c))