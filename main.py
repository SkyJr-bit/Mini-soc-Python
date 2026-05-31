import os

print("🛡️ MINI SOC INICIADO 🛡️\n")

print("🔍 Executando monitor de rede...")
os.system("python monitor_rede.py")

print("\n📂 Escaneando arquivos...")
os.system("python scanner_arquivos.py")

print("\n📊 Verificando logs...")
os.system("python logs_windows.py")

print("\n⚙️ Organizando arquivos...")
os.system("python organiza_sec.py")

print("\n✅ Todas as verificações concluídas!")