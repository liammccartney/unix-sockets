import socket
import os

socket_address = '/tmp/socket_test.sock'

if os.path.exists(socket_address):
    os.remove(socket_address)

print 'Opening socket...'

server = socket.socket(socket.AF_UNIX, socket.SOCK_STREAM)
server.bind(socket_address)
server.listen(5)

print 'Listening'
while True:
    conn, addr = server.accept()
    print 'accepted a connection'

    while True:
        data = conn.recv(1024)
        if not data:
            break
        else:
            print '-' * 20
            print data
            if data == 'DONE':
                break
    break
print '-' * 20
print 'Shutting down...'

server.close()
os.remove(socket_address)
print 'Process complete'
