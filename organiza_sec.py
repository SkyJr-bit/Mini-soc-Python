import os
import shutil

pasta = "C:/Users/windows/Downloads"

destino_pdf = "C:/PDFs"
destino_img = "C:/Imagens"

# Criar pastas automaticamente
os.makedirs(destino_pdf, exist_ok=True)
os.makedirs(destino_img, exist_ok=True)

print("📂 Iniciando organização com análise de segurança...\n")

for arquivo in os.listdir(pasta):
    caminho = os.path.join(pasta, arquivo)

    if os.path.isfile(caminho):

        # 🚨 DETECÇÃO DE ARQUIVO SUSPEITO
        if "hack" in arquivo.lower():
            print(f"🚨 ALERTA: arquivo suspeito -> {arquivo}")

        # 📄 PDF
        if arquivo.lower().endswith(".pdf"):
            shutil.move(caminho, os.path.join(destino_pdf, arquivo))
            print(f"✅ PDF movido: {arquivo}")

        # 🖼️ IMAGENS
        elif arquivo.lower().endswith((".jpg", ".png")):
            shutil.move(caminho, os.path.join(destino_img, arquivo))
            print(f"✅ Imagem movida: {arquivo}")

print("\n✅ Organização finalizada com monitoramento de segurança.")