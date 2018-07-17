import socket
ip = raw_input('digite o ip de conexao: ')
port = 7000
addr = ((ip, port))

client_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
client_socket.connect(addr)

for x in range(10):
    mensagem = raw_input("Digite uma mensagem para enviar")
    client_socket.send(mensagem)
    print 'mensagem enviada'

client_socket.close()

