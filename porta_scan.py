import socket

alvo = "192.168.1.132"

for porta in range(1, 1024):
    s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    s.settimeout(1)
    resultado = s.connect_ex((alvo, porta))
    
    if resultado == 0:
        print(f"Porta {porta} aberta")
    
    s.close()