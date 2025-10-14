import itertools
from datetime import datetime

# Substituições comuns para letras
substituicoes = {
    'a': ['a', '@', '4'],
    'b': ['b', '8'],
    'e': ['e', '3', '&'],
    'g': ['g', '6'],
    'h': ['h', '#'],
    'i': ['i', '!', '1'],
    'o': ['o', '0'],
    's': ['s', '5', '$'],
    't': ['t', '7'],
    'z': ['z', '2']
}

def gerar_variacoes(bases):
    senhas = set()

    for base in bases:
        combinacoes = []

        def substituir(i=0, atual=""):
            if i == len(base):
                for c in itertools.product(*[(letra.lower(), letra.upper()) for letra in atual]):
                    combinacoes.append(''.join(c))
                return

            letra = base[i].lower()
            opcoes = [letra] + substituicoes.get(letra, [])
            for opcao in opcoes:
                substituir(i + 1, atual + opcao)

        substituir()
        senhas.update(combinacoes)

    return sorted(senhas)

# Entrada com palavras/senhas do usuario
entradas = []
print("Digite as senhas base (digite 'sair' para terminar):")
while True:
    linha = input("> ").strip()
    if linha.lower() == "sair":
        break
    if linha:
        entradas.append(linha)

resultado = gerar_variacoes(entradas)

# Salvar no arquivo com data/hora
respostaArquivo = input("Deseja salvar as senhas em um arquivo? (s/n): ").lower().strip()
if respostaArquivo == "s":
    nome_arquivo = f"senhas_{datetime.now().strftime('%Y-%m-%d_%H-%M-%S')}.txt"
    with open(nome_arquivo, "w", encoding="utf-8") as arq:
        for s in resultado:
            arq.write(s + "\n")

    print(f"\nForam geradas {len(resultado)} senhas.")
    print(f"Arquivo salvo como: {nome_arquivo}")
    input("\nPressione ENTER para sair...")
elif respostaArquivo == "n":
    print(f"\nForam geradas {len(resultado)} senhas.")
    for i in resultado:
        print(i)
    input("\nPressione ENTER para sair...")
else:
    print("Resposta inválida")
    input("\nPressione ENTER para sair...")
