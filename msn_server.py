import socket
host = ''
port = 7000
addr = (host, port)
serv_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
serv_socket.setsockopt(0,socket.SO_REUSEADDR, 1)
serv_socket.bind(addr)
serv_socket.listen(10)
print 'aguardando conexao'
con, cliente = serv_socket.accept()
print 'conectado'
print "aguardando mensagem"

for x in range(10):
    recebe = con.recv(1024)
    print "mensagem recebida: " + recebe

serv_socket.close()

