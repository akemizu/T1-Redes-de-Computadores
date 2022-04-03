import socket
import sys
import time

if len(sys.argv) == 3: #checa se usuário possui argumentos requesitados
    ip = sys.argv[1]
    port = int(sys.argv[2])
else:   
    exit(1)

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM) #criação de server UDP

server_address = (ip, port)
s.bind(server_address)  #Associa socket a um port e id
print("Digite CTRL+C para sair do chat!")

while True:
     
    print("####### Server online #######")
    data, address = s.recvfrom(4096)
    m_timestamp = time.time()
    print("\n\n 2. Server recebeu: ", data.decode('utf-8'))
    print("Timestamp:",m_timestamp)
    print ("IP/Port:", server_address,"\n\n")
    send_data = input("Digite uma mensagem a enviar => ")
    s.sendto(send_data.encode('utf-8'), address)
    r_timestamp = time.time()
    print("\n\n 1. Server enviou : ", send_data)
    print("Timestamp:",r_timestamp)
    print ("IP/Port:", server_address,"\n\n")