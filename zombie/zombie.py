import socket
import subprocess


HOST = "0.0.0.0"
PORT = 5050

server = socket.socket()
server.bind((HOST, PORT))
server.listen(1)

print("🧟 ZOMBIE ONLINE - Esperando o Mestre...")

while True:
    conn, addr = server.accept()

    comando = conn.recv(1024).decode().strip()
    print(f"\n📡 Mestre enviou: {comando}")

    if comando == "status":
        resposta = subprocess.getoutput("uptime -p")
    elif comando == "files":
        resposta = subprocess.getoutput("ls ~")
    elif comando == "disk":
        resposta = subprocess.getoutput("df -h /")
    elif comando == "shutdown":
        resposta = "Desligando Zumbi..."
        conn.send(resposta.encode())
        conn.close()
        subprocess.run("shutdown now", shell=True)
        continue
    else:
        resposta = "Comando desconhecido."

    print(resposta)
    conn.send(resposta.encode())
    conn.close()


