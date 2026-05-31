import os

print("\n📂 Escaneando arquivos suspeitos...\n")

caminho = "C:\\Users\\windows\\Desktop"
suspeitos_arquivo = ["hacker", "exploit", "backdoor"]

for root, dirs, files in os.walk(caminho):
    for file in files:
        for s in suspeitos_arquivo:
            if s in file.lower():
                print(f"⚠ Arquivo suspeito: {os.path.join(root, file)}")