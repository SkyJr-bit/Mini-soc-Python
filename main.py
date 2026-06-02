    
from monitor import monitorar_rede
from colorama import Fore, init
import os
import time

init(autoreset=True)


def limpar_tela():
    os.system('cls' if os.name == 'nt' else 'clear')


def banner():
    print(Fore.GREEN + """
███╗   ███╗██╗███╗   ██╗██╗    ███████╗ ██████╗  ██████╗
████╗ ████║██║████╗  ██║██║    ██╔════╝██╔═══██╗██╔════╝
██╔████╔██║██║██╔██╗ ██║██║    ███████╗██║   ██║██║     
██║╚██╔╝██║██║██║╚██╗██║██║    ╚════██║██║   ██║██║     
██║ ╚═╝ ██║██║██║ ╚████║██║    ███████║╚██████╔╝╚██████╗
╚═╝     ╚═╝╚═╝╚═╝  ╚═══╝╚═╝    ╚══════╝ ╚═════╝  ╚═════╝
""")
    print(Fore.GREEN + "🛡️ MINI SOC - TERMINAL DE SEGURANÇA 🛡️")
    print(Fore.GREEN + "=" * 50)


def menu():
    print(Fore.YELLOW + "\n[1] Monitorar conexões")
    print("[2] Sair\n")


def monitorar():
    print(Fore.YELLOW + "\n🔍 Iniciando monitoramento...\n")
    time.sleep(1)

    resultados = monitorar_rede()

    seguros = 0
    suspeitos = 0
    perigosos = 0

    for r in resultados:
        if str(r.status) == "Seguro":
            seguros += 1
            print(Fore.GREEN + str(r))

        elif str(r.status) == "Suspeito":
            suspeitos += 1
            print(Fore.YELLOW + str(r))
            print(Fore.RED + "🚨 ALERTA DETECTADO!\n")

        else:
            perigosos += 1
            print(Fore.RED + str(r))
            print(Fore.RED + "🚨 PERIGO GRAVE!\n")

    print(Fore.CYAN + "\n📊 RESUMO:")
    print(Fore.GREEN + f"Seguros: {seguros}")
    print(Fore.YELLOW + f"Suspeitos: {suspeitos}")
    print(Fore.RED + f"Perigosos: {perigosos}")

    # salvar log
    with open("soc_log.txt", "a") as f:
        for r in resultados:
            f.write(str(r) + "\n")

    print(Fore.GREEN + "\n✅ Monitoramento finalizado.\n")


def main():
    while True:
        limpar_tela()
        banner()
        menu()

        opcao = input(Fore.CYAN + "Escolha uma opção: ")

        if opcao == "1":
            limpar_tela()
            banner()
            monitorar()
            input(Fore.CYAN + "\nPressione ENTER para voltar...")

        elif opcao == "2":
            print(Fore.GREEN + "\nSaindo do sistema...")
            break

        else:
            print(Fore.RED + "\nOpção inválida!")
            time.sleep(1)


if __name__ == "__main__":
    main()
