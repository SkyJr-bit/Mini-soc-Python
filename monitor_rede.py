import psutil

print("\n🌐 Conexões de rede ativas:\n")

conexoes = psutil.net_connections()

for c in conexoes:
    if c.raddr:
        print(f"IP remoto: {c.raddr.ip} | Porta: {c.raddr.port}")
''