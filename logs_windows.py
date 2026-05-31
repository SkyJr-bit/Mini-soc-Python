print("\n📊 Buscando eventos de falha de login...\n")

import subprocess

try:
    comando = 'wevtutil qe Security /c:5 /rd:true /f:text'
    resultado = subprocess.check_output(comando, shell=True).decode()

    if "4625" in resultado:
        print("🚨 Tentativas de login falhadas detectadas!")
    
    print(resultado)

except:
    print("Erro ao acessar logs")
