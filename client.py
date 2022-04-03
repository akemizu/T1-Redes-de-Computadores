import socket
import sys
import time

if len(sys.argv) == 3: #checa se usuário possui argumentos requesitados
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:
    exit(1)


s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM, 0) #criação de server UDP

server_address = (ip, port)

print("Digite CTRL+C para sair do chat!")


while True:
    send_data = input("Digite uma mensagem a enviar => ");
    s.sendto(send_data.encode('utf-8'), (ip, port)) 
    m_timestamp = time.time()
    print("\n\n 1. Cliente Enviou : ", send_data)
    print("Timestamp:",m_timestamp)
    print("IP/Port:",server_address,"\n\n")
    data, address = s.recvfrom(4096)
    r_timestamp = time.time()
    print("\n\n 2. Cliente Recebeu : ", data.decode('utf-8'))
    print("Timestamp:",r_timestamp)
    print("IP/Port:",server_address,"\n\n")

s.close()