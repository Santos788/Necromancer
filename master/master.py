import shutil
import socket
import os

# Códigos ANSI puros — o Termux já suporta nativamente, sem precisar de libs extras
class Fore:
    LIGHTBLUE_EX = "\033[94m"
    LIGHTMAGENTA_EX = "\033[95m"
    LIGHTCYAN_EX = "\033[96m"
    LIGHTGREEN_EX = "\033[92m"
    LIGHTRED_EX = "\033[91m"
    BLUE = "\033[34m"

class Style:
    BRIGHT = "\033[1m"
    RESET_ALL = "\033[0m"

import socket

IP = "SEU_IP"
PORT = "SUA_PORT"

def verificar_zumbi():

    try:
        cliente = socket.socket()
        cliente.settimeout(2)
        cliente.connect((IP, PORT))
        cliente.close()
        return True
    except:
        return False
    
def nec(comando):
    cliente = socket.socket()
    try:
        cliente.connect((IP, PORT))
    except ConnectionRefusedError:
        print(C_WARN + "🧟 Zumbie offline ou zombie.py não está rodando." + Style.RESET_ALL)
        return 
    cliente.send(comando.encode())

    resposta = cliente.recv(4096).decode()
    print("\n🧟 Resposta do Zumbi:")
    print(resposta)

    cliente.close()

C_TITLE = Fore.LIGHTBLUE_EX + Style.BRIGHT
C_BORDER = Fore.BLUE
C_NUM = Fore.LIGHTMAGENTA_EX + Style.BRIGHT
C_TEXT = Fore.LIGHTBLUE_EX
C_PROMPT = Fore.LIGHTCYAN_EX + Style.BRIGHT
C_OK = Fore.LIGHTGREEN_EX
C_WARN = Fore.LIGHTRED_EX + Style.BRIGHT

BANNER_LINES = [
    "███╗   ██╗███████╗ ██████╗██████╗  ██████╗ ███╗   ███╗ █████╗ ███╗   ██╗ ██████╗███████╗██████╗ ",
    "████╗  ██║██╔════╝██╔════╝██╔══██╗██╔═══██╗████╗ ████║██╔══██╗████╗  ██║██╔════╝██╔════╝██╔══██╗",
    "██╔██╗ ██║█████╗  ██║     ██████╔╝██║   ██║██╔████╔██║███████║██╔██╗ ██║██║     █████╗  ██████╔╝",
    "██║╚██╗██║██╔══╝  ██║     ██╔══██╗██║   ██║██║╚██╔╝██║██╔══██║██║╚██╗██║██║     ██╔══╝  ██╔══██╗",
    "██║ ╚████║███████╗╚██████╗██║  ██║╚██████╔╝██║ ╚═╝ ██║██║  ██║██║ ╚████║╚██████╗███████╗██║  ██║",
    "╚═╝  ╚═══╝╚══════╝ ╚═════╝╚═╝  ╚═╝ ╚═════╝ ╚═╝     ╚═╝╚═╝  ╚═╝╚═╝  ╚═══╝ ╚═════╝╚══════╝╚═╝  ╚═╝",
]

# Versão média — cabe em terminais a partir de ~50 colunas (Termux em paisagem / fonte menor)
BANNER_LINES_MED = [
    "░█▀█░█▀▀░█▀▀░█▀▄░█▀█░█▄█░█▀█░█▀█░█▀▀░█▀▀░█▀▄",
    "░█░█░█▀▀░█░░░█▀▄░█░█░█░█░█▀█░█░█░█░░░█▀▀░█▀▄",
    "░▀░▀░▀▀▀░▀▀▀░▀░▀░▀▀▀░▀░▀░▀░▀░▀░▀░▀▀▀░▀▀▀░▀░▀",
]

# Versão compacta — cabe em qualquer terminal de celular em pé (~30-40 colunas)
BANNER_LINES_SMALL = [
    "▙ ▌▛▀▘▞▀▖▛▀▖▞▀▖▙▗▌▞▀▖▙ ▌▞▀▖▛▀▘▛▀▖",
    "▌▌▌▙▄ ▌  ▙▄▘▌ ▌▌▘▌▙▄▌▌▌▌▌  ▙▄ ▙▄▘",
    "▌▝▌▌  ▌ ▖▌▚ ▌ ▌▌ ▌▌ ▌▌▝▌▌ ▖▌  ▌▚ ",
    "▘ ▘▀▀▘▝▀ ▘ ▘▝▀ ▘ ▘▘ ▘▘ ▘▝▀ ▀▀▘▘ ▘",
]

# Degradê de cor (lilás claro -> azul -> roxo escuro), efeito 3D igual ao da referência
BANNER_GRADIENT = [147, 111, 105, 99, 93, 55]

def get_term_width(default=80):
    try:
        return shutil.get_terminal_size(fallback=(default, 24)).columns
    except Exception:
        return default

def print_banner():
    width = get_term_width()
    banner_width = max(len(l) for l in BANNER_LINES)
    med_width = max(len(l) for l in BANNER_LINES_MED)

    if width >= banner_width + 2:
        lines = BANNER_LINES
    elif width >= med_width + 2:
        lines = BANNER_LINES_MED
    else:
        lines = BANNER_LINES_SMALL

    print()
    for i, line in enumerate(lines):
        color = BANNER_GRADIENT[min(i, len(BANNER_GRADIENT) - 1)]
        print(f"\033[38;5;{color}m{line}{Style.RESET_ALL}")
    print()

def box_line(text, width=60):
    return C_BORDER + "|" + C_TEXT + f" {text}".ljust(width - 1) + C_BORDER + "|" + Style.RESET_ALL

def print_menu():
    term_width = get_term_width()
    width = max(36, min(60, term_width - 2))
    print(C_BORDER + "+" + "-" * (width - 2) + "+" + Style.RESET_ALL)
    print(box_line("Controle remoto — Zumbi SSH", width))
    print(C_BORDER + "+" + "-" * (width - 2) + "+" + Style.RESET_ALL)
    opcoes = [
        ("1", "Status do Zumbi"),
        ("2", "Listar arquivos da pasta Home"),
        ("3", "Ver uso de disco"),
        ("4", "Desligar Zumbi"),
        ("0", "Sair"),
    ]
    for num, desc in opcoes:
        visible = f"[{num:>2}] {desc}"
        pad = " " * max(0, (width - 3) - len(visible))
        print(C_BORDER + "| " + f"[{C_NUM}{num:>2}{C_TEXT}] {desc}" + pad + C_BORDER + "|" + Style.RESET_ALL)
    print(C_BORDER + "+" + "-" * (width - 2) + "+" + Style.RESET_ALL)

def run(opcao):
    if opcao == "1":
        nec("status")

    elif opcao == "2":
        nec("files")

    elif opcao == "3":
        nec("disk")

    elif opcao == "4":
        confirmar = input(C_WARN + "Tem certeza? (s/n): " + Style.RESET_ALL)
        if confirmar.lower() == "s":
            nec("shutdown")

    elif opcao == "0":
        print(C_OK + "Encerrando o Mestre..." + Style.RESET_ALL)
        return False

    else:
        print(C_WARN + "Opção inválida." + Style.RESET_ALL)

    return True

def main():
    os.system("clear")
    print_banner()

    if verificar_zumbi():
        print(C_OK + "ZUMBI ONLINE" + Style.RESET_ALL)

    else:
        print(C_WARN + "ZUMBI OFFLINE" + Style.RESET_ALL)

    while True:
            print_menu()
            opcao = input(C_PROMPT + "\n[$] Escolha: " + Style.RESET_ALL)
            if not run(opcao):
                break
            print()

if __name__ == "__main__":
    main()
